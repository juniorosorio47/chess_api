from rest_framework import serializers
from .models import Pawn, Queen, Bishop, King, Knight, Rook, Piece



class PawnSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pawn
        fields = '__all__'

class QueenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Queen
        fields = '__all__'

class KingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = King
        fields = '__all__'

class BishopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bishop
        fields = '__all__'

class KnightSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Knight
        fields = '__all__'

class RookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rook
        fields = '__all__'

class PieceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Piece
        fields = '__all__'
