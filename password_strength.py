import random
import streamlit as st
import re
import string

if "password_history" not in st.session_state:
   st.session_state.password_history = []

st.title("🔐 Password Generator and Strength Checker")

score = 0
Improvements: list[str] = []

# Password Strength Checking Function
def pass_check(password):
    """Check your password strong or not and give suggestions"""
    global score
    score = 0
    Improvements.clear()

    if len(password) >= 8:
        score += 1
    else:
        Improvements.append("⚠️ Your password is too short! Use at least 8 characters for better security.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        Improvements.append("🔠 Add at least one uppercase letter (A-Z) to strengthen your password.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        Improvements.append("🔡 Add at least one lowercase letter (a-z) to strengthen your password.")

    if re.search(r"[@#$%!]", password):
        score += 1
    else:
        Improvements.append("🔐 Add at least one special character (@, #, $, %, !) to make your password stronger.")  

    if re.search(r"[0-9]", password):
        score += 1
    else:
        Improvements.append("🔢 Add at least one number (0-9) to make your password stronger.")

# Password Generator Function
def pass_generator(length, use_digits, use_special):
    """generate a unique and strong password as per user requirements"""
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation

    pasword = "".join(random.choice(characters) for _ in range(length))

    st.session_state.password_history.append(pasword)

    return pasword

# Password Strength Checker UI
st.subheader("🔍 Password Strength Checker")
user_input_password = st.text_input("Enter your password", type="password")

if st.button("Check your password status"):
    pass_check(user_input_password)
    st.write(f"Your score is {score} out of 5")

    if score == 5:
        st.success("✅ Your password is strong!")
    else:
        for tip in Improvements:
            st.warning(tip)

st.write('-' * 100)

# Password Generator UI
st.subheader("🔑 Generate Your Own Password")
pass_length = st.slider("Select your password length", min_value=6, max_value=20, value=6)
pass_digits = st.checkbox("Include digits")
pass_special = st.checkbox("Include special characters")

if st.button("Generate password"):
    st.write(f"🔒 Generated password: `{pass_generator(pass_length,pass_digits,pass_special)}`")

st.divider()

st.subheader("📜 Password History")
if st.session_state.password_history :
    for idx, pasword in enumerate (st.session_state.password_history):
        col1,col2 = st.columns([3,1])
        col1.text(pasword)
        if col2.button("❌ Delete", key=f"del_{idx}") :
            st.session_state.password_history.pop(idx)
            st.rerun()
    
    if st.button("🗑️ Clear History"):
        st.session_state.password_history.clear()
        st.rerun()


