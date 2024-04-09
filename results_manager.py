import database_manager

def add_inspection_result(plan_id, measured_value, inspector_name, work_order):
    """
    Add a new inspection result to the database.

    :param plan_id: ID of the inspection plan the result is for.
    :param measured_value: The measured value/result of the inspection.
    :param inspector_name: Name of the inspector who performed the inspection.
    :param work_order: Work order number associated with the inspection.
    """
    database_manager.add_inspection_result(plan_id, measured_value, inspector_name, work_order)

def update_inspection_result(result_id, measured_value):
    """
    Update an existing inspection result.

    :param result_id: ID of the inspection result to update.
    :param measured_value: The new measured value/result to update.
    """
    database_manager.update_inspection_result(result_id, measured_value)

def get_inspection_results_for_plan(plan_id):
    """
    Retrieve all inspection results for a given plan.

    :param plan_id: ID of the inspection plan to get results for.
    :return: List of dictionaries, each representing an inspection result.
    """
    return database_manager.get_inspection_results_for_plan(plan_id)

def delete_inspection_result(result_id):
    """
    Delete an inspection result from the database.

    :param result_id: ID of the inspection result to delete.
    """
    database_manager.delete_inspection_result(result_id)

# Example usage and testing
if __name__ == "__main__":
    # Assume you've added an inspection plan and its ID is 1
    plan_id = 1

    # Adding a new inspection result
    add_inspection_result(plan_id, 0.5, "John Doe", "WO123456")
    print("Added new inspection result.")

    # Assuming you know the result ID is 1, updating that result
    update_inspection_result(1, 0.55)
    print("Updated inspection result.")

    # Fetching and displaying all results for a plan
    results = get_inspection_results_for_plan(plan_id)
    print("Inspection results for plan ID 1:", results)

    # Deleting an inspection result
    delete_inspection_result(1)
    print("Deleted inspection result.")
