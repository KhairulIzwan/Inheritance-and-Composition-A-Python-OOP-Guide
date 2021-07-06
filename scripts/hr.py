#!/usr/bin/env python

# import the necessary packages

class PayrollSystem:
	def calculate_payroll(self, employees):
		print('Calculating Payroll')
		print('===================')
		for employee in employees:
			print('Payroll for: {}-{}'.format(
						employee.id, employee.name))
			print('- Check amount: {}'.format(employee.calculate_payroll()))
			print('')
			
class Employee:
	def __init__(self, id, name):
		self.id = id
		self.name = name
		
class SalaryEmployee(Employee, object):
	def __init__(self, id, name, weekly_salary):
		super(SalaryEmployee, self).__init__(id, name)
		self.weekly_salary = weekly_salary

	def calculate_payroll(self):
		return self.weekly_salary
		
class HourlyEmployee(Employee, object):
	def __init__(self, id, name, hours_worked, hour_rate):
		super(HourlyEmployee, self).__init__(id, name)
		self.hours_worked = hours_worked
		self.hour_rate = hour_rate

	def calculate_payroll(self):
		return self.hours_worked * self.hour_rate
		
class CommissionEmployee(SalaryEmployee, object):
	def __init__(self, id, name, weekly_salary, commission):
		super(CommissionEmployee, self).__init__(id, name, weekly_salary)
		self.commission = commission

	def calculate_payroll(self):
		fixed = super(CommissionEmployee, self).calculate_payroll()
		return fixed + self.commission
