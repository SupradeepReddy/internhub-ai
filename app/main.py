from fastapi import FastAPI
from pydantic import BaseModel
from app.matcher import analyze_match

app = FastAPI(title="InternHub AI Matcher")
class StudentProfile(BaseModel):
    name: str
    skills: list[str]
    interests: list[str]
    experience: str

class InternshipRequest(BaseModel):
    student_profile: StudentProfile
    internship_description: str

@app.post("/analyze")
def analyze(request: InternshipRequest):
    return analyze_match(
        request.student_profile.model_dump(),
        request.internship_description
    )
