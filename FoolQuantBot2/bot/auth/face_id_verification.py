import requests

class FaceIDVerification:
    def verify(self, image):
        response = requests.post('https://faceapi.example.com/verify', files={'image': image})
        return response.json()['isIdentical']
