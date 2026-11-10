What it does
This Python program estimates the electricity used by machines in a workshop. It calculates each machine's daily and monthly energy consumption in kilowatt-hours (kWh), estimates the monthly electricity cost using the tariff entered by the user, and displays the total.
How to run it
Install Python 3.
Download or clone this repository.
Open a terminal in the project folder.
Run:
python workshop_energy_cost_estimator.py
Sample output
================================================
       WORKSHOP ENERGY COST ESTIMATOR
================================================
How many machines do you want to enter? 2

Machine 1
Enter machine name: Air Compressor
Power rating in watts: 1500
Hours used per day (0 to 24): 4

Machine 2
Enter machine name: Bench Grinder
Power rating in watts: 750
Hours used per day (0 to 24): 2

Enter your electricity tariff (naira per kWh): 200

                    ENERGY CONSUMPTION REPORT
Machine                  Daily kWh     Monthly kWh Monthly cost (N)
Air Compressor               6.00          180.00       36,000.00
Bench Grinder                1.50           45.00        9,000.00
TOTAL                        7.50          225.00       45,000.00

PROJECT INSIGHT
Highest daily energy user: Air Compressor (6.00 kWh/day).
Tariff used: N200.00 per kWh
Monthly estimate is based on 30 days.
My own twist
The program identifies and displays the machine with the highest daily energy consumption. This can help a workshop identify which machine contributes most to its electricity use.
What I learned
I practised using Python functions, return values, lists, dictionaries, loops, conditional statements, input validation, and basic energy calculations.
By
Alakija Michael, ND Mechatronics Engineering, Yaba College of Technology.
