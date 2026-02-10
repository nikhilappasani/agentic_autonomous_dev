from datetime import date

def get_greeting_with_date() -> str:
    """
    Retrieves today's date and returns a greeting message.

    Returns:
        str: A greeting message with today's date.
    """
    today = date.today()
    formatted_date = today.strftime("%B %d, %Y")
    return f"Hello, how are you today? Today's date is {formatted_date}."

if __name__ == "__main__":
    # Print the greeting message with today's date
    print(get_greeting_with_date())