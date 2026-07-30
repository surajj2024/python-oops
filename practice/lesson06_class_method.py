class Employee:
    company = "google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"name: {self.name} Salary: {self.salary} name: {self.company}")

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

    @classmethod
    def default_employee(cls, data):
        return cls(data["name"], data["salary"])


suraj = Employee("suraj", 20000)
suraj.change_company("new company")
data = {"name": "unknown", "salary": 0}
newEmployee = Employee.default_employee(data)
suraj.show_details()
newEmployee.show_details()


