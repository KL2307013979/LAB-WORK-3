#Name: Muhamad Azfar Bin Mohamad Fauzi
#ID Student: AM2307013979
#Assignment: LAB WORK 3
def display_room_types(room_types, nightly_rates):
    print("Available Room Types:")
    for i, room_type in enumerate(room_types, 1):
        print(f"{i}. {room_type} - RM {nightly_rates[i-1]:.2f} per night")

def calculate_total_cost(room_type_index, num_rooms, nightly_rates, check_in_date, check_out_date):
    if 1 <= room_type_index <= len(nightly_rates):
        nightly_rate = nightly_rates[room_type_index - 1]
        duration_of_stay = (check_out_date - check_in_date).days
        return nightly_rate * num_rooms * duration_of_stay
    else:
        return None

def get_date_input(prompt):
    while True:
        date_str = input(prompt)
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def main():
    print("---------------------------------------------")
    print(" Welcome to Our ABC Hotel Reservation System ")
    print("---------------------------------------------")

    # User Input
    room_types = ["Single", "Double", "Suite"]
    nightly_rates = [100, 150, 250]

    display_room_types(room_types, nightly_rates)

    room_type_index = int(input("\nPlease select a room type (1/2/3): "))
    num_rooms = int(input("Enter the number of rooms: "))
    check_in_date = get_date_input("Enter your check-in date (YYYY-MM-DD): ")
    check_out_date = get_date_input("Enter your check-out date (YYYY-MM-DD): ")

    # Calculate Total Cost
    total_cost = calculate_total_cost(room_type_index, num_rooms, nightly_rates, check_in_date, check_out_date)

    if total_cost is not None:
        # Additional Services
        services = {"breakfast": 20, "wifi": 10, "parking": 15}
        print("\nAdditional Services:")
        print("1. Breakfast - RM20")
        print("2. WiFi      - RM10")
        print("3. Breakfast - RM15")
        additional_services_cost = sum(services[service] for service in services if input(f"Would you like to add any additional services {service.capitalize()}? (yes/no): ").lower() == 'yes')
        print("\nThank you for your reservation.")

        # Display Reservation Details
        print("\nReservation Details:")
        print(f"Room Type: {room_types[room_type_index - 1]}")
        print(f"Number of Rooms: {num_rooms}")
        print(f"Check-in Date: {check_in_date.strftime('%Y-%m-%d')}")
        print(f"Check-out Date: {check_out_date.strftime('%Y-%m-%d')}")
        print(f"Room Cost: RM {total_cost:.2f}")
        print(f"Additional Services Cost: RM {additional_services_cost:.2f}")
        print(f"Total Cost: RM{total_cost + additional_services_cost:.2f}")
        print("\nReservation confirmed. Thank you for choosing our hotel. Enjoy your stay!")
    else:
        print("Invalid room type. Please choose a valid option.")

if __name__ == "__main__":
    from datetime import datetime
    main()
