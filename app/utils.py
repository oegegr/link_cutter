from config import Config


def encode_id(id, base=Config.ENCODE_BASE):
    encoded_id = []
    len_base = len(base)
    while id:
        id, rem = divmod(id, len_base)
        encoded_id.append(base[rem])
    encoded_id.reverse()
    return ''.join(encoded_id)


def decode_id(short_url, base=Config.ENCODE_BASE):
    print(short_url)
    len_base = len(base)
    strlen = len(short_url)
    num = 0
    idx = 0
    for char in short_url:
        power = (strlen - (idx + 1))
        num += base.index(char) * (len_base ** power)
        idx += 1
    return num