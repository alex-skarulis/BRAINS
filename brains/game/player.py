from pydantic import BaseModel
from typing import List

class Player(BaseModel):
    name: str
    notes: List[str] = []

    def add_notes(self, note: str):
        self.notes.append(note)

    def view_notes(self):
        return "\n".join(self.notes)