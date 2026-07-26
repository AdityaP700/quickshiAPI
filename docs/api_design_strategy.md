## API Design Strategy

When architecting a FastAPI microservice, establish the API contract by strictly defining the following four vectors before implementation:

1. **Endpoint Topology:** The HTTP Method (GET, POST, PUT, DELETE) and the route path.
2. **Payload Contract:** The expected data structures (Query params, JSON bodies, Form data) and strict validation schemas to be enforced by Pydantic.
3. **Execution Workflow:** Determine the concurrency model. Will the endpoint perform synchronous CPU-bound tasks or asynchronous I/O-bound tasks?
4. **Constraints & Trade-offs:** Identify resource limits, latency requirements (e.g., streaming vs. batch processing), and defined failure handling boundaries.
