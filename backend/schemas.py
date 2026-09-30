from typing import Literal, Optional
from pydantic import BaseModel, EmailStr, Field, ConfigDict, computed_field, model_validator


# --- USER SCHEMAS ---

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
    phone: Optional[str] = None
    role: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserOut


# --- PROPERTY SCHEMAS ---

class PropertyCreate(BaseModel):
    title: str
    property_type: str
    purpose: Literal["rent", "land"]
    county: str
    town: str
    price: float = Field(gt=0)
    total_units: int = Field(default=1, ge=1)
    available_units: int = Field(default=1, ge=0)
    description: Optional[str] = None
    image_url: Optional[str] = None

    @model_validator(mode="after")
    def validate_units(self):
        if self.available_units > self.total_units:
            raise ValueError("Available units cannot be greater than total units.")
        return self


class PropertyOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    property_type: str
    purpose: str
    county: str
    town: str
    price: float
    total_units: int
    available_units: int
    description: Optional[str] = None
    image_url: Optional[str] = None
    is_available: bool
    owner_id: int

    # 🔹 Add owner relationship field so Pydantic captures it from ORM
    owner: Optional[UserOut] = None

    # 🔹 Now self.owner references the nested UserOut Pydantic model!
    @computed_field
    def owner_name(self) -> str:
        if self.owner:
            return f"{self.owner.first_name} {self.owner.last_name}"
        return "Landlord"

    @computed_field
    def owner_email(self) -> Optional[str]:
        if self.owner:
            return self.owner.email
        return None

    @computed_field
    def owner_phone(self) -> Optional[str]:
        if self.owner:
            return self.owner.phone
        return None