from datetime import datetime

def get_today_date() -> None:
    """
    Retrieves the current date and prints a greeting message.

    This function uses the datetime module to get the current date
    and prints a message including today's date.
    """
    try:
        today_date = datetime.now().date()
        print(f"Hello, How are you today? Today's date is {today_date}.")
    except ImportError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_today_date()