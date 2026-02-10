from datetime import date

def get_greeting() -> str:
    """
    Retrieves today's date and returns a greeting message.

    Returns:
        str: A greeting message with today's date.
    """
    today = date.today()
    return f"Hello, how are you today? Today's date is {today}."

def main() -> None:
    """
    Main function to execute the script.
    """
    try:
        greeting_message = get_greeting()
        print(greeting_message)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()