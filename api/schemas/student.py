from datetime import date

from pydantic import BaseModel, ConfigDict, Field, field_validator


class StudentCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    birthday: date
    phone_number: str = Field(..., min_length=10, max_length=15)
    country: str = Field(..., min_length=1, max_length=100)
    state: str = Field(..., min_length=1, max_length=100)
    city: str = Field(..., min_length=1, max_length=100)
    address: str = Field(..., min_length=1, max_length=255)

    @field_validator("phone_number")
    @classmethod
    def phone_digits_only(cls, v: str) -> str:
        if not v.isdigit():
            raise ValueError("phone_number must contain digits only")
        return v

    @field_validator("birthday")
    @classmethod
    def birthday_not_future(cls, v: date) -> date:
        if v > date.today():
            raise ValueError("birthday cannot be in the future")
        return v


class StudentResponse(StudentCreate):
    model_config = ConfigDict(extra="forbid")

    id: int
