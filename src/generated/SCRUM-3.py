from datetime import date

def get_greeting_message() -> str:
    """
    Constructs a greeting message that includes today's date.

    Returns:
        str: A greeting message with today's date.
    """
    today = date.today()
    greeting_message = f"Hello, how are you today? Today's date is {today}."
    return greeting_message

def main() -> None:
    """
    Main function to execute the script.
    Retrieves today's date and prints a greeting message.
    """
    try:
        message = get_greeting_message()
        print(message)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()