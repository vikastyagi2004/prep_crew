# Placement Prep Crew – Multi-Agent AI Resume Analyzer

Placement Prep Crew is an AI-powered application that helps candidates prepare for job opportunities by analyzing their resumes against job descriptions. It uses a **multi-agent AI architecture** in which three specialized AI agents collaborate to evaluate resume relevance, suggest improvements, and generate interview questions.

Built using Python, Groq API, and Streamlit, the project demonstrates how multiple AI agents can work together to solve a real-world problem.

## Features

- **Resume Screening:** Analyzes a resume against a job description and generates an estimated match score.
- **Skill Gap Analysis:** Identifies matching skills and highlights missing skills required for the role.
- **Resume Improvement:** Suggests improved resume bullet points and recommends areas to learn or build.
- **Interview Preparation:** Generates five interview questions ranging from easy to difficult based on the job description and identified skill gaps.
- **Multi-Agent Collaboration:** Uses three specialized AI agents with separate responsibilities.
- **Structured Communication:** Uses JSON to exchange structured information between agents.
- **Interactive Interface:** Provides a simple web interface built with Streamlit.

## AI Agent Architecture

The application consists of three specialized agents:

### 1. Screener Agent
- Compares the candidate's resume with the job description.
- Evaluates the relevance of the candidate's skills and experience.
- Generates a match score, matched skills, missing skills, and an overall summary.
- Returns its analysis in JSON format.

### 2. Coach Agent
- Uses the screening report and resume as input.
- Suggests three improved resume bullet points.
- Recommends three things the candidate should learn or build.
- Focuses on improving the candidate's profile without inventing experience.

### 3. Interviewer Agent
- Uses the job description and identified missing skills.
- Generates five relevant interview questions.
- Organizes questions from easy to difficult.
- Helps candidates prepare for role-specific interviews.

## How It Works

The application follows a sequential multi-agent workflow:

1. The user enters their resume and the target job description.
2. The Screener Agent analyzes both inputs.
3. The screening result is converted into structured JSON data.
4. The Coach Agent receives the screening report and resume to suggest improvements.
5. The Interviewer Agent receives the job description and missing skills to generate interview questions.
6. The application displays the results through the Streamlit interface.

### Workflow

```text
             User Input
                 |
        Resume + Job Description
                 |
                 v
          Screener Agent
                 |
          Structured JSON
                 |
          +------+------+
          |             |
          v             v
      Coach Agent   Interviewer Agent
          |             |
          v             v
    Resume Advice   Interview Questions
          |             |
          +------+------+
                 |
                 v
           Streamlit UI
                 |
                 v
           Final Results
```

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Groq API | LLM integration |
| LLM (`openai/gpt-oss-20b`) | AI-powered analysis and generation |
| Multi-Agent Architecture | Dividing tasks among specialized agents |
| Prompt Engineering | Defining agent roles and responsibilities |
| JSON | Structured communication between agents |
| Streamlit | Interactive web application |
| python-dotenv | Environment variable management |

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/vikastyagi2004/prep_crew.git
cd prep_crew
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install groq python-dotenv streamlit
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from [Groq Console](https://console.groq.com/).

**Important:** Never upload your `.env` file or expose your API key publicly.

### 5. Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to access the application.

## Key Concepts Demonstrated

- Building AI agents using Python classes.
- Connecting Python applications with LLMs through the Groq API.
- Using system prompts to define agent responsibilities.
- Designing a multi-agent workflow.
- Passing structured data between agents using JSON.
- Managing context and controlling which information each agent receives.
- Executing independent agents in parallel using Python's `ThreadPoolExecutor`.
- Building an interactive AI application using Streamlit.

## Future Improvements

- Add a Reviewer Agent to validate AI-generated suggestions.
- Execute independent agents in parallel to reduce response time.
- Add a cover letter generation agent.
- Support comparison of multiple job descriptions.
- Improve error handling and JSON validation.
- Add resume upload support and downloadable reports.

## Limitations

- The match score is an AI-generated estimate, not an actual hiring decision.
- AI-generated suggestions and interview questions may not always be accurate.
- Results depend on the quality of the resume and job description.
- Avoid submitting sensitive personal information unnecessarily when using external AI services.

## Learning Outcome

This project provided hands-on experience with LLM integration, prompt engineering, multi-agent collaboration, structured JSON communication, context management, and building AI-powered applications with Python and Streamlit.

---

**Developed as a hands-on Multi-Agent AI project.**