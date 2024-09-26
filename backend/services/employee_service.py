from sqlalchemy.orm import Session
from models import Employee
from typing import Optional
import random
import string

class employee_service:

    @staticmethod
    def check_employee_id_exists(employee_id: str, db: Session) -> bool:
        """Check if the employee ID already exists in the database.

        Args:
            employee_id (str): The employee ID to check.
            db (Session): The database session used for querying.

        Returns:
            bool: True if the employee ID exists; False otherwise.
        """
        exists = db.query(Employee).filter(Employee.id == employee_id).first() is not None
        return exists

    @staticmethod
    def generate_employee_id(db: Session) -> str:
        """Generate a unique employee ID.

        The ID is prefixed with 'UI' followed by a random alphanumeric suffix of 7 characters.
        It ensures that the generated ID does not already exist in the database.

        Args:
            db (Session): The database session used for querying.

        Returns:
            str: A unique employee ID.
        """
        prefix = 'UI'
        while True:
            random_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
            employee_id = f"{prefix}{random_suffix}"
            if not employee_service.check_employee_id_exists(employee_id, db):
                return employee_id

    @staticmethod
    def get_employee_from_id(employee_id: str, db: Session) -> Optional[Employee]:
        """Retrieve an employee from the database by their ID.

        Args:
            employee_id (str): The ID of the employee to retrieve.
            db (Session): The database session used for querying.

        Returns:
            Optional[Employee]: The Employee object if found; None if not found.
        """
        return db.query(Employee).filter(Employee.id == employee_id).first()

