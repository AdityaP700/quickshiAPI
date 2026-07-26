whenever we are developing a fastapi server

## Always ask for the 4 questions
- Endpoint : GET or POST or what
- Payload: what its expected to carry
- Workflow : how it should work ,is it async ,or sync or static
-Constraint : what could be the limit ,or tradeoff

- Constraint : Must simulate network/GPU latency by sleeping for 0.5 seconds between each word. Must use FastAPI's StreamingResponse.