from datetime import date

def get_todays_date() -> str:
    """
    Retrieves today's date and returns a formatted greeting message.

    Returns:
        str: A greeting message with today's date.
    """
    try:
        today = date.today()
        return f"Hello, how are you today? Today's date is {today}."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Print the greeting message with today's date
    print(get_todays_date())