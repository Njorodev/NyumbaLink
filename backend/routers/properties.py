from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import get_db
from models import Property, User
from schemas import PropertyCreate, PropertyOut
from dependencies import require_landlord

router = APIRouter(prefix="/api/properties", tags=["Properties"])

@router.get("", response_model=list[PropertyOut])
def list_properties(
    county: Optional[str] = None,
    town: Optional[str] = None,
    property_type: Optional[str] = Query(default=None, alias="type"),
    purpose: Optional[str] = None,
    db: Session = Depends(get_db)
):
    q = db.query(Property).filter(Property.is_available == True)
    if county: q = q.filter(Property.county.ilike(county))
    if town: q = q.filter(Property.town.ilike(town))
    if property_type: q = q.filter(Property.property_type.ilike(property_type))
    if purpose: q = q.filter(Property.purpose == purpose)
    return q.order_by(Property.created_at.desc()).all()

@router.post("", response_model=PropertyOut, status_code=201)
def create_property(payload: PropertyCreate, db: Session = Depends(get_db), landlord: User = Depends(require_landlord)):
    item = Property(**payload.model_dump(), owner_id=landlord.id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/{property_id}", response_model=PropertyOut)
def get_property(property_id: int, db: Session = Depends(get_db)):
    item = db.query(Property).filter(Property.id == property_id).first()
    if not item:
        raise HTTPException(404, "Property not found")
    return item
