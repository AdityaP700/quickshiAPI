## Task 2: Real-time LLM Streaming Simulation

### Objective
Modern AI product UX dictates that users must not be blocked by synchronous loading states during generation. The goal is to mimic a production LLM streaming pipeline by emitting generated tokens to the client in real-time.

### Technical Requirements
- **Endpoint:** `GET /chat/stream`
- **Payload Schema:** Query parameter `prompt` (String)
- **Workflow Architecture:** Implement an asynchronous generator pattern to handle stream yielding.

### Constraints
- Simulate network and inference latency by introducing a non-blocking `0.5s` delay per token using `asyncio.sleep()`.
- Deliver the payload using FastAPI's `StreamingResponse` wrapping Server-Sent Events (SSE).
