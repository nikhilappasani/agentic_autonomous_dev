from datetime import date

def get_greeting_message() -> str:
    """
    Retrieves today's date and constructs a greeting message.

    Returns:
        str: A greeting message including today's date.
    """
    try:
        # Get today's date
        today: date = date.today()
        
        # Create a greeting message with today's date
        greeting_message: str = f"Hello, how are you today? Today's date is {today}."
        
        return greeting_message
    except Exception as e:
        return f"An error occurred: {e}"

def main() -> None:
    """
    Main function to execute the script and print the greeting message.
    """
    # Print the greeting message
    print(get_greeting_message())

if __name__ == "__main__":
    main()