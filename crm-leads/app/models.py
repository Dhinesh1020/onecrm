from pydantic import BaseModel
from typing import Optional

class Lead(BaseModel):
    id: Optional[str] = None
    name: str
    email: str
    phone: Optional[str] = None
    status: Optional[str] = "new"
