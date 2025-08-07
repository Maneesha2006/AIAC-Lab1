def calculate_power_bill():
    print("Power Bill Calculator")
    house_number = input("Enter house number: ")
    try:
        prev_reading = float(input("Enter previous month meter reading (in units): "))
        curr_reading = float(input("Enter present month meter reading (in units): "))
        if curr_reading < prev_reading:
            print("Error: Present month reading cannot be less than previous month reading.")
            return
    except ValueError:
        print("Invalid input. Please enter numeric values for meter readings.")
        return

    print("Select consumer type:")
    print("1. Domestic")
    print("2. Industry")
    consumer_type = input("Enter 1 for Domestic or 2 for Industry: ").strip()

    units_consumed = curr_reading - prev_reading

    if consumer_type == '1':
        # Domestic rates (example slab)
        if units_consumed <= 100:
            rate = 3.0
        elif units_consumed <= 200:
            rate = 4.5
        elif units_consumed <= 500:
            rate = 6.0
        else:
            rate = 8.0
        consumer_str = "Domestic"
    elif consumer_type == '2':
        # Industry rates (example slab)
        if units_consumed <= 200:
            rate = 5.0
        elif units_consumed <= 500:
            rate = 7.0
        else:
            rate = 10.0
        consumer_str = "Industry"
    else:
        print("Invalid consumer type selected.")
        return

    bill_amount = units_consumed * rate

    print("\n--- Power Bill Details ---")
    print(f"House Number: {house_number}")
    print(f"Consumer Type: {consumer_str}")
    print(f"Previous Month Reading: {prev_reading} units")
    print(f"Present Month Reading: {curr_reading} units")
    print(f"Units Consumed: {units_consumed} units")
    print(f"Rate per Unit: ₹{rate}")
    print(f"Total Bill Amount: ₹{bill_amount:.2f}")

if __name__ == "__main__":
    calculate_power_bill()
