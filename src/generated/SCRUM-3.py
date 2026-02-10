import datetime

def get_today_date() -> str:
    """
    Retrieve today's date and return a greeting message.

    Returns:
        str: A greeting message with today's date.
    """
    today_date = datetime.date.today()
    return f"Hello, How are you today? Today's date is {today_date}."

if __name__ == "__main__":
    # Print the greeting message with today's date
    print(get_today_date())