import datetime

def get_today_date() -> str:
    """
    Retrieves today's date in a formatted string.

    Returns:
        str: Today's date formatted as 'Month Day, Year'.
    """
    today_date = datetime.date.today()
    return today_date.strftime('%B %d, %Y')

def print_greeting() -> None:
    """
    Prints a greeting message along with today's date.
    """
    greeting_message = "Hello, How are you today?"
    today_date = get_today_date()
    print(greeting_message)
    print(f"Today's date is: {today_date}")

if __name__ == "__main__":
    print_greeting()