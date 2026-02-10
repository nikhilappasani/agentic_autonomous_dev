from datetime import datetime

def get_today_date() -> None:
    """
    Retrieves today's date and prints a greeting message with the date.

    This function uses the datetime module to get the current date and
    prints a message including the date.

    Returns:
        None
    """
    today_date = datetime.now().date()
    print(f"Hello, How are you today? Today's date is {today_date}.")

# Execute the function
get_today_date()