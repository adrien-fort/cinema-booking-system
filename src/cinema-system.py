from logger import log_info
from verify_cinema_hall import verify_cinema_hall

def main():
    print("Welcome to cinema booking system")
    user_input = input("Enter hall-name, hall-height, hall-length (comma separated): ")
    log_info(f"User input: {user_input}")
    try:
        hall_name, hall_height, hall_length = [x.strip() for x in user_input.split(",")]
        hall_height = int(hall_height)
        hall_length = int(hall_length)
        print(f"Input received: hall_name={hall_name}, hall_height={hall_height}, hall_length={hall_length}")
        result = verify_cinema_hall(hall_name, hall_height, hall_length)
        print(f"Verification result: {result}")
    except Exception as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
