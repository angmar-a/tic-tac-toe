from .board import Board

class Game:
    def __init__(self, p1, p2):
        self.board = Board()
        self.players = [p1, p2]
        self.turn = 0  # index into players

    def play(self):
        while True:
            print("\n" + self.board.render())
            player = self.players[self.turn]
            pos = player.move(self.board)
            self.board.place(pos, player.mark)

            w = self.board.winner()
            if w:
                print("\n" + self.board.render())
                print(f"\n{player.name} ({w}) wins!")
                return
            if self.board.is_full():
                print("\n" + self.board.render())
                print("\nIt's a draw!")
                return

            self.turn = 1 - self.turn