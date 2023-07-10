# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 07/02/2023
# Last Modified Date : 08/07/2023
# Reviewed by        : Silpa M
# Reviewed on        : 20/02/2023

import user
from user import User
from serviceitems import Service
from payment import Payment
from payment import Customer
from DB_connection import query_execute


class Home:
    name = ""
    user_choice: int = 1

    @staticmethod
    def dashboard(customer_id=""):
        global user_choice
        print("_" * 100)
        print("\t\t\t\t\t\t\t\t\t > Dashboard < -")
        print("_" * 100, "\n")
        query = "Select * from userdata where cus_id=%s;"
        values = (customer_id,)
        result = query_execute(3, query, values)
        try:
            name = result[2] + " " + result[3]
        except TypeError:
            name = result[1]
        print(name, "  signed in @", Service.get_timestamp(3).strftime("%d-%m-%Y"), " " * 50, Service.get_timestamp(4))
        print("\t\t\t\t\t\t\t\t\t    > home < -")
        valid_choice = [1, 2, 3, 4, 5, 6]
        prompt = "\n1.View your details,\n2.Update your details\n3.Service your device \n4.Your last Service details " \
                 "\n5.Make your payment\n6.Sign off\n"
        user_choice = User.get_user_choice(prompt, valid_choice)
        if user_choice == 1:
            User.print_user_details(customer_id)
            Home.dashboard(customer_id)
        elif user_choice == 2:
            User.update_user_details(customer_id)
            Home.dashboard(customer_id)
        elif user_choice == 3:
            Service.rise_service_request(customer_id)
            # Service.rise_request(customer_id)
            Home.dashboard(customer_id)
        elif user_choice == 4:
            Customer().print_details(name, customer_id)
            Home.dashboard(customer_id)
        elif user_choice == 5:
            Payment.payment_methods()
            Home.dashboard(customer_id)
        elif user_choice == 6:
            Home.sign_out(name)

    @classmethod
    def sign_out(cls, name=""):
        global user_choice
        print("_" * 100)
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
                quit()
            elif user_choice == 2:
                Home.dashboard()

    @staticmethod
    def greeting():
        global user_choice
        customer_id = ""
        print("_" * 100, "\n\t\t\t\t\t\t\t- > Welcome to the Application < -")
        print("_" * 100, "\n")
        prompt = "\nExisting User ?\n\t1.Yes\t2.No\n"
        valid_choice = [1, 2]
        user_choice = User.get_user_choice(prompt, valid_choice)
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
