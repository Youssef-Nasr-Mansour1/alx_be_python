task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        reminder = (f"Your task {task} is High priority")
    case "medium":
        reminder = (f"Your task {task} is medium periority")
    case "low":
        reminder = (f"Your task {task} is low periority")
if time_bound = "yes":
    print (reminder)
    print("This is a time-sensitive task that requires immediate attention today!")
else:
    print(reminder)
    