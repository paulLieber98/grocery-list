import streamlit as st

# Initialize the grocery list
if 'grocery_list' not in st.session_state:
    st.session_state.grocery_list = []

# Function to display the grocery list
def display():
    st.write("This is your grocery list so far:")
    if st.session_state.grocery_list:
        for item in st.session_state.grocery_list:
            st.write(f"- {item}")
    else:
        st.write("Your list is empty.")

# Function to add an item to the grocery list
def add(item):
    if item:
        st.session_state.grocery_list.append(item)
        st.success(f"'{item}' has been added to the list.")

# Function to remove an item from the grocery list
def remove(item):
    if item in st.session_state.grocery_list:
        st.session_state.grocery_list.remove(item)
        st.success(f"'{item}' has been removed from the list.")
    else:
        st.error(f"'{item}' is not in the list.")

# Streamlit UI
st.title("Grocery List Manager")

st.subheader("Add or Remove Items")

# Add an item to the grocery list
add_item = st.text_input("Enter an item to add", key="add_item")
if st.button("Add Item"):
    add(add_item)
    display()

# Remove an item from the grocery list
remove_item = st.text_input("Enter an item to remove", key="remove_item")
if st.button("Remove Item"):
    remove(remove_item)
    display()

# Display the grocery list
st.subheader("Current Grocery List")
display()

# Option to clear the entire list
if st.button("Clear List"):
    st.session_state.grocery_list.clear()
    st.success("The grocery list has been cleared.")
    display()
