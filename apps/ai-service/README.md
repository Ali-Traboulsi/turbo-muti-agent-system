# AI Service

## Local Development

1. Ensure `docker-compose up -d` is running (spins up Redis + Dapr placement).
2. Copy Dapr YAMLs:
   ```bash
   cp ../../packages/dapr-config/*.yaml dapr/components/
   ```
