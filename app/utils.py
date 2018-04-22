from config import Config


def encode_id(id, base=Config.ENCODE_BASE):
    encoded_id = []
    len_base = len(base)
    while id:
        id, rem = divmod(id, len_base)
        encoded_id.append(base[rem])
    encoded_id.reverse()
    return ''.join(encoded_id)


