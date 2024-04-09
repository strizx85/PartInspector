from database_manager import create_tables
from gui import InspectionApp

def main():
    # Initialize the database by creating tables if they don't already exist.
    create_tables()
    
    # Launch the GUI application.
    app = InspectionApp()
    app.mainloop()

if __name__ == "__main__":
    main()
