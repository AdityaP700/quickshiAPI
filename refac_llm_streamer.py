from fastapi import FastAPI,HTTPException
from fastapi.responses import StreamingResponse
## asyncio is a built-in Python library that provides
# the engine for running asynchronous
import asyncio
import json
# #since we want to introduce a delay
# import time
## the idea here is to stream the words
## given the prompt provided ,so for example
## if one of the users spins up the function
## then it will start to stream (fake_llm_generator)
## the issue is that ,you wanna stream right
##so you correctly yield cuz i wanted a conveyor belt that pushes
## out words one by one
## i added time.sleep() ,bcuz i thought ,an llm doesnt dump
## all texts instantly ,it takes time to generate ,i need to force a half second
## delay b/w words to simulate that thinking
app = FastAPI()
async def async_llm_generator(prompt:str):
    ## taking input as a string of words
    # if not TRUE/FALSY ?? as in like
    # an empty string "" is considered Falsy
    if not prompt.strip():
        # You cannot raise an HTTPException inside a generator and have it return a clean 4xx code
        # to the client once the 200 OK stream has started. You must yield an error event instead.
        yield f"data: {json.dumps({'error': 'Prompt cannot be empty'})}\n\n"
        return

    words = ["Here","is","your","streaming","answer","from","the","LLM"]
    for word in words:
        await asyncio.sleep(0.5)
        ## The Raw Data Structure : Payload
        payload={"token":word+" "}
        ##  It takes that Python dictionary
        # converts it into a clean string of text.
        # This is a Python f-string that wraps your serialized
        # JSON string inside the strict Server-Sent Events (SSE)
        yield f"data: {json.dumps(payload)}\n\n"
    # Standard practice to tell
    # the client the stream is finished
    yield f"data:[DONE]\n\n"
## total 4 seconds to yield 8 words
@app.get("/chat/stream")
async def chat_stream(prompt:str=""):
    ##instead of a massive response payload
    ## we are keeping the HTTP connection open
    ## streams data to the client chunk by chunk ,token by token
    """
returns a streaming response that the browsers
eventsource API can consume """
    return StreamingResponse(
        async_llm_generator(prompt),
        media_type="text/event-stream",
        ## so while i am sending any package
        #3 i need to have a label so that the server could understand
        ## how to handle the package
        # Adding headers to prevent
        # proxies/CDNs from buffering the stream
        headers={
            ## i am telling the cloudfare to not store or cache any information
            "Cache-Control":"no-cache",
            ## , standard HTTP/1.1 requests
            # close the underlying TCP socket connection
            "Connection":"keep-alive",
            ##it waits to gather chunks of data from upstream
            # (FastAPI) until it fills a buffer (usually 4KB or 8KB)
            # before sending it to the client to save network packe
            "X-Accel-Buffering":"no"
        }
    )

## questions : What happens if two users hit this
#  endpoint at exactly the same time?
## invalid sse format
## missing headers : without media type ,proxies and browsers might buffer the response wiatinting
