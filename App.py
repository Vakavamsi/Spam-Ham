import streamlit as st
import pickle
from preprocessing import clean   # use your existing clean() function

# Page config
st.set_page_config(
    page_title="Spam Email Classifier",
    page_icon="📧",
    layout="centered"
)

# Title
st.title("📧 Spam Email Classifier")
st.write("Enter an email message to check whether it is **Spam** or **Ham (Not Spam)**.")

# Load trained model
@st.cache_resource
def load_model():
    with open("spam_email_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# Text input
email_text = st.text_area(
    "✉️ Email Text",
    height=180,
    placeholder="Paste the email content here..."
)

# Predict button
if st.button("🔍 Predict"):
    if email_text.strip() == "":
        st.warning("⚠️ Please enter some email text")
    else:
        cleaned_text = clean(email_text)
        prediction = model.predict([cleaned_text])[0]

        if prediction.lower() == "spam":
            st.error("🚨 This email is **SPAM**")
        else:
            st.success("✅ This email is **HAM (Not Spam)**")

        # Optional: show cleaned text
        with st.expander("🔎 View cleaned text"):
            st.write(cleaned_text)

# Sidebar info
st.sidebar.header("ℹ️ About")
st.sidebar.write("""
- **Model**: Naive Bayes  
- **Vectorizer**: TF-IDF  
- **Use Case**: Spam Email Detection  
- **Built with**: Python & Streamlit
""")
