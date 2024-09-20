task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        message = (f"Your task {task} is High priority")
    case "medium":
        message = (f"Your task {task} is medium periority")
    case "low":
        message = (f"Your task {task} is low periority")
if time_bound != "yes":
    print (message)
else:
    print(message)
    print("This is a time-sensitive task that requires immediate attention today!")