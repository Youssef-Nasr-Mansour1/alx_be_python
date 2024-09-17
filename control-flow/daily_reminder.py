# daily_reminder.py

def main():
    # Prompt for a Single Task
    task = input("Enter your task: ").strip()
    
    # Ensure priority input is valid
    while True:
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority in ("high", "medium", "low"):
            break
        print("Invalid input. Please enter 'high', 'medium', or 'low'.")
    
    # Ensure time_bound input is valid
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
        if time_bound in ("yes", "no"):
            break
        print("Invalid input. Please enter 'yes' or 'no'.")
    
    # Process the Task Based on Priority and Time Sensitivity
    match priority:
        case "high":
            priority_message = "high priority task"
        case "medium":
            priority_message = "medium priority task"
        case "low":
            priority_message = "low priority task"
        case _:
            priority_message = "task with unknown priority"  # Shouldn't occur due to validation

    # Provide a Customized Reminder
    if time_bound == "yes":
        reminder_message = f"Reminder: '{task}' is a {priority_message} that requires immediate attention today!"
    else:
        reminder_message = f"Note: '{task}' is a {priority_message}. Consider completing it when you have free time."

    print(reminder_message)

if __name__ == "__main__":
    main()
