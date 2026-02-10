from datetime import date

def get_greeting_message() -> str:
    """
    Constructs a greeting message that includes today's date.

    Returns:
        str: A greeting message with today's date.
    """
    # Get today's date
    today = date.today()
    
    # Create a greeting message with today's date
    greeting_message = f"Hello, how are you today? Today's date is {today}."
    
    return greeting_message

def main() -> None:
    """
    Main function to execute the script.
    """
    try:
        # Get the greeting message
        message = get_greeting_message()
        
        # Print the greeting message
        print(message)
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()