from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import Cafe
from schemas import CafeCreate, CafeRead
from database import get_db

router = APIRouter()

@router.get("/", response_model=list[CafeRead])
def get_cafes(location: str = None, db: Session = Depends(get_db)):
    """Retrieve a list of cafes.

    Args:
        location (str, optional): Filter cafes by location. If provided, only cafes in this location will be returned.
        db (Session): Database session dependency.

    Returns:
        List[CafeRead]: A sorted list of cafes, sorted by the number of employees in descending order.

    Raises:
        HTTPException: If there is an issue retrieving the cafes.
    """
    query = db.query(Cafe)
    if location:
        query = query.filter(Cafe.location == location)
    cafes = query.all()
    return sorted(cafes, key=lambda x: x.employees, reverse=True)


@router.post("/")
def create_cafe(cafe: CafeCreate, db: Session = Depends(get_db)):
    """Create a new cafe.

    Args:
        cafe (CafeCreate): The cafe data to create a new cafe.
        db (Session): Database session dependency.

    Returns:
        dict: A message indicating successful creation.

    Raises:
        HTTPException: If a cafe with the same name already exists.
    """
    db_cafe = Cafe(**cafe.dict(), employees=0)
    db.add(db_cafe)
    try:
        db.commit()
        db.refresh(db_cafe)
        return {
            "message": "Cafe created successfully!"
        }
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="A cafe with this name already exists.")


@router.put("/{cafe_id}")
def update_cafe(cafe_id: str, cafe: CafeCreate, db: Session = Depends(get_db)):
    """Update an existing cafe.

    Args:
        cafe_id (str): The ID of the cafe to update.
        cafe (CafeCreate): The updated cafe data.
        db (Session): Database session dependency.

    Returns:
        dict: A message indicating successful update.

    Raises:
        HTTPException: If the cafe is not found or if a cafe with the same name already exists.
    """
    db_cafe = db.query(Cafe).filter(Cafe.id == cafe_id).first()
    if not db_cafe:
        raise HTTPException(status_code=404, detail="Cafe not found")

    try:
        for key, value in cafe.dict().items():
            setattr(db_cafe, key, value)
        db.commit()
        return {"message": "Cafe updated successfully!"}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="A cafe with this name already exists.")


@router.delete("/{cafe_id}")
def delete_cafe(cafe_id: str, db: Session = Depends(get_db)):
    """Delete a cafe by ID.

    Args:
        cafe_id (str): The ID of the cafe to delete.
        db (Session): Database session dependency.

    Returns:
        dict: A message indicating successful deletion.

    Raises:
        HTTPException: If the cafe is not found.
    """
    db_cafe = db.query(Cafe).filter(Cafe.id == cafe_id).first()
    if not db_cafe:
        raise HTTPException(status_code=404, detail="Cafe not found")
    
    db.delete(db_cafe)
    db.commit()
    return {"message": "Cafe deleted successfully!"}