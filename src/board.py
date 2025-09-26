<<<<<<< Updated upstream
=======
from typing import List, Optional

class Board:
    def __init__(self):
        self.cells: List[str] = [" "] * 9  # indices 0..8

    def render(self) -> str:
        c = self.cells
        rows = [f" {c[0]} | {c[1]} | {c[2]} ",
                "---+---+---",
                f" {c[3]} | {c[4]} | {c[5]} ",
                "---+---+---",
                f" {c[6]} | {c[7]} | {c[8]} "]
        return "\n".join(rows)

    def empty_at(self, pos: int) -> bool:
        return self.cells[pos] == " "

    def place(self, pos: int, mark: str) -> bool:
        if 0 <= pos < 9 and self.empty_at(pos):
            self.cells[pos] = mark
            return True
        return False

    def winner(self) -> Optional[str]:
        lines = [(0,1,2),(3,4,5),(6,7,8),
                 (0,3,6),(1,4,7),(2,5,8),
                 (0,4,8),(2,4,6)]
        for a,b,c in lines:
            if self.cells[a] != " " and self.cells[a] == self.cells[b] == self.cells[c]:
                return self.cells[a]
        return None

    def is_full(self) -> bool:
        return all(c != " " for c in self.cells)

    def copy(self) -> "Board":
        b = Board()
        b.cells = self.cells[:]
        return b
>>>>>>> Stashed changes

