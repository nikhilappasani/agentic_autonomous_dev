import datetime

def get_today_date() -> str:
    """
    Retrieves today's date and returns it as a string.

    Returns:
        str: Today's date in YYYY-MM-DD format.
    """
    today_date = datetime.date.today()
    return str(today_date)

def print_greeting() -> None:
    """
    Prints a greeting message along with today's date.
    """
    today_date = get_today_date()
    print(f"Hello, How are you today? Today's date is {today_date}.")

if __name__ == "__main__":
    try:
        print_greeting()
    except Exception as e:
        print(f"An error occurred: {e}")