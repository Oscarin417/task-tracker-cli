from typing import TypedDict, Optional

class TASKINTERFAZ(TypedDict):
    id: str
    descripcion: str
    status: str
    createdAt: str
    updatedAt: Optional[str]
