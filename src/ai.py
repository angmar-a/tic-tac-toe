from typing import Optional, Tuple
from .board import Board

SCORES = {
    "X":  1,   # X wins
    "O": -1,   # O wins
    "draw": 0
}

class AI:
    def __init__(self, mark: str):
        assert mark in {"X", "O"}
        self.mark = mark
        self.opponent = "O" if mark == "X" else "X"

    def move(self, board: Board) -> int:
        best_score = float("-inf") if self.mark == "X" else float("inf")
        best_move: Optional[int] = None

        # Try all legal moves
        for pos in range(9):
            if board.empty_at(pos):
                b2 = board.copy()
                b2.place(pos, self.mark)
                score = self._minimax(b2, maximizing=(self.opponent == "X"),
                                      alpha=float("-inf"), beta=float("inf"))

                # X maximizes, O minimizes
                if self._is_better(score, best_score):
                    best_score, best_move = score, pos

        # Fallback (shouldn’t happen): first empty
        if best_move is None:
            for pos in range(9):
                if board.empty_at(pos):
                    return pos
        return best_move  # type: ignore

    # ---------- internals ----------

    def _terminal_score(self, board: Board) -> Optional[int]:
        w = board.winner()
        if w is not None:
            # score from X's perspective, then flip if AI is O
            base = SCORES[w]
            return base if self.mark == "X" else -base
        if board.is_full():
            return SCORES["draw"]
        return None

    def _minimax(self, board: Board, maximizing: bool, alpha: float, beta: float) -> int:
        term = self._terminal_score(board)
        if term is not None:
            return term

        if maximizing:
            best = float("-inf")
            # maximizing player is X in standard scoring
            current_mark = "X"
            for pos in range(9):
                if board.empty_at(pos):
                    b2 = board.copy()
                    b2.place(pos, current_mark)
                    score = self._minimax(b2, maximizing=False, alpha=alpha, beta=beta)
                    best = max(best, score)
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
            return int(best)
        else:
            best = float("inf")
            # minimizing player is O in standard scoring
            current_mark = "O"
            for pos in range(9):
                if board.empty_at(pos):
                    b2 = board.copy()
                    b2.place(pos, current_mark)
                    score = self._minimax(b2, maximizing=True, alpha=alpha, beta=beta)
                    best = min(best, score)
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
            return int(best)

    def _is_better(self, score: int, best_score: float) -> bool:
        # If AI is X, higher is better; if AI is O, lower is better.
        if self.mark == "X":
            return score > best_score
        else:
            return score < best_score
