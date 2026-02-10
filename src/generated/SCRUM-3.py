import datetime

def get_todays_date() -> str:
    """
    Retrieves today's date in YYYY-MM-DD format.

    Returns:
        str: Today's date as a string.
    """
    today = datetime.date.today()
    return str(today)

def print_greeting() -> None:
    """
    Prints a greeting message that includes today's date.
    """
    today_date = get_todays_date()
    print(f"Hello, how are you today? Today's date is {today_date}.")

if __name__ == "__main__":
    print_greeting()