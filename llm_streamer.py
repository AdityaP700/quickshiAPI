from fastapi import FastAPI
from fastapi.responses import StreamingResponse
#since we want to introduce a delay
import time
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
def fake_llm_generator():
    ## taking input as a string of words
    words = ["Here","is","your","streaming","answer","from","the","LLM"]
    for word in words:
        time.sleep(0.5)
        yield word+""
## total 4 seconds to yield 8 words
@app.get("/chat/stream")
async def chat_stream(prompt:str):
    ##instead of a massive response payload
    ## we are keeping the HTTP connection open
    ## streams data to the client chunk by chunk ,token by token
    return StreamingResponse(fake_llm_generator)

## questions : What happens if two users hit this
#  endpoint at exactly the same time?
## invalid sse format
## missing headers : without media type ,proxies and browsers might buffer the response wiatinting
