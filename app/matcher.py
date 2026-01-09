from app.scoring import calculate_score
from app.resume_generator import generate_resume_summary

def analyze_match(student, jd):
    student_skills = set(skill.lower() for skill in student["skills"])
    jd_words = set(jd.lower().split())

    matched_skills = student_skills.intersection(jd_words)
    missing_skills = jd_words - student_skills

    score = calculate_score(len(matched_skills), len(jd_words))
    resume = generate_resume_summary(student)

    return {
        "match_summary": f"Student matches {len(matched_skills)} required skills.",
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills),
        "confidence_score": score,
        "tailored_resume_summary": resume
    }
