from fastapi import FastAPI

app = FastAPI()
#Retrieves data from
#a server without modifying anything
@app.get("/")
#read from the root
def read_root():
    #return the response 
    return {"message": "Hello world"}
