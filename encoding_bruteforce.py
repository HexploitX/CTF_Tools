def encode_decode(text):
    arr_encodings = [
        'utf-8', 'cp1251', 'koi8-r', 'koi8-u', 'cp866', 'cp855', 'cp437', 'cp1250', 'cp1252',
        'cp1253', 'cp1254', 'cp1255', 'cp1256', 'cp1257', 'cp1258', 'iso-8859-1', 'iso-8859-2',
        'iso-8859-3', 'iso-8859-4', 'iso-8859-5', 'iso-8859-6', 'iso-8859-7', 'iso-8859-8', 'iso-8859-9',
        'iso-8859-10', 'iso-8859-11', 'iso-8859-12', 'iso-8859-13', 'iso-8859-14', 'iso-8859-15', 'iso-8859-16',
        'gb2312', 'euc-jp', 'euc-kr'
    ]

    results = {}

    for enc in arr_encodings:
        try:
            encoded = text.encode(enc)
            decoded = encoded.decode('utf-8')
            results[enc] = decoded
        except Exception as e:
            pass
            # results[enc] = f"Error {e}"

    return results


if __name__ == '__main__':
    input_text = input('Enter your text: ')
    results = encode_decode(input_text)

    for encoding, result in results.items():
        print(f"{encoding}: {result}")