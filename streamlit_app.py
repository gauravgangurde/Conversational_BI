import streamlit as st

# Create the tab objects
tab1, tab2, tab3 = st.tabs(['Analysis','Report', 'Validation'])

# Define a button to switch to the next tab
if tab1.button("Next Tab", key = 'a'):
    tab1.empty()
    tab2.write("This is the content of Tab 2.")
elif tab2.button("Next Tab", key = 'b'):
    tab2.empty()
    tab3.write("This is the content of Tab 3.")
elif tab3.button("Next Tab", key = 'c'):
    tab3.empty()
    tab1.write("This is the content of Tab 1.")
else:
    tab1.write("This is the content of Tab 1.")
