# Pythonic Patterns & Anti-Patterns

This guide outlines best practices for building robust AI APIs with FastAPI, focusing on Pydantic and Asynchronous programming.

## Recommended Practices (✅)

### 1. Declarative Schema Validation
Use Pydantic's `BaseModel` and `Field` for robust, declarative payload validation at the application boundary.
```python
from pydantic import BaseModel, Field
from typing import List

class ResumePayload(BaseModel):
    name: str = Field(..., min_length=1, description="Full name of the candidate")
    skills: List[str] = Field(..., min_length=1, description="List of technical skills")
    years_of_experience: int = Field(..., gt=0, description="Total years of experience")
```

### 2. Non-blocking Delays
Use `await asyncio.sleep()` to simulate latency or await I/O, preserving the event loop's concurrency.
```python
import asyncio

async def my_async_worker():
    await asyncio.sleep(0.5) 
```

### 3. Compliant SSE Payloads
Format streaming chunks accurately with the `data: ` prefix and `\n\n` delimiter using Python f-strings and `json.dumps`.
```python
import json

async def async_llm_generator(word: str):
    payload = {"token": word + " "}
    yield f"data: {json.dumps(payload)}\n\n"
```

### 4. Graceful Stream Degradation
If an error occurs during an active stream, yield an error payload inline rather than raising a hard exception.
```python
async def stream_handler(prompt: str):
    if not prompt.strip(): 
        yield f"data: {json.dumps({'error': 'Prompt cannot be empty'})}\n\n"
        return
```

---

## Anti-Patterns to Avoid (❌)

### 1. Thread Blocking
Never use `time.sleep()` in an asynchronous context; it blocks the entire event loop and degrades server concurrency.
```python
# BAD: Blocks the entire server thread
import time
def fake_generator():
    time.sleep(0.5)
    yield "token"
```

### 2. Mid-stream Exceptions
Do not raise an `HTTPException` inside an active generator. Once the HTTP 200 header has been transmitted, raising an exception leads to broken client connections.
```python
# BAD: Crashes the active stream connection
async def stream_handler(prompt: str):
    if not prompt:
        raise HTTPException(status_code=400, detail="Empty prompt")
```

### 3. Missing Stream Headers
Always configure the `Cache-Control: no-cache`, `X-Accel-Buffering: no`, and `text/event-stream` headers. Failing to do so allows intermediate proxies to buffer the stream, completely breaking the real-time user experience.
