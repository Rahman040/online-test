import streamlit as st

def tipcal():
    st.title("Welcome to the Tip calculator")

    bill = st.number_input("Enter the total bill amount: ", step=0.5, max_value=10000.0, min_value=0.0)
    percent = st.number_input("Percent of tip you want to give (10,15,20): ", step=5, max_value=20, min_value=10)
    members = st.number_input("Number of members: ", step=1, min_value=1)

    if st.button("Calculate"):
        tip = (percent / 100) * bill
        amount = tip + bill
        split = amount / members
        st.write(f"Tip amount is: {tip:.2f}")
        st.write(f"The Total Amount is: {amount:.2f}")
        st.write(f"Each member has to pay: {split:.2f}")

tipcal()
