import datetime

def get_today_date() -> str:
    """
    Retrieves today's date and returns it as a string.

    Returns:
        str: A string representation of today's date in the format YYYY-MM-DD.
    """
    today_date = datetime.date.today()
    return str(today_date)

def print_greeting() -> None:
    """
    Prints a greeting message that includes today's date.
    """
    today_date = get_today_date()
    print(f"Hello, how are you today? Today's date is {today_date}.")

if __name__ == "__main__":
    try:
        print_greeting()
    except Exception as e:
        print(f"An error occurred: {e}")