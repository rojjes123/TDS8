# TDS8
import streamlit as st

def largest_number(a, b, c):
    """
    Returns the largest number among three given numbers
    """
    if int(a) >= int(b) and int(a) >= int(c):
        return int(a)
    elif int(b) >= int(a) and int(b) >= int(c):
        return int(b)
    else:
        return int(c)

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
    largest = largest_number int(a, b, c)

    if st.button('Find Largest'):
        

    # Display the result
         st.write("The largest number is:", largest)

if __name__ == '__main__':
    main()
