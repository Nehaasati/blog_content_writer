import streamlit as st
from workflow import build_workflow

workflow = build_workflow()

st.set_page_config(page_title="AI Content Writer", page_icon="✍️")
st.title("✍️ AI Content Writer")

theme = st.text_input("Enter a theme:", placeholder="e.g. The Future of AI")

if st.button("Generate Article"):
    if theme.strip():
        with st.spinner("Generating article..."):
            result = workflow.invoke({"theme": theme})
            st.subheader("✅ Final Article")
            st.write(result["final"])
    else:
        st.warning("Please enter a theme first.")

