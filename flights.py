import random, time
from views import connection, get_flight_services
from datetime import datetime, timedelta


def generate_random_flight_data(num_records=12):
    services = get_flight_services(connection())
    statuses = ["On Time", "Delayed"]

    flight_data = []

    current_time = datetime.now()

    for i in range(num_records):
        flight_number = services[i][1]
        from_city = services[i][2]
        to_city = services[i][3]
        eta = current_time + timedelta(minutes=random.randint(5, 20))
        actual_time = eta + timedelta(minutes=random.randint(-15, 15))

        # Check if the flight is scheduled after the current time
        if eta > current_time:
            delay = (actual_time - eta).total_seconds() // 60
            status = random.choice(statuses)
            gate_no = f"Gate {random.randint(1, 8)}"

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
    return flight_data

