from datetime import date

def get_todays_date() -> str:
    """
    Retrieves today's date and returns it in a formatted string.

    Returns:
        str: Today's date formatted as 'Month Day, Year'.
    """
    today = date.today()
    formatted_date = today.strftime("%B %d, %Y")
    return formatted_date

def print_greeting() -> None:
    """
    Prints a greeting message along with today's date.
    """
    try:
        formatted_date = get_todays_date()
        print(f"Hello, how are you today? Today's date is {formatted_date}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print_greeting()