from typing import Optional, Literal
from pydantic import BaseModel, EmailStr, Field, ConfigDict

class UserCreate(BaseModel):
    first_name: str = Field(min_length=2, max_length=80)
    last_name: str = Field(min_length=2, max_length=80)
    email: EmailStr
    phone: Optional[str] = Field(default=None, max_length=30)
    password: str = Field(min_length=8, max_length=128)
    role: Literal["landlord", "seeker"]

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str]
    role: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserOut

class PropertyCreate(BaseModel):
    title: str
    property_type: str
    purpose: Literal["rent", "land"]
    county: str
    town: str
    price: float = Field(gt=0)
    description: Optional[str] = None
    image_url: Optional[str] = None

class PropertyOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    property_type: str
    purpose: str
    county: str
    town: str
    price: float
    description: Optional[str]
    image_url: Optional[str]
    is_available: bool
    owner_id: int
