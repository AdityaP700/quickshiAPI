## Foundational API & HTTP Concepts

### HTTP Protocol in AI Workflows
- **POST:** Submits stateful data (e.g., executing a prompt, uploading training payloads).
- **GET:** Retrieves stateless data without mutation (e.g., polling model status).
- **PUT / PATCH:** Modifies existing resources (e.g., updating fine-tuning parameters).
- **DELETE:** Purges data (e.g., dropping vector indices or chat histories).

### Pydantic Validation Constraints
Use standard constraints for robust boundary checks:
- **Strings/Arrays:** `min_length`, `max_length`.
- **Numerics:** `gt` (greater than), `lt` (less than), `ge` (greater/equal), `le` (less/equal).

### The EventSource API (SSE)
For real-time streaming to the frontend, the `EventSource` web API seamlessly consumes `text/event-stream` endpoints.
- **Protocol Markers:** Payloads must start with `data: ` and flush via `\n\n`.
- **Connection Persistence:** A single long-lived HTTP connection is established, avoiding WebSockets' bidirectional overhead for simple uni-directional token streams.

### HTTP State Constraints
Once an endpoint returns a `200 OK` header to initiate a stream, the HTTP status is finalized. Late-stage exceptions will violently crash the transport layer. Defensive programming requires yielding error states natively within the SSE data contract rather than raising application exceptions.
