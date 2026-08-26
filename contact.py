class Contact:

    def __init__(self, Name, Phone_Number, Email):
        self.Name = Name
        self.Phone_Number = Phone_Number
        self.Email = Email

    def formatContact(self):

        print("Name: {}".format(self.Name))
        print("Phone Number: {}".format(self.Phone_Number))
        print("Email: {}".format(self.Email))