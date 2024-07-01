import streamlit as st
import langchain_helper as lh
st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine",("Indian", "Italian", "Mexican", "Arabic", "American", "French"))


if cuisine:
    response = lh.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(',')
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)

if __name__ == "__main__":
    print(lh.generate_restaurant_name_and_items("Arabic"))
