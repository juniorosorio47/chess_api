from django.db import models

class Piece(models.Model):

    color = models.CharField(max_length=10)
    key = models.CharField(max_length=1)
    name = models.CharField(max_length=20)

    class Meta:
        abstract:True

class King(Piece):

    def create(self, color):
        self.name = "king"
        self.key = 'k'
        super(color)

class Queen(Piece):

    def create(self, color):
        self.name = "queen"
        self.key = 'q'
        super(color)

class Knight(Piece):

    def create(self, color):
        self.name = "knight"
        self.key = 'n'
        super(color)

class Pawn(Piece):

    def create(self, color):
        self.name = "pawn"
        self.key = 'p'
        super(color)

class Bishop(Piece):

    def create(self, color):
        self.name = "bishop"
        self.key = 'b'
        super(color)

class Rook(Piece):

    def create(self, color):
        self.name = "bishop"
        self.key = 'b'
        super(color)
