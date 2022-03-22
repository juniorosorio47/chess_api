from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Piece
from .serializers import (BishopSerializer, KingSerializer, KnightSerializer,
                          PawnSerializer, PieceSerializer, QueenSerializer,
                          RookSerializer)
from .utils import (bishop_possible_movements, convert_coordinates_to_numeric,
                    generate_board, get_piece, king_possible_movements,
                    knight_possible_movements, pawn_possible_movements,
                    queen_possible_movements, rook_possible_movements)


@api_view(['POST'])
def create_piece(request):
    piece_color = request.data['color'].lower()
    piece_type = request.data['type'].lower()

    piece = get_piece(piece_type)

    if not piece:
        return Response(
            data={ 'error': 'Type not found!' },
            status=status.HTTP_404_NOT_FOUND)

    if piece_color != 'black' and piece_color != 'white':
        return Response(
            data={ 'error': 'Color not valid! The color should be white or black.' },
            status=status.HTTP_404_NOT_FOUND)

    if piece.get('key') == 'p':
        print('This is a Pawn')

        new_pawn = {
            'key': piece.get('key'),
            'name': piece.get('type'),
            'color': piece_color
        }

        serializer = PawnSerializer(data= new_pawn)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    elif piece.get('key') == 'q':
        print('This is a Queen')

        new_queen = {
            'key': piece.get('key'),
            'name': piece.get('type'),
            'color': piece_color
        }

        serializer = QueenSerializer(data= new_queen)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    elif piece.get('key') == 'k':
        print('This is a King')

        new_king = {
            'key': piece.get('key'),
            'name': piece.get('type'),
            'color': piece_color
        }

        serializer = KingSerializer(data=new_king)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    elif piece.get('key') == 'n':
        print('This is a Knight')

        new_knight = {
            'key': piece.get('key'),
            'name': piece.get('type'),
            'color': piece_color
        }

        serializer = KnightSerializer(data=new_knight)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif piece.get('key') == 'b':
        print('This is a Bishop')

        new_bishop = {
            'key': piece.get('key'),
            'name': piece.get('type'),
            'color': piece_color
        }

        serializer = BishopSerializer(data=new_bishop)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif piece.get('key') == 'r':
        print('This is a Rook')

        new_rook = {
            'key': piece.get('key'),
            'name': piece.get('type'),
            'color': piece_color
        }

        serializer = RookSerializer(data=new_rook)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def get_possible_movements(request):
    # Get request data
    piece_id = request.data['piece_id']
    # coordinate = [char for char in request.data['coordinate']]
    coordinate = request.data['coordinate'].lower()

    if not len(coordinate)==2:
        return Response(
            data={ 'error': 'Invalid coordinate string' },
            status=status.HTTP_400_BAD_REQUEST)

    # Generate the board
    board = generate_board(8)

    # Converts the coordinates
    converted_coordinate = convert_coordinates_to_numeric(board, coordinate)


    second_turn = []

    try:
        find_piece = Piece.objects.get(pk=piece_id)
        piece = PieceSerializer(find_piece)
        
        if piece.data['key']=='k':
            possible_moves = king_possible_movements(board, int(converted_coordinate[0]), int(converted_coordinate[1]))

        if piece.data['key']=='q':
            possible_moves = queen_possible_movements(board, int(converted_coordinate[0]), int(converted_coordinate[1]))

        if piece.data['key']=='n':
            possible_moves = knight_possible_movements(board, int(converted_coordinate[0]), int(converted_coordinate[1]))

            for item in possible_moves:
                converted_coord = convert_coordinates_to_numeric(board, item)
                second_turn.append({f'{item}':knight_possible_movements(board, int(converted_coord[0]), int(converted_coord[1]))})

        if piece.data['key']=='b':
            possible_moves = bishop_possible_movements(board, int(converted_coordinate[0]), int(converted_coordinate[1]))

        if piece.data['key']=='r':
            possible_moves = rook_possible_movements(board, int(converted_coordinate[0]), int(converted_coordinate[1]))

        if piece.data['key']=='p':
            possible_moves = pawn_possible_movements(board, int(converted_coordinate[0]), int(converted_coordinate[1]), piece.data)

        # Remove the coordinate from the results
        possible_moves = [i for i in possible_moves if i != coordinate]
            
        return Response(data = {
                "piece": piece.data, 
                "possible_moves": possible_moves,
                "second_turn": second_turn,
                
                },
                status=status.HTTP_200_OK)
        
    except:
        print('Could not find piece ID')

        return Response(
            data={ 'error': 'Could not find piece ID' },
            status=status.HTTP_404_NOT_FOUND)