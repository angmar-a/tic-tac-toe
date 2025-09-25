class Human:
    def __init__(self, name: str, mark: str):
        self.name = name
        self.mark = mark

    def move(self, board) -> int:
        while True:
            try:
                raw = input(f"{self.name} ({self.mark}) - choose 1-9: ").strip()
                pos = int(raw) - 1  # Convert to 0-8 index
                if 0 <= pos < 9 and board.empty_at(pos):
                    return pos
            except ValueError:
                pass
            print("Invalid move. Pick an empty square 1-9.")
