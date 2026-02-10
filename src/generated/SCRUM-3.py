from datetime import datetime

def get_today_date() -> None:
    """
    Retrieves the current date and prints a greeting message with today's date.
    """
    try:
        # Get today's date
        today_date = datetime.now().date()
        
        # Print the greeting message with today's date
        print(f"Hello, How are you today? Today's date is {today_date}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_today_date()