import requests
sess = requests.Session()

url = 'https://t-capybit-kdot8z7j.spbctf.org/funds'
cookie = bytearray(b''.fromhex('28123600894ec0052e3aaaa91597dcad48aedf6c29de97312653d2a47f27d9a0efff226b0b501b3a6abc700e74f2a752a4b6444ff82c2d9250c836db1380d5b7530bf33de35a5999a5c1c194908e12da048bcf945f08b610925b9ce7e6fc206bf6a52587b0af02596cd091a318'))

for i in range(len(cookie)):
    original_byte = cookie[i]

    print(f'Position {i:3d}\t{original_byte:02x}\t', end='')
    flipped = cookie[:]

    # flipped[i] ^= 0b11111111
    flipped[i] ^= 0b00000001
    res = sess.get(url, cookies={"session": flipped.hex()})
    leaked = res.text[res.text.find('0x'):][:4]
    # leaked = int(leaked, 16) ^ 0b11111111
    # print(chr(leaked), end='', flush=True)
    print(res.text)
