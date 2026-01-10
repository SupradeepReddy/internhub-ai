from app.matcher import analyze_match

def run_cli():
    print("\n=== InternHub CLI – Internship Match Checker ===\n")

    name = input("Enter student name: ")

    skills_input = input("Enter skills (comma separated): ")
    skills = [skill.strip() for skill in skills_input.split(",")]

    interests_input = input("Enter interests (comma separated): ")
    interests = [interest.strip() for interest in interests_input.split(",")]

    experience = input("Enter short experience summary: ")

    internship_description = input("\nEnter internship description:\n")

    student_profile = {
        "name": name,
        "skills": skills,
        "interests": interests,
        "experience": experience
    }

    result = analyze_match(student_profile, internship_description)

    print("\n--- Internship Match Result ---\n")

    print("Match Summary:")
    print(result["match_summary"], "\n")

    print("Matched Skills:")
    for skill in result["matched_skills"]:
        print(f"- {skill}")

    print("\nMissing Skills:")
    for skill in result["missing_skills"]:
        print(f"- {skill}")

    print(f"\nConfidence Score: {result['confidence_score']}%")

    print("\nSuggested Resume Summary:")
    print(result["tailored_resume_summary"])

if __name__ == "__main__":
    run_cli()
