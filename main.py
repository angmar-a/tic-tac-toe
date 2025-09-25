from src.player import Human
from src.game import Game
from src.ai import AI

def prompt_choice(prompt, choices):
    choices_lower = {c.lower(): c for c in choices}
    while True:
        ans = input(f"{prompt} {choices} > ").strip().lower()
        if ans in choices_lower:
            return ans
        print(f"Please choose one of {choices}.")

def prompt_yes_no(prompt):
    while True:
        ans = input(f"{prompt} [y/n] > ").strip().lower()
        if ans in {"y","yes"}: return True
        if ans in {"n","no"}: return False
        print("Type y or n.")

def choose_marks(p1_name="Player 1", p2_name="Player 2"):
    pick = prompt_choice(f"{p1_name}, pick your mark (X goes first):", ["X","O"])
    if pick == "x":
        return ("X", "O"), 0  # p1 is X, starts
    else:
        return ("O", "X"), 1  # p2 is X, starts

def print_positions_guide():
    print("Tic-Tac-Toe — positions 1..9:")
    print(" 1 | 2 | 3 \n---+---+---\n 4 | 5 | 6 \n---+---+---\n 7 | 8 | 9 ")

def main():
    print_positions_guide()

    mode = prompt_choice("Choose mode:", ["HUMANvsHUMAN","HUMANvsAI"])
    if mode == "humanvsai":
        you_first = prompt_yes_no("Do you want to go first (play as X)?")
        if you_first:
            p1 = Human("You", "X")
            p2 = AI("O")
            start_idx = 0
        else:
            p1 = AI("X")
            p2 = Human("You", "O")
            start_idx = 0  # X always starts; our p1 is X
    else:
        # HUMAN vs HUMAN
        names = [input("Enter name for Player 1: ").strip() or "Player 1",
                 input("Enter name for Player 2: ").strip() or "Player 2"]
        (m1, m2), start_idx = choose_marks(names[0], names[1])
        p1 = Human(names[0], m1)
        p2 = Human(names[1], m2)

    game = Game(p1, p2)
    # Ensure the X-player starts (Game starts with index 0)
    # If our X isn't at index 0, swap the order.
    if game.players[0].mark != "X":
        game.players[0], game.players[1] = game.players[1], game.players[0]

    game.play()

if __name__ == "__main__":
    main()