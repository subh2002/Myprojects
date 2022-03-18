import phonenumbers
from phonenumbers import carrier, geocoder, timezone 

mobileNo=input('Enter mobile.no with country code:')
mobileNo=phonenumbers.parse(mobileNo)

#get timezone a phonenumber 
print(timezone.time_zones_for_number(mobileNo))

#getting carrier for phone number 
print(carrier.name_for_number(mobileNo,"en"))

#getting region information
print(geocoder.description_for_number(mobileNo,"en"))

#validating a phone number 
print("valid phone Number :",phonenumbers.is_valid_number(mobileNo))

#checking possiblity of the number 
print("checking the number : ",phonenumbers.is_possible_number(mobileNo))