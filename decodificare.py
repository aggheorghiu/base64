import base64

def functie_decodificare():
    with open('codificareOutput.txt', 'r') as f:
        encoded_string = f.read().strip()

    decoded_bytes = base64.b64decode(encoded_string)
    decoded_string = decoded_bytes.decode('utf-8')

    with open('decodificareOutput.txt', 'w') as f:
        f.write(decoded_string)

#
# def functie_decodificare():
#     with open('codificareOutput.txt', 'r') as f:
#         encoded_string = f.read().strip()
#
#     # Convert the base64-encoded string to bytes
#     encoded_bytes = encoded_string.encode('ascii')
#
#     # Decode the bytes to a list of ASCII codes
#     ascii_codes = list(base64.b64decode(encoded_bytes))
#
#     # Convert the ASCII codes to a string
#     decoded_string = ''.join(chr(code) for code in ascii_codes)
#
#     with open('decodificareOutput.txt', 'w') as f:
#         f.write(decoded_string)
