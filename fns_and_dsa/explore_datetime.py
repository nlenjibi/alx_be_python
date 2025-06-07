# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    now = datetime.now()
    print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days_to_add: int):
    today = datetime.now().date()
    future = today + timedelta(days=days_to_add)
    print("Future date:", future.strftime("%Y-%m-%d"))

def main():
    display_current_datetime()
    try:
        days = int(input("Enter the number of days to add to the current date: ").strip())
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")

if __name__ == "__main__":
    main()
