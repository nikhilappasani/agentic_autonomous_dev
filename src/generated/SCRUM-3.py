from datetime import date

def print_greeting() -> None:
    """
    Prints a greeting message along with today's date.

    This function retrieves the current date using the `datetime` module
    and prints a formatted greeting message to the console.
    """
    try:
        today = date.today()
        print(f"Hello, how are you today? Today's date is {today}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print_greeting()