# BRAINS: Business Role-Playing and AI Networking Simulation

**BRAINS** is a command-line application that blends elements of a turn-based multiplayer role-playing game, a note-taking application, and a project management/ticketing system. Inspired by classic games like Zork, War Games, and Dungeons & Dragons, BRAINS is designed to provide an engaging, text-based simulation experience for both human players and AI agents.

## Current Status

🚧 **This project is in very early development.** Core features are still being designed and implemented. We welcome contributions and feedback as we build out the application.

## Features

- **Quest System:** Define and manage quests with dependencies, acceptance criteria, and associated notes.
- **Turn-Based Gameplay:** Players take turns to progress through quests, with AI agents capable of taking over when needed.
- **Character Sheets:** Players and AI agents have their own character sheets, guiding their role-playing decisions.
- **AI Integration:** AI agents are powered by models defined in their character sheets, with the ability to autonomously complete quests.

Usage
Start the game with:

bash
Copy code
python -m brains.cli --start --player <your_name>
Example:

bash
Copy code
python -m brains.cli --start --player "Alex"
Development
Repository Structure
brains/: Core application code.
tests/: Unit tests.
docs/: Documentation and design notes.
Key Python Packages
argparse: Command-line argument parsing.
fastapi: API framework (planned for future expansion).
httpx: HTTP client (planned for future expansion).
jmespath: JSON querying.
openai: AI integration.
pydantic: Data validation and management.
ujson: Fast JSON processing.
uvicorn: ASGI server (planned for future expansion).
Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

### License

This project is licensed under the GNU GENERAL PUBLIC LICENSE.

### Next Steps

1. **Implement the CLI Game Loop**: Start building out the main game loop in `cli.py`, where players take turns.
2. **Enhance AI Logic**: Develop the logic for AI agents in `ai_agent.py` to interact with quests and make decisions.
3. **Test and Iterate**: Begin writing unit tests in the `tests/` directory to ensure the game’s functionality.