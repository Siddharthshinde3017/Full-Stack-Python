class company:
    def cname(self):
        print("Xyz private limited")

class department(company):
    def dept(self):
        print("depart ment of IT")

class employee(department):
    def emp(self):
        print("Employee: Johnee")

e = employee()
e.emp()
e.cname()
e.dept()