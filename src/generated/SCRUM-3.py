import datetime

def get_today_date() -> str:
    """
    Retrieves today's date and returns a greeting message.

    Returns:
        str: A greeting message with today's date.
    """
    try:
        today_date = datetime.date.today()
        greeting_message = f"Hello, how are you today? Today's date is {today_date}."
        return greeting_message
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Print the greeting message with today's date
    print(get_today_date())