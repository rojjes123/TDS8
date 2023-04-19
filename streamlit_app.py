# TDS8
import streamlit as st

def find_largest(num1, num2, num3):
    """
    Find The Largest
    """
    ""
    put uour numbers
    ""
    
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def main():
    """
    This function defines the Streamlit app UI and logic.
    """
    st.title("Find the largest ")
    st.title('Enter three numbers and find the largest among them.')
    num1 = st.number_input("Enter the first  number", value=0, step=1)
    num2 = st.number_input("Enter the second  number", value=0, step=1)
    num3 = st.number_input("Enter the third  number", value=0, step=1)

    if st.button("Find the largest"):
        largest_num = find_largest(num1, num2, num3)
        st.success(f"The largest number is {largest_num}")

if __name__ == "__main__":
    main()


    
