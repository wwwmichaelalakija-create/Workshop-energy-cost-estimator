"""
Workshop Energy Cost Estimator
A beginner-friendly Python mini project for estimating workshop electricity use.
"""

# This list will store the details of every machine entered by the user.
machines = []


def get_positive_number(prompt, allow_zero=False):
    """Ask for a number and keep asking until the user enters a valid value."""
    while True:
        try:
            value = float(input(prompt))

            if value < 0 or (value == 0 and not allow_zero):
                print("Please enter a number greater than zero.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a number, not letters.")


def get_machine_count():
    """Get the number of machines the user wants to calculate for."""
    while True:
        try:
            count = int(input("How many machines do you want to enter? "))

            if count >= 1:
                return count
            else:
                print("Please enter at least 1 machine.")

        except ValueError:
            print("Invalid input. Enter a whole number, such as 2 or 3.")


def calculate_energy(power_watts, hours_per_day):
    """Return the daily energy consumption in kilowatt-hours (kWh)."""
    return (power_watts / 1000) * hours_per_day


def main():
    print("=" * 48)
    print("       WORKSHOP ENERGY COST ESTIMATOR")
    print("=" * 48)

    machine_count = get_machine_count()

    # Collect the details of each machine.
    for number in range(1, machine_count + 1):
        print(f"\nMachine {number}")

        while True:
            machine_name = input("Enter machine name: ").strip()
            if machine_name:
                break
            print("Machine name cannot be empty.")

        power = get_positive_number("Power rating in watts: ")
        hours = get_positive_number("Hours used per day (0 to 24): ", allow_zero=True)

        if hours > 24:
            print("A machine cannot be used for more than 24 hours in one day.")
            while hours > 24:
                hours = get_positive_number("Enter hours from 0 to 24: ", allow_zero=True)

        daily_kwh = calculate_energy(power, hours)

        # Save each machine's information in the list.
        machines.append({
            "name": machine_name,
            "power": power,
            "hours": hours,
            "daily_kwh": daily_kwh
        })

    tariff = get_positive_number(
        "\nEnter your electricity tariff (naira per kWh): "
    )

    print("\n" + "=" * 68)
    print("                    ENERGY CONSUMPTION REPORT")
    print("=" * 68)
    print(f"{'Machine':<22}{'Daily kWh':>14}{'Monthly kWh':>16}{'Monthly cost (N)':>16}")
    print("-" * 68)

    total_daily_kwh = 0
    total_monthly_kwh = 0
    total_monthly_cost = 0

    # Calculate and display the daily and monthly figures for each machine.
    for machine in machines:
        daily = machine["daily_kwh"]
        monthly = daily * 30
        monthly_cost = monthly * tariff

        total_daily_kwh += daily
        total_monthly_kwh += monthly
        total_monthly_cost += monthly_cost

        print(
            f"{machine['name'][:20]:<22}"
            f"{daily:>14.2f}"
            f"{monthly:>16.2f}"
            f"{monthly_cost:>16,.2f}"
        )

    print("-" * 68)
    print(
        f"{'TOTAL':<22}{total_daily_kwh:>14.2f}"
        f"{total_monthly_kwh:>16.2f}{total_monthly_cost:>16,.2f}"
    )

    # Own twist: identify the machine that consumes the most energy each day.
    highest_user = max(machines, key=lambda item: item["daily_kwh"])

    print("\nPROJECT INSIGHT")
    if highest_user["daily_kwh"] == 0:
        print("All machines currently have zero recorded daily energy use.")
    else:
        print(
            f"Highest daily energy user: {highest_user['name']} "
            f"({highest_user['daily_kwh']:.2f} kWh/day)."
        )

    print(f"Tariff used: N{tariff:,.2f} per kWh")
    print("Monthly estimate is based on 30 days.")
    print("\nThank you for using the Workshop Energy Cost Estimator!")


# Run the program when this file is opened directly.
if __name__ == "__main__":
    main()
