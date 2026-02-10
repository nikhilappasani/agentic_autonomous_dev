#!/usr/bin/env python3

import datetime

def print_greeting() -> None:
    """
    Prints a greeting message along with today's date.

    This function retrieves the current date using the datetime module
    and prints a message to the console.
    """
    try:
        today = datetime.date.today()
        print(f"Hello How are you today? Today's date is {today}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print_greeting()