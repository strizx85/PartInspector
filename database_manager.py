import sqlite3

DATABASE_PATH = 'inspection_management.db'

def connect_db():
    """Create a database connection."""
    conn = sqlite3.connect(DATABASE_PATH)
    return conn

def create_tables():
    """Create the database tables if they don't already exist."""
    conn = connect_db()
    cursor = conn.cursor()

    # Create table for inspection plans
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS inspection_plans (
        id INTEGER PRIMARY KEY,
        part_number TEXT NOT NULL,
        part_revision TEXT,
        part_description TEXT,
        pdf_document_path TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Create table for inspection results
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS inspection_results (
        id INTEGER PRIMARY KEY,
        plan_id INTEGER NOT NULL,
        measured_value REAL NOT NULL,
        inspector_name TEXT NOT NULL,
        work_order TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (plan_id) REFERENCES inspection_plans(id)
    )
    ''')

    conn.commit()
    conn.close()

# CRUD operations for inspection_plans
def add_inspection_plan(part_number, part_revision, part_description, pdf_document_path):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO inspection_plans (part_number, part_revision, part_description, pdf_document_path)
    VALUES (?, ?, ?, ?)
    ''', (part_number, part_revision, part_description, pdf_document_path))
    conn.commit()
    plan_id = cursor.lastrowid
    conn.close()
    return plan_id

def get_inspection_plan(plan_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inspection_plans WHERE id = ?', (plan_id,))
    plan = cursor.fetchone()
    conn.close()
    return plan

def update_inspection_plan(plan_id, part_number, part_revision, part_description, pdf_document_path):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE inspection_plans
    SET part_number = ?, part_revision = ?, part_description = ?, pdf_document_path = ?
    WHERE id = ?
    ''', (part_number, part_revision, part_description, pdf_document_path, plan_id))
    conn.commit()
    conn.close()

def delete_inspection_plan(plan_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM inspection_plans WHERE id = ?', (plan_id,))
    conn.commit()
    conn.close()

def fetch_all_inspection_plans():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, part_number, part_revision FROM inspection_plans")
    plans = cursor.fetchall()
    conn.close()
    print("Fetched plans:", plans)  # Debug print
    return plans

# Example usage
if __name__ == '__main__':
    create_tables()
    # Add more testing and usage examples as needed
