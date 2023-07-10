import Db_connection
from Db_connection import cursor,connect
import Reserve
def display_stations():
    cursor.execute("SELECT * FROM stations")
    stations = cursor.fetchall()
    if stations:
        print("Station ID\tName")
        print("-----------------")
        for station in stations:
            print(f"{station[0]}\t\t{station[1]}")
    else:
        print("No stations available.")
def display_trains():
    cursor.execute("SELECT * FROM trains")
    trains = cursor.fetchall()
    if trains:
        print("Train_no\tSource_name\t\t\t\tDestination_name\t\tDeparture_time\tArrival_time\tAC-Sleeper\t\tSleeper\t\tSitting")
        print("--------------------------------------------------------------------------------------------------------------------------------")
        for train in trains:
            print(f"{train[0]}\t\t\t\t{train[1]}\t\t\t\t{train[2]}\t\t\t\t{train[3]}\t\t\t{train[4]}\t\t\t{train[5]}\t\t\t\t{train[6]}\t\t{train[7]}")
    else:
        print("No trains available.")

def main():
    flag = True
    while flag:
        print("1. Display Stations")
        print("2. Display Trains")
        print("3. Reservations")
        print("4. Exit")
        # choice = int(input("Enter your choice: "))
        while True:
            try:
                choice = int(input("Enter a number: "))
                break  # Break out of the loop if a valid number is entered
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        if choice == 1:
            display_stations()
        elif choice == 2:
            display_trains()
        elif choice == 3:
            Reserve.main()
        elif choice == 4:
            flag = False
