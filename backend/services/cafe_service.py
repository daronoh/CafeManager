from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Cafe
from typing import Optional

class cafe_service:
    @staticmethod
    def get_cafe_from_name(name: Optional[str], db: Session) -> Optional[Cafe]:
        """Retrieve the ID of a cafe by its name.

        Args:
            name (Optional[str]): The name of the cafe to look up.
            db (Session): The database session used for querying.

        Returns:
            Optional[str]: The ID of the cafe if found; None if name is not provided.

        Raises:
            HTTPException: If the cafe with the specified name does not exist.
        """

        if not name:
            return None
        
        cafe = db.query(Cafe).filter(Cafe.name == name).first()
        if cafe:
            return cafe
        else:
            raise HTTPException(status_code=404, detail="Cafe not found")
        
    @staticmethod
    def update_cafe_employees(old_cafe_name: Optional[str], new_cafe_name: Optional[str], db: Session):
        """
        Update the employee counts for cafes when an employee changes from one cafe to another.

        This method retrieves the cafes corresponding to the provided names, and if they are different,
        it adjusts the employee counts by decrementing the count for the old cafe and incrementing it 
        for the new cafe.

        Parameters:
        - old_cafe_name (Optional[str]): The name of the cafe from which the employee is moving. 
        If None, no decrement action is performed.
        - new_cafe_name (Optional[str]): The name of the cafe to which the employee is moving. 
        If None, no increment action is performed.
        - db (Session): The database session used to perform operations on the cafes.

        Returns:
        - None: This method does not return a value.

        Raises:
            HTTPException: If the cafe with the specified name does not exist.
        """
        old_cafe = cafe_service.get_cafe_from_name(old_cafe_name, db)
        new_cafe = cafe_service.get_cafe_from_name(new_cafe_name, db)

        if old_cafe != new_cafe:
            if old_cafe:
                old_cafe.decrement_employees(db)
            if new_cafe:
                new_cafe.increment_employees(db)




