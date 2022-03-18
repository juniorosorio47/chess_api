# Chess possible movements API
This is an API that returns a list of possible movements for a given piece on board 8x8. The coordinates are defined following the Algebraic Notation.  

# Setup API:
To run this project in your computer you have 2 options:  
1. With Docker and docker-compose: Runs 2 docker images: The API and the database (MySQL).  
2. With Python and a MySQL database. **Note:** docker-compose option already do everything, thats magic 🪄.  

## 

# Here is how to use the API:

## Add a piece to the board:
First of all, you need to add the piece to the board.  
You can make a request to:  
```
http://localhost:8000/api/chess/piece/add
```

Your request body should have the following parameters to create a piece (the values are not case sensitive):  
```json
{
    //You can send the type in 2 ways: with the key or name. These are described below.
    "name":"knight", // or "N"
    "color":"black" // or "white"
}
```

### Possible types:  

| Name | Key | Possible Movements |
|---|---|---|
| Pawn  | P  |  1 or 2 spaces forward |
| Rook  | R  | anywhere in the same rank or same file  |
| Knight  | N  |  2 in one direction and 1 in the other “L-shaped” |
| Bishop  |  B | diagonally, any distance  |
| Queen  | Q  |  horizontal, vertical or diagonal, any distance |
| King  |  K | 1 space in any direction  |


### The response from the API route **/api/chess/piece/add** should be like this:

```json
{
    "data":{
        "piece_id":1,
        "message":"Piece Knight added to the board"
    }
}
```

---

## Get the possible movements:
After created at least one piece, you can make a request to the following url to get the possible movements:  

```
http://localhost:8000/api/chess/piece/movements
```
You need to send the **piece_id** and **current_coordinate** (in [Algebraic notation](https://en.wikipedia.org/wiki/Algebraic_notation_(chess))) of the piece.  
If the piece is a **Knight (N)**, the API will return the possible movements within **2 turns**. If its another piece it will return the possible movements for 1 turn.  
For instance: The Knight I created is at the coordinate H6 on an empty board, and I want to know what are the possible movements. So I will make a request informing the piece_id and current coordinate.  

My request body should have the following parameters:  
```json
{
    // Piece id received on the piece creation
    "piece_id":1,
    // Current coordinates of my piece
    "current_coordinate":"H6"
}
```

### The response from the API route **/api/chess/piece/move** should be like this:
```json
{
    "data":{
        "piece_id":1,
        "current_coordinate":"h6",
        "possible_movements":[
            "g4",
            "g8",
            "f5",
            "f7",
        ],
        "next_possible_movements":[

            "g4",
            "g8",
            "f5",
            "f7",
        ]
    }
}
```


