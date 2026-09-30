from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session, joinedload

from database import get_db
from dependencies import require_landlord
from models import Property, User
from schemas import PropertyCreate, PropertyOut

router = APIRouter(prefix="/api/properties", tags=["Properties"])


@router.get("", response_model=list[PropertyOut])
def list_properties(
    county: Optional[str] = None,
    town: Optional[str] = None,
    property_type: Optional[str] = Query(default=None, alias="type"),
    purpose: Optional[str] = None,
    db: Session = Depends(get_db),
):
    # 🔹 Use joinedload(Property.owner) to eager-load the User relationship
    q = db.query(Property).options(joinedload(Property.owner)).filter(Property.is_available == True)

    if county:
        q = q.filter(Property.county.ilike(f"%{county}%"))
    if town:
        q = q.filter(Property.town.ilike(f"%{town}%"))
    if property_type:
        q = q.filter(Property.property_type.ilike(f"%{property_type}%"))
    if purpose:
        q = q.filter(Property.purpose == purpose)

    return q.order_by(Property.created_at.desc()).all()


@router.post("", response_model=PropertyOut, status_code=201)
def create_property(
    payload: PropertyCreate,
    db: Session = Depends(get_db),
    landlord: User = Depends(require_landlord),
):
    # 🔹 Assign foreign key `owner_id`
    item = Property(**payload.model_dump(), owner_id=landlord.id)
    db.add(item)
    db.commit()

    # 🔹 Re-query the created item with `joinedload(Property.owner)` so Pydantic has access to `self.owner`
    new_property = (
        db.query(Property)
        .options(joinedload(Property.owner))
        .filter(Property.id == item.id)
        .first()
    )

    return new_property