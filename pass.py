import streamlit as st
import re

# Page Configuration
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

# Title and Introduction
st.title("💪🔐 Password Strength Checker")
st.markdown("""
### Welcome to the Ultimate Password Strength Checker! 👋
Use this simple tool to check the strength of your password and get suggestions on how to make it stronger.
We will provide helpful tips to create a **strong and secure password** 🔐
""")

# User Input
password = st.text_input("Enter Your Password", type="password")

# Initialize feedback list and score
feedback = []
score = 0

if password:
    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Check uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase letters.")
    
    # Check digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")
    
    # Check special characters
    if re.search(r'[!@#$%&]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (!@#$%&).")
    
    # Display password strength
    if score == 4:
        st.success("✅ Your password is strong! 🎉")
    elif score == 3:
        st.warning("🟡 Your password is medium strength. Consider making it stronger.")
    else:
        st.error("🔴 Your password is weak. Please improve it.")
    
    # Show improvement suggestions if any
    if feedback:
        st.markdown("### 🔧 Improvement Suggestions")
        for tip in feedback:
            st.write(tip)
else:
    st.info("🔍 Please enter a password to check its strength.")
