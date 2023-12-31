#!/usr/bin/env python
# coding: utf-8

# # First Semester Project: Automating Accounting Procedures for a Business(Individual Project)

# ## Project Overview:
# ### A local retail business, dealing with a variety of products, aims to streamline and automate its accounting procedures. The business operates two shifts per day with one worker on each shift. The primary goal is to create a Python project that assists in automating essential accounting tasks, including calculating total sales, worker salaries, profit, tips, and total tips for the day.
# 

# #### Key Features:
# 1.	Calculate Total Sales for the Day: from sales data for morning and evening shifts, produce total sales for the day.
# 2.	Calculate Worker's Salary: given hourly rate and hours worked by a worker. retrieve the worker's salary.
# 3.	Calculate Profit: given a list of numbers representing total sales and total cost of items sold, find the profit.(or loss if negative)
# 4.	Calculate Tips for a Shift: from sales data for a specific shift, workers get tipped for the shift (2% of shift sales).
# 5.	Calculate Total Tips for the Day: with sales data for morning and evening shifts, return total tips for the day (sum of tips from both shifts).
# 	Think of your shift sales as a list.
# 
# #### User Interface:
# ●	Create a user-friendly interface that displays a menu of available operations.
# ●	Accept user input to choose the desired operation (1-5) or exit (6).
# #### Input Handling:
# ●	Prompt the user to enter numbers for each operation.
# ●	Ensure that the program handles invalid inputs gracefully (e.g., non-numeric inputs).
# #### Result Display:
# ●	Display the result of the selected operation clearly to the user.
# #### Program Loop:
# ●	Implement a loop that allows the user to perform multiple calculations until choosing to exit.
# #### Project Structure:
# ●	Organize your code into functions to encapsulate specific operations.
# ●	Maintain a clear separation between function definitions and the main program.
# #### Error Handling:
# ●	Include error handling for scenarios such as division by zero.
# 	Exiting the Program:
# ●	Provide an option for users to exit the  program.
# 
# 

# In[18]:


#START
class RetailAccounting:
    def __init__(self, hourly_rate):
        self.hourly_rate = hourly_rate
        self.morning_shift_sales = []
        self.evening_shift_sales = []
        self.total_cost_of_items_sold = 0

    def calculate_total_sales(self):
        total_sales = sum(self.morning_shift_sales) + sum(self.evening_shift_sales)
        return total_sales

    def calculate_worker_salary(self, hours_worked):
        worker_salary = self.hourly_rate * hours_worked
        return worker_salary

    def calculate_profit(self):
        total_sales = self.calculate_total_sales()
        profit = total_sales - self.total_cost_of_items_sold
        return profit

    def calculate_tips_for_shift(self, shift_sales):
        tips = 0.02 * sum(shift_sales)
        return tips

    def calculate_total_tips_for_day(self):
        total_tips = self.calculate_tips_for_shift(self.morning_shift_sales) +                      self.calculate_tips_for_shift(self.evening_shift_sales)
        return total_tips

# Creating Function to collect shift sales
def input_shift_sales(shift_name):
    sales = []
    while True:
        try:
            sales_str = input(f"Enter {shift_name} shift sales (Seperate the entries by comma and press Enter, then type 'done' to finish and press enter): ")
            if sales_str.lower() == 'done':
                break
            sales.extend(map(float, sales_str.split(',')))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
    return sales

#Create Function to Collect Total cost of the products
def input_total_cost():
    while True:
        try:
            total_cost = float(input("Enter total cost of items sold: "))
            return total_cost
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            

#Allow user to decide hourly rate            
def input_hourly_rate():
    while True:
        try:
            hourly_rate = float(input("Enter hourly rate: "))
            return hourly_rate
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            

#Creating Function to display Retail Accounting System Menu            
def display_menu():
    print("\n===== Retail Accounting System Menu =====")
    print("1. Calculate Total Sales for the Day")
    print("2. Calculate Worker's Salary")
    print("3. Calculate Profit")
    print("4. Calculate Tips for a Shift")
    print("5. Calculate Total Tips for the Day")
    print("6. Exit")

#Creating Function to allow user navigate around choices
def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Invalid input. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

#Creating Function to get float input
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

#Creating Functions for different accounting computation
def perform_total_sales_calculation(accounting):
    total_sales = accounting.calculate_total_sales()
    print(f"Total Sales for the Day: #{total_sales}")


def perform_worker_salary_calculation(accounting):
    hours_worked = get_float_input("Enter hours worked by the worker: ")
    worker_salary = accounting.calculate_worker_salary(hours_worked)
    print(f"Worker's Salary: #{worker_salary}")


def perform_profit_calculation(accounting):
    profit = accounting.calculate_profit()
    print(f"Profit: #{profit}")


def perform_tips_for_shift_calculation(accounting):
    shift_type = input("Enter shift type (m for morning / e for evening): ").lower()

    if shift_type == "m":
        shift_sales = accounting.morning_shift_sales
        tips_for_shift = accounting.calculate_tips_for_shift(shift_sales)
        print(f"Tips for the Morning Shift: #{tips_for_shift}")
    elif shift_type == "e":
        shift_sales = accounting.evening_shift_sales
        tips_for_shift = accounting.calculate_tips_for_shift(shift_sales)
        print(f"Tips for the Evening Shift: #{tips_for_shift}")
    else:
        print("Invalid shift type. Please enter 'm' or 'e'.")
        return

    

def perform_total_tips_for_day_calculation(accounting):
    total_tips_for_day = accounting.calculate_total_tips_for_day()
    print(f"Total Tips for the Day: #{total_tips_for_day}")


# In[ ]:


# Main program
if __name__ == "__main__":
    print("Retail Accounting System")
    print("Enter Important Values For the Operation")
    hourly_rate = input_hourly_rate()  # Set the hourly rate
    retail_accounting = RetailAccounting(hourly_rate)

    # Input sales data
    retail_accounting.morning_shift_sales = input_shift_sales("morning")
    retail_accounting.evening_shift_sales = input_shift_sales("evening")

    # Input total cost
    retail_accounting.total_cost_of_items_sold = input_total_cost()

    while True:
        display_menu()
        user_choice = get_user_choice()

        if user_choice == 1:
            perform_total_sales_calculation(retail_accounting)
        elif user_choice == 2:
            perform_worker_salary_calculation(retail_accounting)
        elif user_choice == 3:
            perform_profit_calculation(retail_accounting)
        elif user_choice == 4:
            perform_tips_for_shift_calculation(retail_accounting)
        elif user_choice == 5:
            perform_total_tips_for_day_calculation(retail_accounting)
        elif user_choice == 6:
            print("Exiting the Retail Accounting System. Goodbye!")
            break


# In[ ]:




