from datetime import date, datetime
import re


#
def get_timestamp(case=0):
    # gets the current timestamp
    value = datetime.now()
    timestamp = datetime.timestamp(value)
    # gets the current month
    current_month = value.month
    # gets the current year
    current_year = value.year
    # gets the current date
    value = date.today()
    # Format the datetime object as a string
    dt = datetime.fromtimestamp(timestamp)
    # Format the datetime object as a string
    formatted_datetime = dt.strftime("%Y-%m-%d %H:%M:%S")
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
    elif case == 5:
        return current_month
    elif case == 6:
        return current_year


#
#
# print("Case 1:", get_timestamp(1))
# print("Case 2:", get_timestamp(2))
# print("Case 3:", get_timestamp(3))
# print("Case 4:", get_timestamp(4))
# print("Case 5:", get_timestamp(5))
# print("Case 6:", get_timestamp(6))
#
#
# # print("Case 1:", get_timestamp(1))
#
# def card_validation(case, card_no, v_year, v_month, ccv):
#     # global status
#     Visa_pattern = r'^4\d{16}(?:\d{4})?$'
#     Mastercard_pattern = r'^5[1-5]\d{14}$'
#     RuPay_pattern = r'^5084\d{10}$'
#     ccv_pattern = r'^(?!.*(.).*\1)(?!(?:012|123|234|345|456|567|678|789))\d{3}$'
#     if case == 1:
#         rule = re.compile(Visa_pattern)
#         if re.search(rule, str(card_no)):
#             status = True
#         else:
#             status = False
#     if case == 2:
#         rule = re.compile(Mastercard_pattern)
#         if re.search(rule, str(card_no)):
#             status = True
#         else:
#             status = False
#     if case == 3:
#         rule = re.compile(RuPay_pattern)
#         if re.search(rule, str(card_no)):
#             status = True
#         else:
#             status = False
#     current_year = get_timestamp(6)
#     current_month = get_timestamp(5)
#     if 1 <= v_month < 13 and v_month >= current_month and v_year >= current_year:
#         status = True
#     else:
#         status = False
#
#     rule = re.compile(ccv_pattern)
#     if re.search(rule, str(ccv)):
#         status = True
#     else:
#         status = False
#     return status


# # print(card_validation(2, 5178, 2022, 1, 603))
# # card_no = 4017042708031864
# # card_no = 5084999999999999
# card_no = 5084065432109876
# # card_no = 1234567890123456
# Visa_pattern = r'^4\d{15}$'
# # Mastercard_pattern = r'^5[1-5]\d{14}$'
# RuPay_pattern = r'^5084\d{12}$'
# ccv_pattern = r'^(?!.*(.).*\1)(?!(?:012|123|234|345|456|567|678|789))\d{3}$'
#
# Mastercard_pattern = r'^5[1-5]\d{14}$'
# rule = re.compile(Mastercard_pattern)
# if re.search(rule, str(card_no)):
#     status = True
# else:
#     status = False
# print(status)
# def is_luhn_valid(card_number):
#     card_number = str(card_number).replace(" ", "")  # Remove any spaces
#     if not card_number.isdigit():
#         return False  # The card number must contain only digits
#
#     digits = [int(digit) for digit in card_number]
#     checksum = 0
#
#     # Double every second digit from the right
#     for i in range(len(digits) - 2, -1, -2):
#         digits[i] *= 2
#         if digits[i] > 9:
#             digits[i] -= 9
#
#     # Sum all the digits, including the doubled ones
#     checksum = sum(digits)
#
#     # Check if the checksum is divisible by 10
#     return checksum % 10 == 0
#
#
# # Example usage:
# card_number = "5178770109554769"  # Replace with the card number to check
# valid = is_luhn_valid(card_number)
# print("Is the card number valid?", valid)
#
#
# def validate_pin(pin):
#     pin_pattern = '^(?!.*(.).*\1)(?!(?:0123|1234|2345|3456|4567|5678|6789|7890))\d{4}$'
#     rule = re.compile(pin_pattern)
#     if re.search(rule, str(pin)):
#         status = True
#     else:
#         status = False
#     return status
#
# print(validate_pin(2217))
# def get_ccv():
#     status = True
#     flag = True
#     ccv = 1
#     ccv_pattern = r'^(?!.*(.).*\1)(?!(?:012|123|234|345|456|567|678|789))\d{3}$'
#     while flag:
#         print("Enter your card's ccv")
#         try:
#             ccv = int(input())
#         except:
#             print("Invalid entry")
#         else:
#             rule = re.compile(ccv_pattern)
#             if re.search(rule, str(ccv)):
#                 status = True
#             else:
#                 status = False
#                 print("You have entered a invalid CCV")
#         flag = not status
#     return status
#
# s = get_ccv()
# print(s)

prompt = "_" * 100 + "\n" + "\t" * 9 + "- > Payment < -\n" + "_" * 100 + "\n1. Net Banking\n2. Credit / Debit card\n3. UPI Payment\n4. Back to Dashboard\n"

print(prompt)
