import datetime

def get_todays_date() -> str:
    """
    Retrieves today's date and returns a greeting message.

    Returns:
        str: A greeting message with today's date.
    """
    try:
        today_date = datetime.date.today()
        return f"Hello, how are you today? Today's date is {today_date}."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Execute the function and print the result
    print(get_todays_date())