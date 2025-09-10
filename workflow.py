from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Define the LLM
llm = ChatGroq(model="gemma2-9b-it", temperature=0.7)


# 1. Topic Generation Node
def generate_topics(state):
    theme = state["theme"]
    response = llm.invoke(f"Suggest 3 engaging content topics around: {theme}")
    return {"topics": response.content}


# 2. Outline Generation Node
def generate_outline(state):
    topic = state["topics"]
    response = llm.invoke(f"Create a detailed outline for this topic:\n{topic}")
    return {"outline": response.content}


# 3. Draft Writing Node
def write_draft(state):
    outline = state["outline"]
    response = llm.invoke(f"Write a detailed article draft based on this outline:\n{outline}")
    return {"draft": response.content}


# 4. Editing Node
def edit_draft(state):
    draft = state["draft"]
    response = llm.invoke(f"Polish this draft for grammar, clarity, and flow:\n{draft}")
    return {"polished": response.content}


# 5. Final Review Node
def final_review(state):
    polished = state["polished"]
    response = llm.invoke(f"Provide a final clean version of this article:\n{polished}")
    return {"final": response.content}


# 🔹 Build Workflow Function
def build_workflow():
    workflow = StateGraph(dict)

    workflow.add_node("topic_gen", generate_topics)
    workflow.add_node("outline_gen", generate_outline)
    workflow.add_node("draft_writer", write_draft)
    workflow.add_node("editor", edit_draft)
    workflow.add_node("reviewer", final_review)

    # Define execution order
    workflow.set_entry_point("topic_gen")
    workflow.add_edge("topic_gen", "outline_gen")
    workflow.add_edge("outline_gen", "draft_writer")
    workflow.add_edge("draft_writer", "editor")
    workflow.add_edge("editor", "reviewer")
    workflow.add_edge("reviewer", END)

    return workflow.compile()
