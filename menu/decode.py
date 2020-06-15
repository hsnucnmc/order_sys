#!/usr/bin/env python3
import base64

# decode image
with open("encode.txt", "rb") as encode_image_txt:
    encode_image = encode_image_txt.read()
    image = base64.decodebytes(encode_image)
    # create a writable image and write the decoding result
    image_result = open('decode.jpg', 'wb')
    image_result.write(image)
