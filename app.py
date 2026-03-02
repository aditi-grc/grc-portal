import streamlit as st

st.set_page_config(layout="wide")

# ======================
# NAVIGATION BAR
# ======================

st.title("GRC TOOL - ATOMSEC")

col1,col2,col3,col4 = st.columns(4)

with col1:
    page = st.selectbox(
        "Frameworks",
        ["Home","ISO 27001:2022","SOC2","GDPR","CE/CE+"]
    )

with col2:
    entity = st.selectbox(
        "Entity",
        ["AtomSec","Group","Europe","APAC","LATAM"]
    )

with col3:
    about_btn = st.button("About")

with col4:
    contact_btn = st.button("Contact")

st.divider()

# ======================
# HOMEPAGE
# ======================

if page == "Home" and not about_btn and not contact_btn:

    st.header("Welcome to AtomSec GRC Tool")

    st.write("Select a Framework or Entity to Begin")

    st.subheader("Frameworks")

    f1,f2 = st.columns(2)

    with f1:
        if st.button("ISO 27001:2022"):
            st.session_state.framework="ISO"

        if st.button("GDPR"):
            st.session_state.framework="GDPR"

    with f2:
        if st.button("SOC2"):
            st.session_state.framework="SOC2"

        if st.button("CE / CE+"):
            st.session_state.framework="CE"

# ======================
# ABOUT PAGE
# ======================

if about_btn:

    st.header("About GRC Tool")

    st.write("""

This tool is designed for AtomSec internal compliance management.

It helps manage:

• ISO 27001  
• SOC2  
• GDPR  
• CE / CE+

The tool tracks:

• Controls  
• Evidence  
• Policies  
• Compliance Status

""")

    st.write("Contact: aditi-grc@gmail.com")


# ======================
# CONTACT PAGE
# ======================

if contact_btn:

    st.header("Contact")

    st.write("""

For support contact:

aditi-grc@gmail.com

""")


# ======================
# FRAMEWORK PAGE
# ======================

framework = None

if "framework" in st.session_state:
    framework = st.session_state.framework

if page != "Home":
    framework = page

if framework:

    st.header(framework + " Framework")

    # Example status
    status = st.selectbox(
        "Framework Status",
        ["Not Started","In Progress","Completed"]
    )

    st.divider()

    # PAGE 4 LOGIC
    if status == "Not Started":

        st.warning("Framework not started")

        st.write("Suggested first steps:")

        st.write("""

1 Define Scope  
2 Identify Assets  
3 Perform Risk Assessment  
4 Define Policies

""")

    elif status == "In Progress":

        st.info("Framework in Progress")

        st.subheader("Checklist")

        st.write("""

Define Scope

Risk Assessment

Policies

Internal Audit

Management Review

""")


        st.subheader("Evidence Required")

        st.write("""

Risk Assessment Report

Policies

Training Records

Audit Logs

""")


    elif status == "Completed":

        st.success("Framework Completed")

        st.subheader("Dashboard Overview")

        c1,c2,c3 = st.columns(3)

        c1.metric("Controls","82")
        c2.metric("Policies","18")
        c3.metric("Evidence","143")
