from agents import Agent
from crew import run_crew
 
reviewer = Agent(
    "Reviewer",
    "You check career advice against the resume. List any claim "
    "the resume does not support, or reply 'All good'.",
)
 
resume = open("sample_resume.txt", encoding="utf-8").read()
jd = open("sample_jd.txt", encoding="utf-8").read()
report, advice, questions = run_crew(resume, jd)
print(reviewer.speak(f"RESUME:\n{resume}\n\nADVICE:\n{advice}"))

