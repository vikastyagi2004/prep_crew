import json
from agents import Agent
 
 
def parse_json(raw):
    raw = raw.replace("```json", "").replace("```", "").strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"match_score": 0, "matched_skills": [], "missing_skills": [],
                "summary": "Screener did not return valid JSON. Run again."}
 
 
screener = Agent(
    "Screener",
    "You are a recruiter. Compare the resume with the job description. "
    "Reply ONLY with JSON like: "
    '{"match_score": 72, "matched_skills": ["Python"], '
    '"missing_skills": ["Docker"], "summary": "one line"}',
)

coach = Agent(
    "Coach",
    "You are a career coach for college students. Using the screening "
    "report and the resume, rewrite 3 resume bullet points to fit the job, "
    "then list 3 things to learn or build next. Never invent experience "
    "the student does not have.",
)
interviewer = Agent(
    "Interviewer",
    "You are a hiring manager. Using the job description and the "
    "candidate's missing skills, write 5 numbered interview questions, "
    "from easy to hard.",
)

def run_crew(resume, jd):
    # Agent 1 sees everything and writes a structured report
    report = parse_json(screener.speak(f"JOB:\n{jd}\n\nRESUME:\n{resume}"))
    missing = ", ".join(report.get("missing_skills", []))
 
    # Agent 2 sees the report and the resume, not the job
    coach_msg = f"REPORT:\n{json.dumps(report, indent=2)}\n\nRESUME:\n{resume}"
    advice = coach.speak(coach_msg)
 
    # Agent 3 sees the job and the gaps, not the resume
    interviewer_msg = f"JOB:\n{jd}\n\nMISSING SKILLS: {missing}"
    questions = interviewer.speak(interviewer_msg)
    return report, advice, questions

if __name__ == "__main__":
    resume = open("sample_resume.txt", encoding="utf-8").read()
    jd = open("sample_jd.txt", encoding="utf-8").read()
    report, advice, questions = run_crew(resume, jd)
    print("MATCH SCORE:", report.get("match_score"))
    print("MISSING:", report.get("missing_skills"))
    print("\n--- COACH ---\n" + advice)
    print("\n--- INTERVIEWER ---\n" + questions)
