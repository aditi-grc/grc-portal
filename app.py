import streamlit as st

st.set_page_config(layout="wide")

st.title("GRC Compliance Portal")

st.sidebar.title("Navigation")

framework = st.sidebar.selectbox(
"Select Framework",
[
"ISO 27001:2022",
"SOC 2",
"GDPR",
"CE & CE+"
]
)

entity = st.sidebar.selectbox(
"Select Entity",
[
"AtomSec",
"Group",
"Europe",
"APAC",
"LATAM"
]
)

st.header("Selection")

st.write("Framework:",framework)

st.write("Entity:",entity)


st.markdown("---")

st.header("Framework Overview")

if framework == "ISO 27001:2022":

    st.subheader("ISO 27001 Checklist")

    st.write("Steps")

    st.write("- Define ISMS Scope")

    st.write("- Perform Risk Assessment")

    st.write("- Define Controls")

    st.write("- Implement Controls")

    st.write("- Internal Audit")


    st.write("Policies")

    st.write("- Information Security Policy")

    st.write("- Access Control Policy")

    st.write("- Backup Policy")

    st.write("- Incident Response Policy")


    st.write("Evidence")

    st.write("- Risk Assessment Report")

    st.write("- Access Review Logs")

    st.write("- Backup Logs")

    st.write("- Training Records")
