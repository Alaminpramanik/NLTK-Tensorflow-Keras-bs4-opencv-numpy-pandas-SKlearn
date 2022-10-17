from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR API KEY'

api_instance = sib_api_v3_sdk.ContactsApi(sib_api_v3_sdk.ApiClient(configuration))
email = 'leadstal@gmail.com'
update_contact = sib_api_v3_sdk.UpdateContact(attributes={'EMAIL': 'alamin493641@gmail.com.com'})

try:
    api_instance.update_contact(email, update_contact)
except ApiException as e:
    print("Exception when calling ContactsApi->update_contact: %s\n" % e)