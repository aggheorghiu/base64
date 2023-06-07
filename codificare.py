import base64


def functie_codificare():
    with open('input.txt', 'r') as f:
        name = f.read().strip()

    encoded_name = base64.b64encode(name.encode('ascii')).decode('ascii')

    # Add padding to the encoded string if necessary
    padding_length = 3 - (len(encoded_name) % 3)
    if padding_length != 3:
        encoded_name += "=" * padding_length

    with open('codificareOutput.txt', 'w') as f:
        f.write(encoded_name)


# def functie_codificare():
#     with open('input.txt', 'r') as f:
#         name = f.read().strip()
#
#     # Convert the string to a list of ASCII codes
#     ascii_codes = [ord(ch) for ch in name]
#
#     # Convert the ASCII codes to base64-encoded bytes
#     encoded_bytes = base64.b64encode(bytes(ascii_codes))
#
#     # Convert the bytes to a string
#     encoded_name = encoded_bytes.decode('ascii')
#
#     # Add padding to the encoded string if necessary
#     padding_length = 3 - (len(encoded_name) % 3)
#     if padding_length != 3:
#         encoded_name += "=" * padding_length
#
#     with open('codificareOutput.txt', 'w') as f:
#         f.write(encoded_name)
