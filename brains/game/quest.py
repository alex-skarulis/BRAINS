try:
    from pydantic import BaseModel, Field, field_validator
    from typing import List, Optional
    import uuid
except ImportError as e:
    print("Error importing modules: {e}")
    exit(1)

class Quest(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    dependencies: Optional[List[str]] = None
    acceptance_criteria: Optional[List[str]] = None

    @field_validator('title', 'description')
    def check_title_description(cls, values):
        title, description = values
        if not title and not description:
            raise ValueError('Title and description cannot be empty')
        return values
    
    

    def is_ready_to_start(self, completed_quests):
        if not self.dependencies:
            return True
        return all(dep in completed_quests for dep in self.dependencies)