import datetime

def get_today_date() -> str:
    """
    Retrieves today's date and returns it as a string.

    Returns:
        str: Today's date in the format YYYY-MM-DD.
    """
    return str(datetime.date.today())

def print_greeting() -> None:
    """
    Prints a greeting message that includes today's date.
    """
    try:
        today = get_today_date()
        print(f"Hello, how are you today? Today's date is {today}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print_greeting()