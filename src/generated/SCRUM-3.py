from datetime import datetime

def get_today_date() -> str:
    """
    Retrieves today's date in YYYY-MM-DD format.

    Returns:
        str: Today's date as a string.
    """
    return datetime.today().date().isoformat()

def print_greeting() -> None:
    """
    Prints a greeting message with today's date.
    """
    today_date = get_today_date()
    print(f"Hello, how are you today? Today's date is {today_date}.")

if __name__ == "__main__":
    print_greeting()