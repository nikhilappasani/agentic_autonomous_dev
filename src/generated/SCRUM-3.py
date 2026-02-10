from datetime import date

def get_greeting_message() -> str:
    """
    Retrieves today's date and constructs a greeting message.

    Returns:
        str: A greeting message including today's date.
    """
    today = date.today()
    formatted_date = today.strftime("%B %d, %Y")
    greeting_message = f"Hello, how are you today? Today's date is {formatted_date}."
    return greeting_message

if __name__ == "__main__":
    print(get_greeting_message())