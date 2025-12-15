import streamlit as st
import wikipediaapi

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="BestInfo",
    page_icon="📘",
    layout="wide"
)

# ---------------- Header ----------------
st.title("📘 BestInfo")
st.caption("Your smart knowledge companion")

st.markdown(
    """
    Search and explore **detailed, Wikipedia-like information**
    about people, science, technology, and general knowledge topics.
    """
)

st.divider()

# ---------------- Search Section (MAIN PAGE) ----------------
col1, col2 = st.columns([4, 1])

with col1:
    topic = st.text_input(
        "Enter a topic",
        placeholder="e.g., Tom Cruise, Bacteria, Artificial Intelligence"
    )

with col2:
    search_clicked = st.button("🔍 Search")

st.divider()

# ---------------- Wikipedia API ----------------
wiki = wikipediaapi.Wikipedia(
    user_agent="BestInfo/1.0 (educational project)",
    language="en",
    extract_format=wikipediaapi.ExtractFormat.WIKI
)

# ---------------- Results Section ----------------
if search_clicked:
    if topic.strip() == "":
        st.warning("Please enter a topic to search.")
    else:
        page = wiki.page(topic)

        if not page.exists():
            st.error("No information found for this topic.")
        else:
            # Title
            st.subheader(page.title)

            # Summary
            st.markdown("### 📌 Summary")
            st.write(page.summary)

            # Full Details
            with st.expander("📖 Read full detailed information"):
                st.write(page.text)

# ---------------- Footer ----------------
st.divider()
st.caption(
    "BestInfo uses Wikipedia’s official API to provide reliable and ethical information access."
)
