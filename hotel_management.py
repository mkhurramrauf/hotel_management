class Hotel:
    def __init__(self):
        self.rooms = {101: None, 102: None, 103: None, 104: None, 105: None}

    def display_rooms(self):
        """Display room availability."""
        print("\n🏨 Room Availability:")
        for room, guest in self.rooms.items():
            status = "Available ✅" if guest is None else f"Occupied by {guest} ❌"
            print(f"Room {room}: {status}")
        print()

    def book_room(self):
        """Book a room for a guest."""
        self.display_rooms()
        try:
            room_number = int(input("Enter room number to book: "))
            if room_number in self.rooms and self.rooms[room_number] is None:
                guest_name = input("Enter guest name: ")
                self.rooms[room_number] = guest_name
                print(f"✅ Room {room_number} has been booked for {guest_name}.\n")
            else:
                print("❌ Invalid room number or room is already occupied!\n")
        except ValueError:
            print("❌ Invalid input! Please enter a valid room number.\n")

    def check_out(self):
        """Check out a guest and free up the room."""
        self.display_rooms()
        try:
            room_number = int(input("Enter room number to check out: "))
            if room_number in self.rooms and self.rooms[room_number] is not None:
                print(f"🛏️ Room {room_number} checked out. {self.rooms[room_number]} has left.\n")
                self.rooms[room_number] = None
            else:
                print("❌ Invalid room number or the room is already empty!\n")
        except ValueError:
            print("❌ Invalid input! Please enter a valid room number.\n")

    def run(self):
        """Run the Hotel Management System."""
        while True:
            print("\n🏨 Hotel Management System")
            print("1. View Available Rooms")
            print("2. Book a Room")
            print("3. Check Out")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.display_rooms()
            elif choice == '2':
                self.book_room()
            elif choice == '3':
                self.check_out()
            elif choice == '4':
                print("👋 Exiting Hotel Management System. Have a nice day!\n")
                break
            else:
                print("❌ Invalid choice! Please enter a number between 1 and 4.\n")

if __name__ == "__main__":
    hotel = Hotel()
    hotel.run()
