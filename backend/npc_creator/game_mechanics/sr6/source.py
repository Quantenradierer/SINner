from pydantic import BaseModel


class Source(BaseModel):
    page: int
    book: str
