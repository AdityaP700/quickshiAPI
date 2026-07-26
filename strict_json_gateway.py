from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from typing import List
#start the fastAPI server
app = FastAPI()
#Retrieves data from
# we are creating a pydantic model
class ResumePayload(BaseModel):
    name:str = Field(...,min_length=1,description="Full name of the candidate")
    # min_length=1 on a List ensures it cannot be an empty array []
    skills : List[str]= Field(...,min_length=1,description="List of technical skills")
    # gt=0 means strictly "greater than 0"
    years_of_experience : int =Field(...,gt=0,description="Total years of experience")

@app.post("/resume")

#read from the root
def submit_resume(resume: ResumePayload):
    #return the response
    """if the payloadis invalid
    fastAPI automatically intercepts it and returns
    a beautiful error 422 json detailing exactly which fields
    failed"""

    return {
        "message": f"Resume accepted for {resume.name}",
        "data_extracted":{
            "top_skill":resume.skills[0],
            "seniority_level":"Senior" if resume.years_of_experience>5 else "Junior "
        }
        }
