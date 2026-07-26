## In 2026, if you are building an AI product and you make the user stare at a spinning loading wheel for 15 seconds while an LLM generates a response, your product will fail. Streaming tokens back to the client in real-time is an absolute baseline requirement for any AI Engineering role.


for this ,the task is to mimic the fastapi framework while the LLm is streaming

## the requirements :
- Endpoint : GET /chat/stream
- Payload : accepts a prompt as a string
- workflow : uses an async generator 
- Constraint