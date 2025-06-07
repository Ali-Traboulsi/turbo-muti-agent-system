export interface AgentTaskResult {
  taskId: string
  agentName: string
  result: string
  createdAt: string // ISO timestamp
}

export interface AgentTask {
  taskId: string
  agentName: string
  task: string
  createdAt: string // ISO timestamp
}
