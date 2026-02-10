from datetime import date

def get_greeting_message() -> str:
    """
    Constructs a greeting message that includes today's date.

    Returns:
        str: A greeting message with today's date formatted as 'Month Day, Year'.
    """
    today = date.today()
    greeting_message = f"Hello, how are you today? Today's date is {today.strftime('%B %d, %Y')}."
    return greeting_message

def main() -> None:
    """
    Main function to print the greeting message.
    """
    message = get_greeting_message()
    print(message)

if __name__ == "__main__":
    main()