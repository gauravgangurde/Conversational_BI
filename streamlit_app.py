import streamlit as st

# Create the tab objects
tab1, tab2, tab3 = st.columns(3)

# Define a button to switch to the next tab
if tab1.button("Next Tab"):
    tab1.empty()
    tab2.write("This is the content of Tab 2.")
elif tab2.button("Next Tab"):
    tab2.empty()
    tab3.write("This is the content of Tab 3.")
elif tab3.button("Next Tab"):
    tab3.empty()
    tab1.write("This is the content of Tab 1.")
else:
    tab1.write("This is the content of Tab 1.")
