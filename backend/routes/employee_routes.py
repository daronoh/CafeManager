from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Employee
from schemas import EmployeeCreate, EmployeeRead
from services import cafe_service, employee_service
from database import get_db
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from pydantic import ValidationError

router = APIRouter()

@router.get("/", response_model=list[EmployeeRead])
def get_employees(cafe_name: str = None, db: Session = Depends(get_db)):
    """Retrieve a list of employees, optionally filtered by cafe name.

    Args:
        cafe (str, optional): The name of the cafe to filter employees by. Defaults to None.
        db (Session): The database session dependency.

    Returns:
        List[dict]: A list of employees, each represented as a dictionary containing:
            - id: Employee ID
            - name: Employee name
            - email_address: Employee email address
            - phone_number: Employee phone number
            - gender: Employee gender
            - cafe_name: Name of the cafe the employee works at
            - days_worked: Number of days the employee has worked since the start date.

    Raises:
        HTTPException: If there is an issue retrieving the employees.
    """
    print(cafe_name)
    cafe = cafe_service.get_cafe_from_name(cafe_name, db)

    query = db.query(Employee)
    if cafe:
        query = query.filter(Employee.cafe_id == cafe.id).filter(Employee.cafe_id.isnot(None))

    employees = query.all()

    response = []
    for employee in employees:
        employee_cafe_name = employee.cafe.name if employee.cafe_id else None
        days_worked = (datetime.today().date() - employee.start_date).days
        response.append({
            "id": employee.id,
            "name": employee.name,
            "email_address": employee.email_address,
            "phone_number": employee.phone_number,
            "gender": employee.gender,
            "cafe_id": employee.cafe_id,
            "cafe_name": employee_cafe_name,
            "days_worked": days_worked 
        })
    
    return response


@router.post("/")
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    """Create a new employee.

    Args:
        employee (EmployeeCreate): The employee data to create a new employee.
        db (Session): The database session dependency.

    Returns:
        dict: A message indicating successful creation.

    Raises:
        HTTPException: If an employee with the same ID already exists or if there are validation issues.
    """
    try:
        employee_id = employee_service.generate_employee_id(db)
        cafe = cafe_service.get_cafe_from_name(employee.cafe_name, db)
        cafe_id = None
        if cafe:
            cafe.increment_employees(db)
            cafe_id = cafe.id

        db_employee = Employee(
            id=employee_id,
            name=employee.name,
            email_address=employee.email_address,
            phone_number=employee.phone_number,
            gender=employee.gender,
            cafe_id=cafe_id,
        )


        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)
        return {
            "message": "Employee created successfully!"
        }

    except IntegrityError as e:
        db.rollback() 
        raise HTTPException(status_code=400, detail="An employee with this ID already exists.")

    except ValidationError as e:
        raise HTTPException(status_code=422, detail="Invalid details")

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")


@router.put("/{employee_id}")
def update_employee(employee_id: str, employee_data: EmployeeCreate, db: Session = Depends(get_db)):
    """Update an existing employee.

    Args:
        employee_id (str): The ID of the employee to update.
        employee_data (EmployeeCreate): The updated employee data.
        db (Session): The database session dependency.

    Returns:
        dict: A message indicating successful update.

    Raises:
        HTTPException: If the employee is not found or if there are validation issues.
    """
    db_employee = employee_service.get_employee_from_id(employee_id, db)
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    try:
        old_cafe_name = db_employee.cafe.name if db_employee.cafe else None
        new_cafe_name = employee_data.cafe_name

        cafe_service.update_cafe_employees(old_cafe_name, new_cafe_name, db)

        if old_cafe_name != new_cafe_name:
            db_employee.reset_employee_days(db)

        new_cafe_id = None
        if employee_data.cafe_name:
            new_cafe_id = cafe_service.get_cafe_from_name(new_cafe_name, db).id
        
        setattr(db_employee, 'cafe_id', new_cafe_id)

        for key, value in employee_data.dict().items():
            if key != 'cafe_name':
                setattr(db_employee, key, value)

        db.commit()
        return {
            "message": "Employee updated successfully!"
        }

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Invalid inputs.")

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")


@router.delete("/{employee_id}")
def delete_employee(employee_id: str, db: Session = Depends(get_db)):
    """Delete an employee by ID.

    Args:
        employee_id (str): The ID of the employee to delete.
        db (Session): The database session dependency.

    Returns:
        dict: A message indicating successful deletion.

    Raises:
        HTTPException: If the employee is not found.
    """
    db_employee = employee_service.get_employee_from_id(employee_id, db)
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    db_employee.cafe.decrement_employees(db)
    db.delete(db_employee)
    db.commit()
    return {"message": "Employee deleted successfully"}