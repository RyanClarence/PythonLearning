#lambda and filter method
list_of_email_addresses = ["vice@gmail.com","zulu@yahoo.com","bob@gmail.com","blessing@bbc.com"]


list_of_address =list(filter(lambda address: address.__contains__("@gmail.com"),list_of_email_addresses))
print(list_of_address)


