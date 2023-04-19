# TDS8
import streamlit as st

def largest_number (a, b, c):
    """
    Returns the largest number among three given numbers
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def main():
    """
    Defines the Streamlit app
    """
    st.title("Find the largest among 3 given numbers")

    # Get user input
    a = st.number_input("Enter the first number:")
    b = st.number_input("Enter the second number:")
    c = st.number_input("Enter the third number:")

    # Call the function to get the largest number
    largest = largest_number (int(a), int(b), int(c))

    if st.button('Find Largest'):
        

    # Display the result
         st.write("The largest number is:", largest)

if __name__ == '__main__':
    main()
