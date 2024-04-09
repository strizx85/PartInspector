CREATE TABLE IF NOT EXISTS inspection_plans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    part_number TEXT NOT NULL,
    part_revision TEXT,
    part_description TEXT,
    pdf_document_path TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS inspection_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_id INTEGER NOT NULL,
    measured_value REAL NOT NULL,
    inspector_name TEXT NOT NULL,
    work_order TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (plan_id) REFERENCES inspection_plans (id)
);
