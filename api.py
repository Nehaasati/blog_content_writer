from fastapi import FastAPI
from pydantic import BaseModel
from workflow import build_workflow

app = FastAPI(title="Content Writer Workflow API")

workflow = build_workflow()

class ThemeRequest(BaseModel):
    theme: str

@app.post("/generate/")
def generate(req: ThemeRequest):
    result = workflow.invoke({"theme": req.theme})
    return {"final_article": result["final"]}

