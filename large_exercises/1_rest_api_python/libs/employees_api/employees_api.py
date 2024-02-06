"""
Low level keywords for the employees REST API
"""
import json
from http import HTTPStatus
from typing import Optional
from generated.employees_openapi_client import Client
from generated.employees_openapi_client.api.employee_controller import find_all
from generated.employees_openapi_client.api.employee_controller import find_one

api_client = Client("http://158.101.191.70:8085")


def get_all_employees():
    """
    Returns all employees as a list of dictionaries {_id_ : _first name_ + _last name_}
    """
    response = find_all.sync_detailed(client=api_client)
    assert response.status_code == HTTPStatus.OK
    return_dict = {}
    response_content = json.loads(response.content)
    for employee in response_content["content"]:
        return_dict[employee["id"]] = f"{employee['firstName']} {employee['lastName']}"
    return return_dict


def get_employee_data(employee_id):
    """
    Returns all data of an employee with the given `employee_id` as a dictionary:
    - First Name
    - Last Name
    - Role
    """
    response = find_one.sync_detailed(id=employee_id, client=api_client)
    assert response.status_code == HTTPStatus.OK
    response_content = json.loads(response.content)
    return response_content
    


def update_employee_data(
    employee_id,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    role: Optional[str] = None,
):
    """
    Updates data of an employee with the given `employee_id` according to the values provided.
    All params except _employee_id_ are optional -
    the data won't be updated if no value is provided.
    """
    raise NotImplementedError("Looking for a student to implement me!")


def create_employee(employee_id, first_name, last_name, role):
    """
    Creates a new employee with the given values
    """
    raise NotImplementedError("Looking for a student to implement me!")

# For debugging only
if __name__ == '__main__':
    everyone = get_all_employees()
    print(everyone)
    someone = get_employee_data(sorted(everyone)[0])
    print(someone)
    old_first_name = someone["firstName"]
    new_first_name = "Gandalf"
    update_employee_data(someone["id"], first_name=new_first_name)
    assert get_employee_data(someone["id"])["firstName"] == new_first_name
    update_employee_data(someone["id"], first_name=old_first_name)
    create_employee(sorted(everyone)[-1] + 1, "Gandalf", "The Gray", "Wizard")
