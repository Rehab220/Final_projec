import tkinter as tk
from tkinter import messagebox
import re
class Projects:
    def __init__(self, project_name,start_date,end_date,Plocation,branches):
        self.project_name = project_name
        self.start_date = start_date
        self.end_date = end_date
        self.Plocation = Plocation
        self.branches = branches

    def display_info(self):
        return f"Project: {self.project_name}\nStart_Date: {self.start_date}\nend_Date: {self.end_date}\nPlocation: {self.Plocation}\nbranches: {self.branches}"

    projects_data = []
    file= open("projects_data.txt", "r")
    FP = file.readlines()
    a=True
    for i in FP:
        if a:
            a=False
            continue
        values = i.strip().split(",")
        project_data = {
            "project_name": values[0],
            "start_date": values[1],
            "end_date": values[2],
            "Plocation": values[3],
            "branches": values[4]
        }
        projects_data.append(project_data)
    print(projects_data)
    print("\n" + "-" * 25 + "\n")
    file.close()
class Branches(Projects):
    def __init__(self, project_name,start_date,end_date,Plocation,branches,branch_name,branch_id,supervisor):
        super().__init__(project_name,start_date,end_date,Plocation,branches)
        self.branch_name = branch_name
        self.branch_id = branch_id
        self.supervisor = supervisor

    def display_info(self):
        return f"Branch: {self.branch_name}\nbranch_id: {self.branch_id}\nsupervisor: {self.supervisor}\n{super().display_info()}"

class Workers(Projects):
    def __init__(self, project_name,start_date,end_date,Plocation,branches,worker_name,department,salary):
        super().__init__(project_name,start_date,end_date,Plocation,branches)
        self.worker_name = worker_name
        self.department = department
        self.salary = salary

    def display_info(self):
        return f"Worker: {self.worker_name}\n{super().display_info()}\ndepartment: {self.department}\nsalary: {self.salary}"

class Tasks(Projects):
    def __init__(self, project_name,start_date,end_date,Plocation,branches,task_name,status):
        super().__init__(project_name,start_date,end_date,Plocation,branches)
        self.task_name = task_name
        self.status = status

    def calculate_total_budget(self):
        expenses =float(input("Enter additional expenses: "))
        initial_budget = float(input("Enter Initial_Budget: "))
        total_budget = initial_budget - expenses
        print(total_budget)

    def display_info(self):
        return f"Task: {self.task_name}\n{super().display_info()}\nStatus: {self.status}"

class EmployeeRegistration:
        def __init__(self, root):
            self.root = root
            self.root.title("Employee Registration")

            self.worker_name = tk.StringVar()
            self.department = tk.StringVar()
            self.email= tk.StringVar()
            self.password = tk.StringVar()

            worker_name_label = tk.Label(root, text="Worker Name:", width=25)
            worker_name_entry = tk.Entry(root, textvariable=self.worker_name, bg="#ddebf9", width=25, bd=2)

            department_label = tk.Label(root, text="Department:", width=25)
            department_entry = tk.Entry(root, textvariable=self.department, bg="#ddebf9", width=25, bd=2)

            email_label = tk.Label(root, text="Email:", width=25)
            email_entry = tk.Entry(root, textvariable=self.email, bg="#ddebf9", width=25, bd=2)

            password_label = tk.Label(root, text="Password:", width=25)
            password_entry = tk.Entry(root, textvariable=self.password, show="*", bg="#ddebf9", width=25, bd=2)

            submit_button = tk.Button(root, text="Submit", bg="#70aeee", width=25, command=self.submit)

            worker_name_label.pack()
            worker_name_entry.pack()
            department_label.pack()
            department_entry.pack()
            email_label.pack()
            email_entry.pack()
            password_label.pack()
            password_entry.pack()
            submit_button.pack()

        def submit(self):
            worker_name = self.worker_name.get()
            department = self.department.get()
            email = self.email.get()
            password = self.password.get()

            if not re.match(r'^[a-zA-Z ]+$', worker_name):
                messagebox.showinfo('Error', 'Invalid worker name format')

            if not re.match(r'^[a-zA-Z ]+$', department):
                messagebox.showinfo('Error', 'Invalid department format')

            if not re.match(r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$', email):
                messagebox.showinfo('Error', 'Invalid email format')

            if not re.match(r'^[a-zA-Z0-9]+$', password):
                messagebox.showinfo('Error', 'Invalid password format')
            else:
                messagebox.showinfo("Employee registered successfully.")


task_1 = Tasks(project_name="Advanced architecture", start_date="1/1/2023", end_date="31/12/2027",
                   Plocation="Amman", branches="khalda", task_name="ESM", status="Under Review")
task_2 = Tasks(project_name="Sustainable cities", start_date="17/8/2020", end_date="3/12/2022", Plocation="Amman",
                   branches="Abdoun", task_name="Green Space Design", status="In Progress")
task_1.calculate_total_budget()
task_2.calculate_total_budget()

project_1 = Projects(project_name="Advanced architecture", start_date="1/1/2023", end_date="31/12/2027", Plocation="Amman", branches="khalda")
project_2 = Projects(project_name="Sustainable cities", start_date="17/8/2020", end_date="3/12/2022", Plocation="Amman", branches="Abdoun")

branch_1 = Branches(project_name="Advanced architecture", start_date="1/1/2023", end_date="31/12/2027", Plocation="Amman", branches="khalda", branch_name="BIM", branch_id="B001", supervisor="John")
branch_2 = Branches(project_name="Sustainable cities", start_date="17/8/2020", end_date="3/12/2022", Plocation="Amman", branches="Abdoun", branch_name="EED", branch_id=" A003", supervisor="Omar")

worker_1 = Workers(project_name="Advanced architecture", start_date="1/1/2023", end_date="31/12/2027", Plocation="Amman", branches="khalda",worker_name="Ali", department="Facility Management", salary="5000")
worker_2 = Workers(project_name="Sustainable cities", start_date="17/8/2020", end_date="3/12/2022", Plocation="Amman", branches="Abdoun",worker_name="Sammer", department="Ecological Design", salary="9000")

# Display information
print(branch_1.display_info())
print("\n" + "-" * 25 + "\n")
print(worker_1.display_info())
print("\n" + "-" * 25 + "\n")
print(task_1.display_info())

root = tk.Tk()
registration = EmployeeRegistration(root)
root.geometry("400x400")
root.mainloop()

