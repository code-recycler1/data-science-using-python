class Employee:
    def __init__(self, employee_id, name, monthly_salary=0, hours_worked=0, hourly_rate=0):
        self.employee_id = employee_id
        self.name = name
        self.monthly_salary = monthly_salary
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        if self.monthly_salary:
            return self.monthly_salary
        elif self.hours_worked and self.hourly_rate:
            return self.hours_worked * self.hourly_rate
        else:
            return None


class PayrollSystem:
    def calculate_payroll(self, employees):
        header = "Calculating Payroll"
        print(header)
        print("=" * len(header))
        for employee in employees:
            print(f"Payroll for {employee.employee_id} - {employee.name}")
            payroll_amount = employee.calculate_payroll()
            if payroll_amount is not None:
                print(f"- Check amount: {payroll_amount}")
            else:
                print("- Check amount: None")
            print("")


# Adding employees and running the payroll system
employees = [
    Employee(1, "Anna Adams", monthly_salary=1500),
    Employee(2, "Bert Branson", hours_worked=20, hourly_rate=30),
    Employee(3, "Chris Corway", monthly_salary=1600),
    Employee(4, "Dermis")
]

payroll_system = PayrollSystem()
payroll_system.calculate_payroll(employees)
