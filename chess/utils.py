# Pieces types
PIECES = [
    {
        'type':'pawn',
        'key':'p'
    },
    {
        'type':'queen',
        'key':'q'
    },
    {
        'type':'king',
        'key':'k'
    },
    {
        'type':'knight',
        'key':'n'
    },
    {
        'type':'bishop',
        'key':'b'
    },
    {
        'type':'rook',
        'key':'r'
    },
]

# Checks if a coordinate is valid for the 8x8 board
def is_valid(x, y):
    return not (x < 0 or y < 0 or x >= 8 or y >= 8)


# Get piece by type or key
def get_piece(piece_type):
    # Search on PIECES for a piece name and return it, if found.
    for piece in PIECES:
        if piece.get('type') == piece_type or piece.get('key') == piece_type:
            return piece

    return False

# Find Index from matrix receiving the item
def find_index_in_matrix(mat, item):

    for r in range(len(mat)):
        for c in range(len(mat)):

            if mat[r][c] == item:
                return (r, c)
                
# Get a board in algebraic notation and return its index
def convert_coordinates_to_numeric(board, coordinate):
    return find_index_in_matrix(board, coordinate)

# Range of chars
def range_char(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))


# Generate a board following Algebraic notation
def generate_board(number):
    matrix = [ [ f'{j}{i+1}' for i in reversed(range(number)) ] for j in range_char('a', 'h') ]

    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


# Receives a the matrix and its coordinate, then return all possible positions for the knight
def knight_possible_movements(mat, p, q):

    if p > 8 or q > 8:
        return {"error":"Invalid coordinate. This should be a 8x8 board."}

     
    # All possible moves of a knight
    X = [2, 1, -1, -2, -2, -1, 1, 2]
    Y = [1, 2, 2, 1, -1, -2, -2, -1]
 
    result = []
 
    # Check if each possible move
    for i in range(8):
        x = p + X[i]
        y = q + Y[i]

        # Append to result the valid moves
        if is_valid(x, y):
            print(f'Possible movement: {mat[x][y]}')
            result.append(mat[x][y])
 
    # Return all possible moves
    return result


# Receives a the matrix and its coordinate, then return all possible positions for the king
def king_possible_movements(mat, p, q):
    if p > 8 or q > 8:
        return {"error":"Invalid coordinate. This should be a 8x8 board."}

    # Possible King Moves
    X = [1, 1, 1, 0, 0, -1,-1, -1]
    Y = [0, 1, -1, -1, 1, 0, +1, -1]

    result = []

    # Check if each possible move
    # is valid or not
    for i in range(8):

        x = p + X[i]
        y = q + Y[i]

        # Append to result the valid moves
        if is_valid(x, y):
            print(f'Possible movement: {mat[x][y]}')
            result.append(mat[x][y])
 
    # Return all possible moves
    return result

# Receives a the matrix and its coordinate, then return all possible positions for the Bishop
def bishop_possible_movements(mat, p, q):

    if p > 8 or q > 8:
        return {"error": "Invalid coordinate. This should be a 8x8 board."}

    result = []
    
    # Get bottom-right movemets
    for i in range(8):
        x = p + i
        y = q + i

        # Append to result the valid moves
        if is_valid(x, y):
            print(f'Possible movement: {mat[x][y]}')
            result.append(mat[x][y])
            
    # Get top-left movements
    for i in range(8):
        x = p - i
        y = q - i

        # Append to result the valid moves
        if is_valid(x, y):
            print(f'Possible movement: {mat[x][y]}')
            result.append(mat[x][y])

    
    # Get bottom-left movements
    for i in range(8):
        x = p + i
        y = q - i

        # Append to result the valid moves
        if is_valid(x, y):
            print(f'Possible movement: {mat[x][y]}')
            result.append(mat[x][y])

    # Get top-right movements
    for i in range(8):
        x = p - i
        y = q + i

        # Append to result the valid moves
        if is_valid(x, y):
            print(f'Possible movement: {mat[x][y]}')
            result.append(mat[x][y])

    # Return all possible moves
    return result

# Receives a the matrix and its coordinate, then return all possible positions for the rook
def rook_possible_movements(mat, p, q):
    if p > 8 or q > 8:
        return {"error": "Invalid coordinate. This should be a 8x8 board."}

    result = []

    # Get top movements
    for i in range(8):
        x = p - i
        y = q

        # Append to result the valid moves
        if is_valid(x, y):
            print(f'Possible movement: {mat[x][y]}')
            result.append(mat[x][y])
    print("TOPPP")
    # Get bottom movements
    for i in range(8):
        x = p + i
        y = q

        # Append to result the valid moves
        if is_valid(x, y):
            print(f'Possible movement: {mat[x][y]}')
            result.append(mat[x][y])

    # Get Right movements
    for i in range(8):
        x = p
        y = q + i

        # Append to result the valid moves
        if is_valid(x, y):
            print(f'Possible movement: {mat[x][y]}')
            result.append(mat[x][y])

    # Get Left movements
    for i in range(8):
        x = p
        y = q - i

        # Append to result the valid moves
        if is_valid(x, y):
            print(f'Possible movement: {mat[x][y]}')
            result.append(mat[x][y])

    # Return all possible moves
    return result

# Receives a the matrix and its coordinate, then return all possible positions for the queen
def queen_possible_movements(mat, p, q):
    result = []
    
    # Get the possible movements for bishop
    bishop_moves = bishop_possible_movements(mat, p, q)

    # Get the possible movements for rook
    rook_moves = rook_possible_movements(mat, p, q)

    # Append the results in one single array
    for item in bishop_moves:
        result.append(item)

    for item in rook_moves:
        result.append(item)

    # Return all possible moves
    return result

# Receives a the matrix and its coordinate, then return all possible positions for the pawn
def pawn_possible_movements(mat, p, q, piece):
    if p > 8 or q > 8:
        return {"error":"Invalid coordinate. This should be a 8x8 board."}

    result = []

    print(piece)
    
    if piece['color'] == 'black':
        if p == 1:
            if is_valid(p+1, q) and is_valid(p+2, q):
                result.append(mat[p+1][q])
                result.append(mat[p+2][q])
            pass

        elif p == 7:
            pass

        else:
            if is_valid(p+1, q):
                result.append(mat[p+1][q])
            pass



    if piece['color'] == 'white':
        if p == 6:
            if is_valid(p-1, q) and is_valid(p-2, q):
                result.append(mat[p-1][q])
                result.append(mat[p-2][q])
            pass

        elif p == 0:
            pass

        else:
            if is_valid(p-1, q):
                result.append(mat[p-1][q])
            pass


    # Return all possible moves
    return result