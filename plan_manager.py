import database_manager

def add_inspection_plan(part_number, part_revision, part_description, pdf_document_path):
    """
    Add a new inspection plan to the database.

    :param part_number: The part number for the inspection plan.
    :param part_revision: The revision of the part for the inspection plan.
    :param part_description: A description of the part.
    :param pdf_document_path: The path to the PDF document associated with the plan.
    :return: The ID of the newly created inspection plan.
    """
    return database_manager.add_inspection_plan(part_number, part_revision, part_description, pdf_document_path)

def update_inspection_plan(plan_id, part_number, part_revision, part_description, pdf_document_path):
    """
    Update an existing inspection plan.

    :param plan_id: The ID of the inspection plan to update.
    :param part_number: The updated part number for the inspection plan.
    :param part_revision: The updated revision of the part.
    :param part_description: The updated description of the part.
    :param pdf_document_path: The updated path to the PDF document.
    """
    database_manager.update_inspection_plan(plan_id, part_number, part_revision, part_description, pdf_document_path)

def get_inspection_plan(plan_id):
    """
    Retrieve an inspection plan based on its ID.

    :param plan_id: The ID of the inspection plan to retrieve.
    :return: A dictionary with the inspection plan details, or None if not found.
    """
    return database_manager.get_inspection_plan(plan_id)

def delete_inspection_plan(plan_id):
    """
    Delete an inspection plan from the database.

    :param plan_id: The ID of the inspection plan to delete.
    """
    database_manager.delete_inspection_plan(plan_id)

def list_all_inspection_plans():
    """
    List all inspection plans.

    :return: A list of dictionaries, each representing an inspection plan's details.
    """
    return database_manager.list_all_inspection_plans()

# Example usage:
if __name__ == "__main__":
    # Example of adding a new plan
    plan_id = add_inspection_plan('001', 'A', 'Widget', '/path/to/document.pdf')
    print(f"Added new inspection plan with ID: {plan_id}")

    # Fetching and displaying a plan
    plan = get_inspection_plan(plan_id)
    print(f"Retrieved plan: {plan}")

    # Updating a plan
    update_inspection_plan(plan_id, '002', 'B', 'Updated Widget Description', '/new/path/to/document.pdf')
    print("Updated inspection plan.")

    # Listing all plans
    all_plans = list_all_inspection_plans()
    print("All inspection plans:", all_plans)

    # Deleting a plan
    delete_inspection_plan(plan_id)
    print(f"Deleted inspection plan with ID: {plan_id}")
