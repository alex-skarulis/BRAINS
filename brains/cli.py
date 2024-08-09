import argparse
from brains.game.quest import Quest
from brains.game.player import Player
from brains.game.ai_agent import AIAgent

def main():
    parser = argparse.ArgumentParser(description="BRAINS: Business Role-Playing and AI Networking Simulation")
    parser.add_argument('--start', action='store_true', help="Start the game")
    parser.add_argument('--player', type=str, help="Player name")
    args = parser.parse_args()

    if args.start:
        if args.player:
            player = Player(name=args.player)
            print(f"Welcome, {player.name}. Your quest begins!")
            # Start the game loop here
        else:
            print("Please provide a player name using --player <name>")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
