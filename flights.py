import random
from datetime import datetime, timedelta


def generate_random_flight_data(num_records=8):
    global flight_number
    cities = ["Hyderabad", "Bengaluru", "Chennai", "Delhi", "Ernakulam"]
    statuses = ["On Time", "Delayed"]

    flight_data = []

    current_time = datetime.now()

    for i in range(num_records):
        from_city = random.choice(cities)
        to_city = random.choice(cities)
        flight_number = f"{from_city[:2]}{to_city[1]}-{i + 1}"
        # Ensure that "From" and "To" cities are distinct
        while from_city == to_city:
            to_city = random.choice(cities)

        eta = current_time + timedelta(minutes=random.randint(30, 180))
        actual_time = eta + timedelta(minutes=random.randint(-15, 15))

        # Check if the flight is scheduled after the current time
        if eta > current_time:
            delay = (actual_time - eta).total_seconds() // 60
            status = random.choice(statuses)
            gate_no = f"Gate {random.randint(1, 10)}"

            # Create a unique flight number based on cities and a unique identifier


            flight_data.append({
                "Flight_Number": flight_number,
                "From": from_city,
                "To": to_city,
                "ETA": eta.strftime("%Y-%m-%d %H:%M:%S"),
                "Actual Time": actual_time.strftime("%Y-%m-%d %H:%M:%S"),
                "Delay": f"{int(delay)} min",
                "Status": status,
                "Gate No": gate_no
            })
    print(flight_data)
    return flight_data
