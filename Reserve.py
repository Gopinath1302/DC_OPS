import Db_connection
from Db_connection import connect,cursor
from datetime import date
import random
def book_reservation(passenger_name, train_number,seat_type,no_of_passengers):
    cursor = connect.cursor()
    sql = "INSERT INTO reservations (passenger_name, train_number,seat_type,no_of_passengers,status) VALUES (%s, %s, %s, %s,'booked')"
    values = (passenger_name, train_number,seat_type,no_of_passengers)
    cursor.execute(sql, values)
    connect.commit()
    print("Reservation successful!")


def cancel_reservation(reservation_id):
    cursor = connect.cursor()
    sql = "UPDATE reservations SET status='canceled' WHERE reservation_id = %s"
    values = (reservation_id,)
    cursor.execute(sql, values)
    connect.commit()
    on = 0
    ont = (random.randint(1000, 9999))
    print(ont)
    flag = True
    while flag:
        try:
            on = int(input("Enter on number:"))
        except:
            print("you have entered a Invalid on number please try with valid one:")
        else:
            print(on)
            flag = False

    if on == ont:
        print("Your Amount will be credited within 3 working days on your bank account")
        print("Reservation canceled successfully!")
    else:
        print("enter the valid on number:")




def view_reservations():
    cursor = connect.cursor()
    sql = "SELECT * FROM reservations WHERE status='booked'"
    cursor.execute(sql)
    reservations = cursor.fetchall()
    if reservations:
        print("Current Reservations:")
        for reservation in reservations:
            print(f"Reservation ID: {reservation[0]}, Passenger: {reservation[1]}, Train_number: {reservation[2]}")
    else:
        print("No reservations found.")
def make_payment(card_number, expiration_date, cvv):
    sql = "INSERT INTO payment (card_number, expiration_date, cvv) VALUES (%s, %s, %s)"
    values = (card_number, expiration_date, cvv)
    cursor.execute(sql, values)
    connect.commit()
    print("Payment has been successfull")
def main():
    flag = True
    while flag:
        print("\n1. Book a reservation")
        print("2. Cancel a reservation")
        print("3. View all reservations")
        print("4. Exit")
        # choice = int(input("Enter your choice: "))
        while True:
            try:
                choice = int(input("Enter a number: "))
                break  # Break out of the loop if a valid number is entered
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if choice == 1:
            passenger_name = input("Enter passenger name: ")
            train_number = int(input("Enter train number: "))
            seat_type = input("Enter seat type:")
            no_of_passengers =int(input("Enter no of passengers:"))
            book_reservation(passenger_name,train_number,seat_type,no_of_passengers)
            card_number = int(input("Enter card number:"))
            year = int(input('Enter a year: '))
            month = int(input('Enter a month: '))
            day = int(input('Enter a day: '))
            expiration_date = date(year, month, day)
            cvv = int(input("Enter cvv:"))
            make_payment(card_number, expiration_date, cvv)

            d = date(year, month, day)
            print(d)

        elif choice == 2:
            reservation_id = int(input("Enter reservation ID to cancel: "))
            cancel_reservation(reservation_id)
        elif choice == 3:
            view_reservations()

        elif choice == 4:
            flag = False

        else:
            print("Invalid choice. Try again.")