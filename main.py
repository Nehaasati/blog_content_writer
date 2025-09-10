def main():
    print("Hello from blog-writer!")
import sys
import subprocess

def run_fastapi():
    subprocess.run(["uvicorn", "api:app", "--reload"])

def run_streamlit():
    subprocess.run(["streamlit", "run", "streamlit_app.py"])

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "api":
        run_fastapi()
    else:
        run_streamlit()


