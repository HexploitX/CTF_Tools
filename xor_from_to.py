xor = lambda fromm, to: bytes([a^b for a, b in zip(fromm, to)])

fromm = input('Enter from: ').encode()
to = input('Enter to: ').encode()
diff = input('Enter difference: ')

diff_bytes = b''.fromhex(diff)
flip = xor(fromm, to)

if len(diff):
    flipped = xor(diff_bytes, flip)
    print("Result: " + flipped.hex())
else:
    print("Result: " + flip.hex())
