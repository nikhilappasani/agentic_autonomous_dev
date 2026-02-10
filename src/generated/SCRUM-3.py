from datetime import date

def get_greeting() -> str:
    """
    Retrieves today's date and returns a greeting message.

    Returns:
        str: A greeting message including today's date.
    """
    today = date.today()
    formatted_date = today.strftime("%B %d, %Y")
    return f"Hello, how are you today? Today's date is {formatted_date}."

if __name__ == "__main__":
    # Print the greeting message
    print(get_greeting())