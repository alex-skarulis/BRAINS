import uuid
from pydantic import BaseModel, Field
from typing import List, Optional

class Quest(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    dependencies: Optional[List[str]] = None
    acceptance_criteria: Optional[List[str]] = None

    def is_ready_to_start(self, completed_quests):
        if not self.dependencies:
            return True
        return all(dep in completed_quests for dep in self.dependencies)