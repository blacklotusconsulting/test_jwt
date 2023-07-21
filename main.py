# This is a sample Python script.
import jwt


def encode_user():
    """
    encode user payload as a jwt
    :param user:
    :return:
    """
    encoded_data = jwt.encode(payload={"name": "Alessandro","cognome": "Romani", "palazzo": 1},
                              key='bubu1aa',
                              algorithm="HS256")
    return encoded_data


if __name__ == "__main__":
    print(encode_user())
