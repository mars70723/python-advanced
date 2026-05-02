import streamlit

def main():
    streamlit.title("Hello World")
    streamlit.button("Click Here")
    if streamlit.button("Click Me"):
        streamlit.write("Button Clicked")
    if streamlit.checkbox("Click"):
        streamlit.write("The checkbox was clicked")
    user_input = streamlit.text_input("Enter Text", "Sample")
    streamlit.write("You wrote: ", user_input)
    age = streamlit.number_input("Enter your age", min_value=0, max_value=100)
    streamlit.write(f"Your age is: {age}")




if __name__ == '__main__':
    main()