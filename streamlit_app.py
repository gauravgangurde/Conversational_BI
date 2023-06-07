import streamlit as st

def main():
    tabs = ["Tab 1", "Tab 2", "Tab 3"]
    current_tab = st.sidebar.radio("Select a tab", tabs)
    
    if current_tab == "Tab 1":
        tab1()
    elif current_tab == "Tab 2":
        tab2()
    elif current_tab == "Tab 3":
        tab3()

def tab1():
    st.title("Tab 1")
    st.write("Content for Tab 1")
    next_tab_button("Tab 2")

def tab2():
    st.title("Tab 2")
    st.write("Content for Tab 2")
    next_tab_button("Tab 3")

def tab3():
    st.title("Tab 3")
    st.write("Content for Tab 3")
    next_tab_button("Tab 1")

def next_tab_button(next_tab):
    col1, col2, col3 = st.beta_columns(3)
    col2.button("Next Tab", key=next_tab)

if __name__ == "__main__":
    main()
