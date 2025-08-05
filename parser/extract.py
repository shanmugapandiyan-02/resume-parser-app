import pdfplumber
import re

# Predefined list of real tech skills (expandable)
KNOWN_SKILLS = [
    "HTML", "CSS", "JavaScript", "Python", "SQL", "Flask", "React", "Angular",
    "Node.js", "MongoDB", "Express", "Bootstrap", "Git", "GitHub", "AWS",
    "MySQL", "PostgreSQL", "Docker", "Kubernetes", "Jenkins", "Java", "C++",
    "C", "Linux", "VS Code", "IntelliJ", "Eclipse", "Power BI", "Tableau",
    "REST API", "GraphQL", "UI", "UX", "JSON", "XML"
]

def parse_resume(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    # Extract Name & Email
    name = text.split('\n')[0] if text else "Unknown"
    email = re.search(r'[\w\.-]+@[\w\.-]+', text)

    # Normalize text
    lower_text = text.lower()

    # Check each known skill in resume text
    found_skills = []
    for skill in KNOWN_SKILLS:
        if skill.lower() in lower_text:
            found_skills.append(skill)

    return {
        'name': name.strip(),
        'email': email.group(0) if email else "Not found",
        'highlighted_skills': found_skills,
        'other_skills': [],  # Optional: fill with keywords if needed
        'raw_text': text
    }
