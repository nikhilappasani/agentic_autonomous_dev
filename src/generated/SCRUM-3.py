from datetime import date

def get_greeting_with_date() -> str:
    """
    Retrieves today's date and returns a greeting message.

    Returns:
        str: A greeting message including today's date.
    """
    try:
        # Get today's date
        today = date.today()
        
        # Format the date as "Month Day, Year"
        formatted_date = today.strftime("%B %d, %Y")
        
        # Construct the greeting message
        message = f"Hello, how are you today? Today's date is {formatted_date}."
        
        return message
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Print the greeting message
    print(get_greeting_with_date())