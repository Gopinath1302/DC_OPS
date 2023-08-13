# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 07/02/2023
# Last Modified Date : 07/08/2023
# Reviewed by        : Silpa Madhusoodanan
# Reviewed on        : 20/02/2023

import re
from tabulate import tabulate
from serviceitems import Service
from user import User
from DB_connection import query_execute, loading_animation


class Payment:

    # User-defined function to get user's card cvv number and authenticate it
    @staticmethod
    def get_ccv():
        flag = True
        ccv_pattern = r'^(?!.*(.).*\1)(?!(?:012|123|234|345|456|567|678|789))\d{3}$'
        while flag:
            print("Enter your card's ccv")
            try:
                ccv = int(input())
            except(TypeError, KeyboardInterrupt):
                print("Invalid entry")
            else:
                rule = re.compile(ccv_pattern)
                if re.search(rule, str(ccv)):
                    status = True
                else:
                    status = False
                    print("You have entered a invalid CCV")
            flag = not status
        return status

    # User-defined function to get user's card pin
    @staticmethod
    def get_pin():
        pin = 0
        flag = True
        while flag:
            print("Enter your Transaction pin")
            try:
                pin = int(input())
            except (TypeError, KeyboardInterrupt, NameError):
                print("Invalid pin!\nPlease try to enter a valid pin")
            finally:
                return pin

    # User-defined function to get user's card pin authenticate it
    @staticmethod
    def validate_pin(pin):
        pin_pattern = '^(?!.*(.).*\1)(?!(?:0123|1234|2345|3456|4567|5678|6789|7890))\d{4}$'
        rule = re.compile(pin_pattern)
        if re.search(rule, str(pin)):
            status = True
        else:
            status = False
        return status

    # User-defined function to validate a user's card number
    @staticmethod
    def is_luhn_valid(card_number):
        card_number = str(card_number).replace(" ", "")  # Remove any spaces
        if not card_number.isdigit():
            return False  # The card number must contain only digits
        digits = [int(digit) for digit in card_number]
        checksum = 0
        # Double every second digit from the right
        for i in range(len(digits) - 2, -1, -2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9
        # Sum all the digits, including the doubled ones
        checksum = sum(digits)
        # Check if the checksum is divisible by 10
        return checksum % 10 == 0

    # User-defined function to get user's card number
    @staticmethod
    def get_card_number():
        flag = True
        status = True
        while flag:
            print("Enter your card number")
            card_no = int(input())
            status = Payment.is_luhn_valid(card_no)
            flag = not status
        return status

    # User-defined function to print total price from DB
    @staticmethod
    def print_total(total):
        print("Your making a payment of Rs:", total)

    # User-defined function to get user's card cvv expiry date and authenticate it
    @staticmethod
    def get_expiry_date():
        status = True
        flag = True
        current_year = Service.get_timestamp(6)
        current_month = Service.get_timestamp(5)
        while flag:
            try:
                print("Enter your card's expiry month")
                valid_month = int(input())
            except (TypeError, KeyboardInterrupt):
                print("Invalid entry!")
            else:
                if 1 <= valid_month < 13 and valid_month >= current_month:
                    status = True
                else:
                    status = False
                    print("You have entered a invalid card expiry month!")
            # print(status)
            try:
                print("Enter your card's expiry year")
                valid_year = int(input())
            except:
                print("Invalid Entry")
            else:
                if valid_year >= current_year:
                    status = True
                else:
                    status = False
                    print("You have entered a invalid card expiry Year!")
            # print(status)
            flag = not status
        return status

    # User-defined function to validate user's upi-id
    @staticmethod
    def validate_upi_id(upi_id):
        regex = '^[a-zA-Z0-9._]+@(?!.*\.\.)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        rule = re.compile(regex)
        if re.search(rule, upi_id):
            return True
        else:
            return False

    # User-defined function to get user's upi-id
    @staticmethod
    def get_upi_id():
        flag = True
        status = True
        while flag:
            print("Enter your UPI-ID :")
            upi_id = input()
            status = Payment.validate_upi_id(upi_id)
            flag = not status
        return status

    # User-defined function to perform online banking process
    @staticmethod
    def online_banking(total):
        print("\nEnter your Bank name")
        bank_name = input()
        query = "select * from bank where bank_name = %s;"
        values = (bank_name,)
        result = query_execute(3, query, values)
        if result is not None:
            print("Please wait we are redirecting your bank server")
            loading_animation(6, word=None)
            print("Enter username for your internet banking: ")
            username = input()
            print("Enter password for your internet banking: ")
            password = input()
            if username and password is not None:
                Payment.print_total(total)
                pin = Payment.get_pin()
                status = Payment.validate_pin(pin)
                if status:
                    loading_animation(2, word=None)
                    print("Thank you For your purchase, visit again")
                else:
                    print("You have entered An incorrect pin\n")
                    status = False
            else:
                print("Invalid User credentials!")
                status = False
        else:
            print("Invalid Bank Name!")
            status = False

        return status

    # User-defined function to perform card transactions
    @staticmethod
    def card_transaction(total):
        global status
        status = False
        status = Payment.get_card_number()
        status = Payment.get_expiry_date()
        status = Payment.get_ccv()
        loading_animation(6, word=None)
        Payment.print_total(total)
        pin = Payment.get_pin()
        status = Payment.validate_pin(pin)
        loading_animation(2, word=None)
        if status:
            print("The transaction has been completed successfully and will be updated in the dashboard later")
        else:
            print("You have entered an in valid pin!")
        return status

    # User-defined function to get user's card cvv number and authenticate it
    @staticmethod
    def upi_payment(total):
        global status
        status = Payment.get_upi_id()
        status = Payment.get_pin()
        print("Please wait we are redirecting your bank server")
        loading_animation(6, word=None)
        Payment.print_total(total)
        pin = Payment.get_pin()
        status = Payment.validate_pin(pin)
        if status:
            loading_animation(2, word=None)
            print("Thank you For your purchase, visit again")
        else:
            print("You have entered an in valid pin!")
        return status

    # User-defined function to payment
    @staticmethod
    def payment_methods(total):
        text = "-> Payments <-"
        print("_" * 105, "\n", text.center(105))
        print("_" * 105)
        prompt = (
            "\n1. Net Banking\n2. Credit / Debit card\n3. UPI Payment\n4. Back to Dashboard\nEnter your choice:\n")
        flag = True
        status = True
        valid_choice = [1, 2, 3, 4]
        while flag:
            user_choice = User.get_user_choice(prompt, valid_choice)
            if user_choice == 1:
                status = Payment.online_banking(total)
            elif user_choice == 2:
                status = Payment.card_transaction(total)
            elif user_choice == 3:
                status = Payment.upi_payment(total)
            elif user_choice == 4:
                status = True
            flag = not status
        return status


class Bill(Payment):
    total = 0

    # User-defined function to calculate the total price
    @classmethod
    def calculate_total(cls, __customer_id):
        query = "Select sum(price) from services where cus_id = %s and p_status = 'Pending';"
        values = (__customer_id,)
        result = query_execute(3, query, values)
        total = result[0]
        return total

    # User-defined function to auto - update the payment status to the DB when ever the price is updated in the DB
    @staticmethod
    def auto_update_payment_status(service_id):
        query = "update services set  p_status = %s where service_id = %s"
        values = ('Pending', service_id)
        query_execute(1, query, values)

    # User-defined function to update the payment status to the DB
    @staticmethod
    def update_payment_status(customer_id, status):
        if status:
            query = "update services set  p_status = %s where cus_id = %s"
            values = ('Successful', customer_id)
            result = query_execute(1, query, values)

    # User-defined function to display the user's Service details
    @staticmethod
    def print_details(name, __customer_id):
        text = "-> Services done <-"
        print("_" * 105, "\n", text.center(105))
        print("_" * 105)
        print("\nYour last Service details are as follows\n")
        print("Name: ", name, "\n")
        print("_" * 40, "\n")
        total = Bill.calculate_total(__customer_id)
        # service_id, cus_id, device_name, serviced_by, sdate, s_status, price, p_status, timestamp
        query = (
            "Select service_id, device_name, s_status, p_status, timestamp from services where cus_id = %s and p_status = "
            "'Pending';")
        values = (__customer_id,)
        result = query_execute(4, query, values)
        header = ["Service ID", "Device", " Service status", "Payment status", "Timestamp"]
        print(tabulate(result, headers=header, tablefmt="grid"))
        print("\nYour total for last service is Rs", total)
