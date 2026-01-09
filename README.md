# InternHub – AI Internship Matching Backend

## Overview
This project is a simple backend service built for the InternHub assignment.
It analyzes a student profile and an internship description to check how well the student matches the role.

The goal of this project is to focus on problem understanding, logical thinking, and clear implementation rather than complex UI or systems.

---

## What This Project Does
The backend takes the following inputs:
- Student skills, interests, and experience
- Internship description text

Based on this, it provides:
- A short internship match summary
- Matched and missing skills
- A confidence / ATS-style score
- A tailored resume summary suitable for the given internship

---

## How It Works
1. The API receives student details and internship description as JSON input.
2. Skills are compared using simple keyword matching logic.
3. A confidence score is calculated based on skill overlap.
4. A resume summary is generated using the student’s profile and interests.
5. The result is returned as a structured JSON response.

The API can be tested directly using FastAPI’s built-in Swagger interface.

---

## Logic and Design Decisions
- Kept the implementation simple and easy to explain.
- Used rule-based logic to make scoring transparent.
- Avoided unnecessary frontend or authentication layers.
- Focused on clarity and correctness over complexity.

---

## Tech Stack Used
- Python
- FastAPI

---

## Assumptions
- Skill relevance is identified using keyword matching.
- The confidence score is indicative and not an official ATS score.
- Resume generation is limited to a concise professional summary.
- No frontend UI is required as per the assignment instructions.

---


