from pydantic import BaseModel, Field
from typing import List

class EntityOutput(BaseModel):
    drug: str = Field(description="Name of the drug")
    events: List[str] = Field(description="List of adverse events")
    severity: str = Field(description="low, medium, or high")
    hospitalization: bool = Field(description="whether hospitalization occurred")
    timeline: str = Field(description="time reference like last week")