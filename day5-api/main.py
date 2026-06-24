from fastapi import FastAPI

app = FastAPI()

@app.get("/details")
def details():
    return {
        "name": "Ankur Bandopadhyay",
        "skills": [
            "Git and GitHub workflows",
            "Python CLI development",
            "React and component-based UI"
        ]
    }