from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass


class SalaryEmployee(Employee):
    def __init__(self, employee_id, name, monthly_salary):
        super().__init__(employee_id, name)
        self.monthly_salary = monthly_salary

    def calculate_payroll(self):
        return self.monthly_salary


class HourlyEmployee(Employee):
    def __init__(self, employee_id, name, hours_worked, hourly_rate):
        super().__init__(employee_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate


class VolunteerEmployee(Employee):
    def calculate_payroll(self):
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
    SalaryEmployee(1, "Anna Adams", 1500),
    HourlyEmployee(2, "Bert Branson", 20, 30),
    SalaryEmployee(3, "Chris Corway", 1600),
    VolunteerEmployee(4, "Dermis")
]

payroll_system = PayrollSystem()
payroll_system.calculate_payroll(employees)
