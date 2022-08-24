import os
from sendgrid import SendGridAPIClient


# sg = SendGridAPIClient(('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'))

# list_id = "5f208410-1a15-4e89-88f6-6265fefa35e8"
# params = {'list_id': 4900}
# data = {
#     "name": "alamin"
# }

# response = sg.client.contactdb.lists._(list_id).put(
#     query_params=params,
#     request_body=data
# )

# print(response.status_code)
# print(response.body)
# print(response.headers)


# import os
# from sendgrid import SendGridAPIClient


# sg = SendGridAPIClient(os.environ.get('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'))

# id = "5f208410-1a15-4e89-88f6-6265fefa35e8"
# data = {
#     "name": "alamin493641@gmail.com"
# }

# response = sg.client.marketing.lists._(id).patch(
#     request_body=data
# )

# print(response.status_code)
# print(response.body)
# print(response.headers)

# import os
# from sendgrid import SendGridAPIClient


sg = SendGridAPIClient('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')

data = {
    "contacts":[
        {
            "email": "poroshpramaniks@gmail.com"
        }
    ]
}

response = sg.client.marketing.contacts.put(
    request_body=data
)

print(response.status_code)
print(response.body)
print(response.headers)

# import os
# from sendgrid import SendGridAPIClient


# sg = SendGridAPIClient(('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'), impersonate_subuser = "The subuser's username. This header generates the API call as if the subuser account was making the call.")

# data = {
#     "name": "poroshpramanik@gmail.com"
# }

# response = sg.client.contactdb.lists.post(
#     request_body=data
# )

# print(response.status_code)
# print(response.body)
# print(response.headers)


