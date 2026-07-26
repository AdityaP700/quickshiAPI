from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List
#start the fastAPI server
app = FastAPI()
#Retrieves data from
# we are creating a pydantic model
class ResumePayload(BaseModel):
    name:str
    skills:List[str]
    years_of_experience:int


@app.post("/resume")

#read from the root
def submit_resume(resume: ResumePayload):
    #return the response
    if len(resume.name.strip())==0:
        raise HTTPException(status_code=400,details="Name cannot be empty")

    if len(resume.skills)==0:
        raise HTTPException(status_code=400,details="Must have at least one skill")

    if resume.years_of_experience<=0:
        raise HTTPException(status_code=400,details="Years of experience must be positive")


    return {"message": f"Resume accepted for {resume.name}","status":"success"}
