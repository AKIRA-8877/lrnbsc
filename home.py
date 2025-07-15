class HomeAutomation:
    def __init__(self):
        self.devices = {
            "Lights": False,
            "Fan": False,
            "Door Lock": True  # True means locked
        }

    def show_status(self):
        print("\n--- Device Status ---")
        for device, status in self.devices.items():
            if device == "Door Lock":
                print(f"{device}: {'Locked' if status else 'Unlocked'}")
            else:
                print(f"{device}: {'On' if status else 'Off'}")

    def toggle_device(self, device_name):
        if device_name in self.devices:
            self.devices[device_name] = not self.devices[device_name]
            state = "On" if self.devices[device_name] else "Off"
            if device_name == "Door Lock":
                state = "Locked" if self.devices[device_name] else "Unlocked"
            print(f"{device_name} is now {state}")
        else:
            print("Device not found.")

    def display_menu(self):
        print("\n🏠 Home Automation System")
        print("1. Toggle Lights")
        print("2. Toggle Fan")
        print("3. Lock/Unlock Door")
        print("4. Show Status")
        print("5. Exit")

def run_home_automation():
    system = HomeAutomation()
    while True:
        system.display_menu()
        choice = input("Select an option: ")

        if choice == '1':
            system.toggle_device("Lights")
        elif choice == '2':
            system.toggle_device("Fan")
        elif choice == '3':
            system.toggle_device("Door Lock")
        elif choice == '4':
            system.show_status()
        elif choice == '5':
            print("Exiting Home Automation System. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

run_home_automation()