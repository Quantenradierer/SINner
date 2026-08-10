from pydantic import BaseModel


class Availability(BaseModel):
    value: int
    addition: str = ""
