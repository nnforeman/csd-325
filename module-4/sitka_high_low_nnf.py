import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

# Read dates, highs, and lows once (same CSV as original program)
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        highs.append(int(row[5]))
        lows.append(int(row[6]))

# Menu instructions
print("=== Sitka Weather Viewer ===")
print("Choose: Highs, Lows, or Exit")

# Loop until the user selects Exit
while True:
    choice = input("Enter H for Highs, L for Lows, or E to Exit: ").strip().lower()

    if choice in ('h', 'high', 'highs'):
        # Plot the high temperatures (red), same formatting as original
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice in ('l', 'low', 'lows'):
        # Plot the low temperatures (blue)
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice in ('e', 'exit'):
        print("Thanks for exploring Sitka weather. Goodbye!")
        sys.exit(0)

    else:
        print("Please enter H, L, or E.")