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
    message = streamlit.text_area("Enter a message")
    streamlit.write(f"Your message: {message}")
    choice = streamlit.radio("Pick one", ["Choice 1", "Choice 2", "Choice 3"])
    streamlit.write(f"You chose: {choice}")
    if streamlit.button("Success"):
        streamlit.success("Operation was successful")
    try:
        1/0
    except Exception as e:
        streamlit.exception(e)



if __name__ == '__main__':
    main()