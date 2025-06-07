from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from langchain import OpenAI, LLMChain, PromptTemplate
from dapr.clients import DaprClient
from dapr.clients.grpc._request import PublishEventRequest
import uuid
import json

app = FastAPI()


# Example Pydantic model for incoming requests:
class GenerationRequest(BaseModel):
    prompt: str
    agent_id: str


# Initialize LangChain LLM
llm = OpenAI(temperature=0.7)


# Example simple generation endpoint
@app.post("/generate")
async def generate(request: GenerationRequest):
    template = "Agent {agent_id}, process this prompt: {prompt}"
    prompt_template = PromptTemplate(
        input_variables=["agent_id", "prompt"], template=template
    )
    chain = LLMChain(llm=llm, prompt=prompt_template)
    result = chain.run({"agent_id": request.agent_id, "prompt": request.prompt})
    # After generating, publish to a Dapr pub/sub topic "agent-results"
    with DaprClient() as client:
        event = {
            "taskId": str(uuid.uuid4()),
            "agentName": request.agent_id,
            "result": result,
            "createdAt": __import__("datetime").datetime.utcnow().isoformat(),
        }
        client.publish_event(
            pubsub_name="redis-pubsub",
            topic_name="agent-results",
            data=json.dumps(event),
        )
    return {"status": "published", "payload": event}
