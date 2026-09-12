class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show_details(self):
        print(f"here is the details {self.name} {self.email}")
        
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["email"])


data = {"name": "Suraj", "email": "suraj@example.com"}

suraj = User.from_dict(data)
suraj.show_details()

