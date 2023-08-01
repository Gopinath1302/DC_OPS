# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 07/02/2023
# Last Modified Date : 27/07/2023
# Reviewed by        : Silpa Madhusoodanan
# Reviewed on        : 20/02/2023

import user
from user import User
from serviceitems import Service
from payment import Payment
from payment import Customer
from DB_connection import query_execute, check_db, close_db_connection


class Home:
    name = ""
    user_choice: int = 1

    # User-defined function to display dashboard
    @staticmethod
    def dashboard(customer_id=""):
        global user_choice
        print("\t\t\t\t\t\t\t\t\t    > home < -")
        print("_" * 105)
        print("\t\t\t\t\t\t\t\t\t > Dashboard < -")
        print("_" * 105, "\n")
        query = "Select * from userdata where cus_id=%s;"
        values = (customer_id,)
        result = query_execute(3, query, values)
        try:
            name = result[2] + " " + result[3]
        except TypeError:
            name = result[1]
        print(name, "  signed in @", Service.get_timestamp(3).strftime("%d-%m-%Y"), " " * 50, Service.get_timestamp(4))
        valid_choice = [1, 2, 3, 4, 5, 6, 7]
        prompt = "\n1.View your details,\n2.Update your details\n3.Service your device \n4.Your last Service details " \
                 "\n5.Make your payment\n6.Notifications\n7.Sign off\n"
        user_choice = User.get_user_choice(prompt, valid_choice)
        if user_choice == 1:
            User.print_user_details(customer_id)
            Home.dashboard(customer_id)
        elif user_choice == 2:
            User.update_user_details(customer_id)
            Home.dashboard(customer_id)
        elif user_choice == 3:
            Service.rise_service_request(customer_id, name)
            # Service.rise_request(customer_id)
            Home.dashboard(customer_id)
        elif user_choice == 4:
            Customer().print_details(name, customer_id)
            Home.dashboard(customer_id)
        elif user_choice == 5:
            total = Customer.calculate_total(customer_id)
            status = Payment.payment_methods(total)
            Customer.update_payment_status(customer_id, status)
            Home.dashboard(customer_id)
        elif user_choice == 6:
            Home.check_notification(customer_id)
            Home.dashboard(customer_id)
        elif user_choice == 7:
            Home.sign_out(name)

    # User-defined function to sig-out a user
    @classmethod
    def sign_out(cls, name=""):
        global user_choice
        print("_" * 105)
        flag = True
        valid_choice = [1, 2]
        prompt = "\nExit Application or not ?\n 1.Yes\t2.No\n"
        while flag:
            user_choice = user.User.get_user_choice(prompt, valid_choice)
            if user_choice == 1:
                print(
                    "\t\t\t\t\t\t\t\t\t-> Signed out Successfully! <- \n\n\t\t\t\t\t\t\t\t\t", name,
                    " thanks for using "
                    "this "
                    "application!\n")
                close_db_connection()
                quit()
            elif user_choice == 2:
                Home.dashboard()

    # User-defined function to greet and authenticate a user
    @staticmethod
    def greeting():
        global user_choice
        customer_id = ""
        print("_" * 105, "\n\t\t\t\t\t\t\t- > Welcome to the Application < -")
        print("_" * 105, "\n")
        prompt = "\nExisting User ?\n\t1.Yes\t2.No\n"
        valid_choice = [1, 2]
        user_choice = User.get_user_choice(prompt, valid_choice)
        check_db()
        if user_choice == 1:
            customer_id = User().sign_in()
        elif user_choice == 2:
            prompt1 = "Want to register as a user or exit the application?\n\t1.Sign-up\t2.Exit\n"
            user_choice = User.get_user_choice(prompt1, valid_choice)
            if user_choice == 1:
                User.sign_up()
                customer_id = User().sign_in()
            elif user_choice == 2:
                quit()
        # print(customer_id)
        Home.dashboard(customer_id)

    @staticmethod
    def check_notification(customer_id):
        print("_" * 105, "\n\t\t\t\t\t\t\t\t > Notifications < -")
        print("_" * 105, "\n")
        prompt = "\t" * 6 + "1.You have a pending bill amount of : Rs "
        total = Customer.calculate_total(customer_id)
        if total is not None:
            print(prompt, total,"\n")
            print("please navigate to make your payments to pay the remaining bill\n\n")
        else:
            print("You have no notification")
