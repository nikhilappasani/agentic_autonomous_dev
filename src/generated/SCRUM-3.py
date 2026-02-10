import datetime

def get_greeting_message() -> str:
    """
    Constructs a greeting message that includes today's date.

    Returns:
        str: A greeting message with today's date.
    """
    today_date = datetime.date.today()
    greeting_message = f"Hello, how are you today? Today's date is {today_date}."
    return greeting_message

def main() -> None:
    """
    Main function to execute the script.
    Prints the greeting message to the console.
    """
    try:
        message = get_greeting_message()
        print(message)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()