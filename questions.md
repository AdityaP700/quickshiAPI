Project 1: The Strict JSON Gateway
Task: Build an API that accepts a POST request with a resume (Name, list of skills, years of experience).

goal : use pydantic to ensure the
years_of_experience is a positive integer
and skills is a list of strings

FastAPI should return a 422 unprocessable Entity
if the data is garbage

# Let the framework do the heavy lifting
# In Pydantic v1, the decorator was @validator
# in pydantic v2, the decorator is @field_validator

Requirements : POST /resume
payload : JSON body with name(strings) ,
skills(list of strings),
years of experience(integer)

constraints :
 - name cant be empty
 - skills must contain at least one skill
 - years of experience must be positive integer

- Expected Workflow: If a user sends a payload that breaks any constraint, FastAPI should automatically reject it with a 422 Unprocessable Entity error.

