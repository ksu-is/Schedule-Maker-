class Schedule:
    def __init__(self):
        self.events = {}

    def add_event(self, time, event):
        if time not in self.events:
            self.events[time] = []
        self.events[time].append(event)
        print(f"Event '{event}' added at {time}.")

    def view_schedule(self):
        if not self.events:
            print("No events scheduled.")
        else:
            print("Scheduled Events:")
            for time, events in sorted(self.events.items()):
                for event in events:
                    print(f"{time}: {event}")

    def delete_event(self, time, event):
        if time in self.events and event in self.events[time]:
            self.events[time].remove(event)
            print(f"Event '{event}' deleted at {time}.")
            if not self.events[time]:
                del self.events[time]
        else:
            print(f"Event '{event}' not found at {time}.")

def main():
    schedule = Schedule()

    while True:
        print("\nOptions:")
        print("1. Add Event")
        print("2. View Schedule")
        print("3. Delete Event")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            time = input("Enter time for the event: ")
            event = input("Enter the event: ")
            schedule.add_event(time, event)
        elif choice == "2":
            schedule.view_schedule()
        elif choice == "3":
            time = input("Enter time for the event: ")
            event = input("Enter the event: ")
            schedule.delete_event(time, event)
        elif choice == "4":
            print("Exiting the schedule program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()