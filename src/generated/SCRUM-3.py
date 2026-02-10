import datetime

def get_today_date() -> str:
    """
    Retrieve today's date.

    Returns:
        str: Today's date in YYYY-MM-DD format.
    """
    return datetime.date.today().isoformat()

def print_greeting() -> None:
    """
    Print a greeting message with today's date.
    """
    today_date = get_today_date()
    print(f"Hello, how are you today? Today's date is {today_date}.")

if __name__ == "__main__":
    try:
        print_greeting()
    except Exception as e:
        print(f"An error occurred: {e}")