# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import jwt


def encode_user():
    """
    encode user payload as a jwt
    :param user:
    :return:
    """
    encoded_data = jwt.encode(payload={"name": "Alessandro","cognome": "Romani", "stocazzo": 1},
                              key='bubu1aa',
                              algorithm="HS256")
    return encoded_data


if __name__ == "__main__":
    print(encode_user())
