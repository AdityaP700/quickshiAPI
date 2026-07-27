# import os
from contextlib import asynccontextmanager
from fastapi import FastAPI,Depends,Request
import asyncio
#a fake 2GB asset

class MockHeavyModel:
    def __init__(self):
        self.is_loaded=False
        #set the value of the model loaded being false
        #it loads the model at an interval of 3s
    async def load_weights(self):
        print("loading a massive model into VRAM....(simulating 3s delay)")
        await asyncio.sleep(3)
        #once loaded ,the state becomes true
        self.is_loaded=True
        print("model ready to serve the requests")

    def generate(self,prompt:str)->str:
        if not self.is_loaded:
            raise RuntimeError("Model isnt loaded yet!")
        return f"simulated LLm response for :{prompt}"

    def cleanup(self):
        print("Flushing model from memory")
        self.is_loaded=False
@asynccontextmanager
async def lifespan(app:FastAPI):
    model=MockHeavyModel()
    await model.load_weights()

    #the fastapi loads the model
    #and place it in the locker
    app.state.ai_model=model
    #the fastapi freezes lifespan when it hits the yield
    yield

    app.state.ai_model.cleanup()

app=FastAPI()
def get_model(request:Request)->MockHeavyModel:
    """
    it fetches the model from the app state and grabs the model when the user initiates a request
    """
    return request.app.state.ai_model
@app.post("/v1/generate")
def generate_text(prompt:str,model:MockHeavyModel=Depends(get_model)):
    #before i even run this ,i need to fetch the model and load it from the locker
    #after fetching it will simply drop the model to the model argument for further use
    """
    fastapi automatically calls get_model() ,grabs the loaded model
    and passes it in as the "model" argument
    """
    response = model.generate(prompt)
    return {"status":"success","data":response}
# simulates a slow ,heavy model loading exactly once at startup
#attaches the model to the application's internal state
#uses a dependency to inject that model into the route ,preventing you from using
#messy global variables



#a graceful teardown to release resources.
#str,model:MockHeavyModel=Depends(get_model)

#: This shows you the danger of global states.
#  Without the Lifespan manager orchestrating the startup event
#  and DI passing the ready instance,
# your code can easily try to use an uninitialized
#  asset.