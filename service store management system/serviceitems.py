# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 07/02/2023
# Last Modified Date : 08/07/2023
# Reviewed by        : Silpa M
# Reviewed on        : 20/02/2023

import re
from user import User
from DB_connection import query_execute
from datetime import date, datetime


class Service:
    __service_price = 1000
    __service = "Nominal service Charges"

    @classmethod
    def add_service(cls, __customer_id, timestamp):
        global __service, __service_price
        prompt = (
            "Enter the service you need...\n1.Hardware Service\tRs 5000\n2.Software Service\tRs 1500\n3.General "
            "Service\tRs 3000\n")
        valid_choice = [1, 2, 3]
        user_choice = User.get_user_choice(prompt, valid_choice)
        if user_choice == 1:
            __service = 'Hardware Service'
            __service_price = 5000
        elif user_choice == 2:
            __service = "Software Service"
            __service_price = 1500
        elif user_choice == 3:
            __service = "General Service"
            __service_price = 3000
        query = "insert into service values (%s, %s, %s, %s);"
        values = (__customer_id, __service, __service_price, timestamp)
        query_execute(1, query, values)

    @staticmethod
    def rise_service_request(__customer_id):
        print("_" * 100, "\n\t\t\t\t\t\t\t\t\t- > Service initiation < -")
        print("_" * 100, "\n")
        timestamp = Service.get_timestamp(2)
        query = "insert into service values (%s,'Nominal Service',1000,%s);"
        values = (__customer_id, timestamp)
        query_execute(1, query, values)
        Service.add_service(__customer_id, timestamp)
        valid_choice = [1, 2]
        prompt = "Want to add another service \n 1.Yes or 2.No\n"
        while True:
            user_choice = User.get_user_choice(prompt, valid_choice)
            if user_choice == 1:
                print("\n")
                Service.add_service(__customer_id, timestamp)
            elif user_choice == 2:
                break

    @staticmethod
    def give_service_list():
        return Service.__service

    @staticmethod
    def give_service_price():
        return Service.__service_price

    # under development
    @staticmethod
    def generate_service_id(__customer_id="", name=""):
        name = re.sub(r"\s+", " ", name)
        name = name.upper()
        value = str(Service.get_timestamp(3))
        value = value.replace("-", "")
        service_id = "SER" + name[:2] + value[:3:-1]
        return service_id
        # pass

    @staticmethod
    def get_timestamp(case=0):
        # Get the current timestamp
        timestamp = datetime.timestamp(datetime.now())
        # gets current date
        value = date.today()
        # Format the datetime object as a string
        dt = datetime.fromtimestamp(timestamp)
        # Format the datetime object as a string
        formatted_datetime = dt.strftime("%Y-%m-%d %H:%M:%S")
        #
        current_time = datetime.now().time()
        time_string = current_time.strftime("%I:%M:%S %p")
        # function call for timestamp
        if case == 1:
            return timestamp
        # function call for date and time
        elif case == 2:
            return formatted_datetime
        # function call for date
        elif case == 3:
            return value
        # function call for time with local format
        elif case == 4:
            return time_string

    # Under development
    @staticmethod
    def rise_request(__customer_id=""):
        print("_" * 100, "\n\t\t\t\t\t\t\t\t\t- > Service initiation < -")
        print("_" * 100)
        time = Service.get_timestamp(2)
        print("The device name:")
        device_name = input()
        print("Model name:")
        model_name = input()
        print("Explain the faults that encountered while using this device:")
        defect_description = input()
        usaage = ""
        prompt = "How do you use the device ?\n\t1.Minimal\t2.Nominal\t3.Extensive\n"
        valid_choices = [1, 2, 3]
        user_choice = User.get_user_choice(prompt, valid_choices)
        if user_choice == 1:
            usaage = "Minimal"
        elif user_choice == 2:
            usaage = "Nominal"
        elif user_choice == 3:
            usaage = "Extensive"
        query = "insert into service_request values(%s,%s,%s,%s,%s,%s,%s,%s);"
        service_id = Service.generate_service_id(__customer_id, model_name)
        print("1.CustomerID:", __customer_id, "\n2.ServiceID:", service_id, "\n3.Device name:", device_name,
              "\n4.Model name:",
              model_name, "\n5.Defect:", defect_description, "\n6.Usage:", usaage, "\n7.Time:", time)
        prompt = "please ensure where all your request details are correct\n\t1.Yes\t2.No\n"
        valid_choice = [1, 2]
        status = "Initiated"
        user_choice = User.get_user_choice(prompt, valid_choice)
        if user_choice == 1:
            values = (__customer_id, service_id, device_name, model_name, defect_description, usaage, status, time)
            query_execute(1, query, values)
        else:
            prompt = "Do you need to update the details\n\t1.yes\t2.No\n"
            user_choice = User.get_user_choice(prompt, valid_choice)
            if user_choice == 2:
                values = (__customer_id, service_id, device_name, model_name, defect_description, usaage, status, time)
                query_execute(1, query, values)
            elif user_choice == 1:
                prompt = "Which value do you need to update?\n"
                valid_choice = [1, 2, 3, 4, 5, 6]
                user_choice = User.get_user_choice(prompt, valid_choice)
                if user_choice == 1 or user_choice == 2 or user_choice == 6:
                    print("Not possible")
                elif user_choice == 3:
                    print("Enter the detail to be updated")
                    device_name = input()
                elif user_choice == 4:
                    print("Enter the detail to be updated")
                    model_name = input()
                elif user_choice == 5:
                    print("Enter the detail to be updated")
                    defect_description = input()
                values = (__customer_id, service_id, device_name, model_name, defect_description, usaage, status, time)
                query_execute(1, query, values)
        print("The service request has been raised over technicians will get to the linked address and collect the "
              "device with-in 1 or 2 working days\n so please verify the address\n")
        query = "Select * from address where cus_id = %s;"
        values = (__customer_id,)
        result = query_execute(3, query, values)
        value = result[1:7]
        for i in range(len(value)):
            if i < 1:
                print("Address:", value[i])
            else:
                print("\t\t", value[i])
        prompt = "\nAre you available in this address with the device\n\t1.Yes\t\t2.No\n"
        valid_choices = [1, 2]
        user_choice = User.get_user_choice(prompt, valid_choices)
        if user_choice == 1:
            exit()
        else:
            print("Please update the address as soon as possible in the yours details")
