from rest_framework import status
from rest_framework.test import APITestCase

class CreatePieceTestCase(APITestCase):

    def create_piece(self):
        data = {
            "type":"b",
            "color":"white"
        }

        response = self.client.post("/api/chess/piece/add/", data)

        print(response.json)
        
        self.assertEqual(response.status_code,  status.HTTP_201_CREATED)
        pass

class GetPossibleMovementsTestCase(APITestCase):

    def get_possible_movements(self):
        data = {
            "piece_id":5,
            "coordinate":"h4"
        }

        response = self.client.get("/api/chess/piece/movements/", data)

        print(response.json)
        
        self.assertEqual(response.status_code,  status.HTTP_200_OK)
        pass
