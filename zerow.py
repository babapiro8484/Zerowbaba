import base64

def get_auth():
    encoded = "WkVST1ctUFJJVkFURS1LRVktMTEyMg=="
    return base64.b64decode(encoded).decode()
