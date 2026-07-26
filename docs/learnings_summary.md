# Core Architectural Learnings

1. **The FastAPI Advantage:** FastAPI excels in AI workloads because it natively supports asynchronous I/O. This allows the server to efficiently handle concurrent requests (like waiting for lengthy LLM generation responses) without blocking the main execution thread.
2. **Pydantic Validation:** By enforcing strict data contracts at the API boundary, Pydantic ensures payloads are structurally sound before execution begins, significantly reducing runtime errors and boilerplate validation logic.
3. **Asynchronous Execution:** Unlike synchronous blocking operations, `async`/`await` patterns allow the CPU to multiplex tasks. While the application awaits a response from an external API (like OpenAI), the server remains responsive to other incoming HTTP requests.
4. **Server-Sent Events (SSE):** SSE provides a lightweight, unidirectional channel for streaming text tokens back to the client over a persistent HTTP connection. This eliminates the poor user experience of waiting for complete batch generation.
5. **Streaming Error Management:** Once a `StreamingResponse` initiates (by sending a 200 OK header), traditional HTTP exceptions cause abrupt connection crashes. The robust, production-ready pattern is to gracefully yield JSON-formatted error events down the active stream.
