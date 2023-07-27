# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 07/02/2023
# Last Modified Date : 27/07/2023
# Reviewed by        : Silpa M
# Reviewed on        : 20/02/2023


import time
from serviceitems import Service
import datetime
from user import User
import re
from DB_connection import query_execute


class Payment:

    @staticmethod
    def payment_methods(total):
        card_number = 111
        pin = 1
        print("_" * 100)
        print("\t\t\t\t\t\t\t\t\t- > Payment < -")
        print("_" * 100, "\n")
        # print("_" * 100)
        print("1. Net Banking")
        print("2. Credit / Debit card")
        print("3. UPI Payment")
        flag = True
        prompt = "Enter your choice:\n"
        valid_choice = [1, 2, 3]
        user_choice = User.get_user_choice(prompt, valid_choice)
        while flag:
            if user_choice == 1:
                print("Type your Bank name\n")
                bank_name = input()
                time.sleep(5)
                print("Loading....")
                print("Please wait we are redirecting your bank server")
                print("Enter username: ")
                username = input()
                print("Enter password: ")
                password = input()
                print("Your making a payment of Rs:", total)
                print("Enter your Transaction pin")
                try:
                    pin = int(input())
                except TypeError:
                    print("invalid entry")
                    if pin == 1234:
                        print("Loading....")
                        time.sleep(7)
                        print("Thank you For your purchase, visit again")
                        flag = False
                    else:
                        print("You have entered An incorrect pin\nWill restart your payment")
                        Payment.payment_methods(total)

            elif user_choice == 2:
                try:
                    print("Enter your card number")
                    card_number = int(input())
                except TypeError:
                    print("Invalid entry !\nPlease try to enter a valid choice")
                if 1000000000000000 < card_number < 9999999999999999:
                    print("Your making a payment of Rs:", total)
                    print("Loading....")
                    time.sleep(5)
                    try:
                        print("Enter your pin")
                        pin = int(input())
                    except TypeError:
                        print("Invalid entry !\nPlease try to enter a valid choice")
                    if pin == 1234:
                        print("Loading....")
                        time.sleep(7)
                        print("Thank you For your purchase, visit again")
                        flag = False
                    else:
                        print("You have entered An incorrect pin \nWill restart your payment")
                        Payment.payment_methods(total)

            elif user_choice == 3:
                regex = "^[A-Za-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
                rule = re.compile(regex)
                while flag:
                    print("Enter your UPI-ID :")
                    upi_id = input()
                    if re.search(rule, upi_id):
                        print("Please wait we are redirecting your bank server")
                        print("Loading....")
                        time.sleep(7)
                        print("Your making a payment of Rs:", total)
                        print("Enter your pin")
                        try:
                            pin = int(input())
                        except TypeError:
                            print("Invalid entry !\nPlease try to enter a valid choice")
                        if pin == 1234:
                            print("Loading....")
                            time.sleep(7)
                            print("Thank you For your purchase, visit again")
                            flag = False
                    else:
                        print("Invalid UPI-Id!\nPlease try  to enter a valid UPI-Id")
                        Payment.payment_methods(total)


class Customer(Payment):
    total = 0

    @classmethod
    def calculate_total(cls, __customer_id):
        query = "Select sum(price) from service where cus_id = %s;"
        values = (__customer_id,)
        result = query_execute(3, query, values)
        # print(result)
        total = result[0]
        return total

    @staticmethod
    def print_details(name, __customer_id):
        print("_" * 100, "\n\t\t\t\t\t\t\t\t\t", "> Services done <")
        print("_" * 100)
        print("\nYour last Service details are as follows\n")
        print("Name: ", name, "\n")
        x = datetime.datetime.now()
        print("Date: ", x.strftime("%c"))
        print("")
        print("_" * 40, "\n")
        total = Customer.calculate_total(__customer_id)
        query = "Select service_name, price from service where cus_id = %s;"
        values = (__customer_id,)
        result = query_execute(4, query, values)
        print("\n   Service \t\t\t Price")
        for row in result:
            list1 = row
            print(list1[0], "\t", list1[1])
        print("\nYour total service charge is  Rs", total)
