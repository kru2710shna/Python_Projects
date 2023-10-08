import phonenumbers

# Input phone number in international format

phone_number = input(("Enter Number:"))

# Parse the phone number
parsed_number = phonenumbers.parse(phone_number, None)

# Check if the phone number is valid
if phonenumbers.is_valid_number(parsed_number):
    print("Valid phone number")
else:
    print("Invalid phone number")

# Get the country associated with the phone number
country = phonenumbers.region_code_for_number(parsed_number)
print("Country:", country)

# Get the national format of the phone number
national_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
print("National Format:", national_format)
