from datetime import date

def get_todays_date() -> str:
    """
    Retrieves today's date and returns it as a formatted string.

    Returns:
        str: Today's date formatted as "Month Day, Year".
    """
    today = date.today()
    formatted_date = today.strftime("%B %d, %Y")
    return formatted_date

def print_greeting_with_date() -> None:
    """
    Prints a greeting message that includes today's date.
    """
    formatted_date = get_todays_date()
    message = f"Hello, how are you today? Today's date is {formatted_date}."
    print(message)

if __name__ == "__main__":
    print_greeting_with_date()