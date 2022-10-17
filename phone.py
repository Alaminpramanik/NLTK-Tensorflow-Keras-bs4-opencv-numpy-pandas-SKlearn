import phonenumbers
from phonenumbers import geocoder

ch_number = phonenumbers.parse("17.0010.000", "CH")
print('phoness', ch_number)
geo=geocoder.description_for_number(ch_number, "bd")
print('geo', geo)
