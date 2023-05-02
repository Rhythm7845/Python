import re

def is_valid_credit_card_number(cc_number):
    cc_number = cc_number.replace('-', '')

    if not re.match(r'^\d{16}$', cc_number):
        return False

    if not re.match(r'^[456]', cc_number):
        return False

    if re.match(r'^\d{4}-\d{4}-\d{4}-\d{4}$', cc_number):
        return True

    if re.match(r'^\d{16}$', cc_number):
        return True

    return False

a = input("Enter a credit card number: ")
print(is_valid_credit_card_number(a))