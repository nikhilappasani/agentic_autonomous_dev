from datetime import date

def get_greeting_message() -> str:
    """
    Retrieves today's date and constructs a greeting message.

    Returns:
        str: A greeting message including today's date.
    """
    # Get today's date
    today: date = date.today()

    # Create a greeting message
    greeting_message: str = f"Hello, how are you today? Today's date is {today}."

    return greeting_message

def main() -> None:
    """
    Main function to execute the script and print the greeting message.
    """
    try:
        # Get the greeting message
        message: str = get_greeting_message()

        # Print the greeting message
        print(message)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()