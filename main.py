# This is a sample Python script.
import jwt
import requests


def encode_user():
    """
    encode user payload as a jwt
    :param user:
    :return:
    """
    encoded_data = jwt.encode(payload={"name": "Alessandro", "cognome": "Romani", "palazzo": 1},
                              key='bubu1aa',
                              algorithm="HS256")
    return encoded_data
def request_bubu():
    r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
    return r.text

def post_bubu():
    data = '11okokok'
    p = requests.post('https://httpbin.org/post', data)
    return p.status_code

if __name__ == "__main__":
    encoded_data = encode_user()
    print("Encoded data:", encoded_data.decode())  # Decoding bytes to a string
    print("HTTP status code:", request_bubu())
    print("HTTP status code:", post_bubu())
