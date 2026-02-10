from datetime import date

def get_greeting_with_date() -> str:
    """
    Retrieves today's date and returns a greeting message.

    Returns:
        str: A greeting message including today's date.
    """
    try:
        # Get today's date
        today: date = date.today()
        # Construct the greeting message
        greeting_message: str = f"Hello, how are you today? Today's date is {today}."
        return greeting_message
    except Exception as e:
        # Handle any unexpected errors
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Print the greeting message with today's date
    print(get_greeting_with_date())