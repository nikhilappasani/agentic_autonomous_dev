import datetime

def get_todays_date() -> datetime.date:
    """
    Retrieves today's date.

    Returns:
        datetime.date: The current date.
    """
    return datetime.date.today()

def print_greeting() -> None:
    """
    Prints a greeting message to the console.
    """
    print("Hello, how are you today?")

if __name__ == "__main__":
    today = get_todays_date()
    print_greeting()
    print(f"Today's date is: {today}")