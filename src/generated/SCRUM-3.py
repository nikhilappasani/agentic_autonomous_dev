from datetime import date

def get_greeting_message() -> str:
    """
    Constructs a greeting message that includes today's date.

    Returns:
        str: A greeting message with today's date.
    """
    today: date = date.today()
    greeting_message: str = f"Hello, how are you today? Today's date is {today}."
    return greeting_message

def main() -> None:
    """
    Main function to execute the script and print the greeting message.
    """
    message: str = get_greeting_message()
    print(message)

if __name__ == "__main__":
    main()