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
    Constructs and prints a greeting message that includes today's date.
    """
    try:
        today_date = get_today_date()
        greeting_message = f"Hello, how are you today? Today's date is {today_date}."
        print(greeting_message)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print_greeting()