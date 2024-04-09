import tkinter as tk
from tkinter import ttk, messagebox
# Assuming database_manager.py and plan_manager.py are correctly set up for saving plans
import database_manager

class ManagePlansForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Manage Inspection Plans")
        # Setup UI for managing plans here...
        tk.Label(self, text="This is where you can manage your inspection plans.").pack()

class InspectionPlanForm(tk.Toplevel):
    def __init__(self, parent, update_plan_list_callback):
        super().__init__(parent)
        self.parent = parent
        self.update_plan_list_callback = update_plan_list_callback
        self.title("Create Inspection Plan")
        self.geometry("600x400")
        
        self.part_number_var = tk.StringVar()
        self.part_revision_var = tk.StringVar()
        self.part_description_var = tk.StringVar()
        self.units_var = tk.StringVar()
        
        self.setup_ui()
        
    def setup_ui(self):
        tk.Label(self, text="Part Number:").grid(row=0, column=0, sticky="e")
        tk.Entry(self, textvariable=self.part_number_var).grid(row=0, column=1, sticky="ew")
        
        tk.Label(self, text="Revision:").grid(row=1, column=0, sticky="e")
        tk.Entry(self, textvariable=self.part_revision_var).grid(row=1, column=1, sticky="ew")
        
        tk.Label(self, text="Description:").grid(row=2, column=0, sticky="e")
        tk.Entry(self, textvariable=self.part_description_var).grid(row=2, column=1, sticky="ew")
        
        tk.Label(self, text="Units:").grid(row=3, column=0, sticky="e")
        tk.OptionMenu(self, self.units_var, "inch", "mm").grid(row=3, column=1, sticky="ew")
        
        # Inspection Criteria Section
        self.criteria_frame = ttk.Frame(self)
        self.criteria_frame.grid(row=4, column=0, columnspan=2, sticky="nsew")
        self.setup_criteria_section()
        
        ttk.Button(self, text="Add Dimension", command=self.add_dimension_row).grid(row=5, column=0, columnspan=2, sticky="ew")
        ttk.Button(self, text="Save", command=self.save_inspection_plan).grid(row=6, column=0, columnspan=2, sticky="ew")
        
        self.dimension_rows = []

    def setup_criteria_section(self):
        headers = ["Dimension Type", "Nominal", "Lower Limit", "Upper Limit", "Preferred Method"]
        for i, header in enumerate(headers):
            ttk.Label(self.criteria_frame, text=header).grid(row=0, column=i, padx=5, pady=5)
            
    def add_dimension_row(self):
        row = len(self.dimension_rows) + 1
        dimension_vars = [tk.StringVar() for _ in range(5)]
        self.dimension_rows.append(dimension_vars)
        for i, var in enumerate(dimension_vars):
            ttk.Entry(self.criteria_frame, textvariable=var).grid(row=row, column=i, padx=5, pady=5)
    
    def save_inspection_plan(self):
        part_number = self.part_number_var.get()
        part_revision = self.part_revision_var.get()
        messagebox.showinfo("Save", f"Inspection Plan for {part_number}-{part_revision} saved.")
        self.update_plan_list_callback()
        self.destroy()

class InspectionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inspection Management System")
        self.geometry("800x600")

        self.plan_var = tk.StringVar()

        self.initialize_ui()

    def initialize_ui(self):
        tk.Label(self, text="Select Inspection Plan:").pack(side="top", fill="x", padx=10, pady=5)
        self.plan_dropdown = ttk.Combobox(self, textvariable=self.plan_var, state="readonly")
        self.plan_dropdown['values'] = self.get_inspection_plans()
        self.plan_dropdown.pack(side="top", fill="x", padx=10, pady=5)

        ttk.Button(self, text="Load Inspection Plan", command=self.load_inspection_plan).pack(side="top", fill="x", padx=10, pady=5)

        ttk.Button(self, text="Create Inspection Plan", command=lambda: InspectionPlanForm(self, self.update_inspection_plans_dropdown)).pack(side="top", fill="x", padx=10, pady=5)

        ttk.Button(self, text="Manage Inspection Plans", command=self.manage_inspection_plans).pack(side="top", fill="x", padx=10, pady=5)
        
    def update_inspection_plans_dropdown(self):
        self.plan_dropdown['values'] = self.get_inspection_plans()

    def get_inspection_plans(self):
        plans = database_manager.fetch_all_inspection_plans()
        formatted_plans = [f"{plan[1]} - Rev {plan[2]}" for plan in plans]
        print("Formatted plans for dropdown:", formatted_plans)  # Debug print
        return formatted_plans

    def load_inspection_plan(self):
        selected_plan = self.plan_var.get()
        if not selected_plan:
            messagebox.showerror("Error", "Please select a plan to load.")
            return
        messagebox.showinfo("Info", f"Loading plan: {selected_plan}")

    def create_inspection_plan(self):
        InspectionPlanForm(self, self.update_inspection_plans_dropdown)

    def manage_inspection_plans(self):
        ManagePlansForm(self)

if __name__ == "__main__":
    app = InspectionApp()
    app.mainloop()
