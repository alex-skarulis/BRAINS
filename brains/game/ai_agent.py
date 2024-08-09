from pydantic import BaseModel

class AIAgent(BaseModel):
    name: str
    model: str
    settings: dict

    def take_turn(self, quest):
        # AI logic goes here, using the model and settings
        print(f"{self.name} is taking its turn...")
        # Simulate some decision making
        decision = f"{self.name} completed the task in {quest.title}."
        return decision
