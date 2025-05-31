# Loop to ensure valid priority input
while True:
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Validate priority input
    if priority not in ['high', 'medium', 'low']:
        print("Please enter a valid priority: high, medium, or low.")
        continue

    # Validate time-bound input
    if time_bound not in ['yes', 'no']:
        print("Please enter 'yes' or 'no' for time-bound.")
        continue

    break  # Exit loop if all inputs are valid

# Match-case based on priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' is a task with unspecified priority"

# Add time-sensitivity note
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Output the reminder
print(f"\nReminder: {reminder}")
