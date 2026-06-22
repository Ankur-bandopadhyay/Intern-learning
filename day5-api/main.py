from fastapi import FastAPI

app = FastAPI()

@app.get("/about")
def about():
    return {
        "name": "Ankur Bandopadhyay",
        "skills": [
            "Git and GitHub workflows",
            "Python CLI development",
            "React and component-based UI"
        ]
    }