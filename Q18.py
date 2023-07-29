class HourlyPaidEmployee:
    def __init__(self, hourly_rate, ideal_hours, ideal_payment):
        self.hourly_rate = hourly_rate
        self.ideal_hours = ideal_hours
        self.ideal_payment = ideal_payment
    def calculate_gross_pay(self, hours_worked):
        if hours_worked <= self.ideal_hours:
            gross_pay = self.ideal_payment - (self.ideal_hours - hours_worked) * self.hourly_rate
        else:
            extra_hours = hours_worked - self.ideal_hours
            overtime_pay = 75 * extra_hours
            gross_pay = self.ideal_payment + overtime_pay

        return gross_pay

hourly_rate = 75  # Payment rate per hour
ideal_hours = 8
ideal_payment = 1500

employee = HourlyPaidEmployee(hourly_rate, ideal_hours, ideal_payment)

hours_worked = float(input("Enter the number of hours worked: "))
gross_pay = employee.calculate_gross_pay(hours_worked)

print("Gross Pay: ", gross_pay)
