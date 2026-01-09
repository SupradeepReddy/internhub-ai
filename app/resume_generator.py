def generate_resume_summary(student):
    return (
        f"{student['name']} is a Computer Science student skilled in "
        f"{', '.join(student['skills'])}. Interested in "
        f"{', '.join(student['interests'])} and seeking an AI internship."
    )
