from _sha3 import sha3_224

salt = '2x4HOYylkHtr9'

def lazy_hashing(text):
    return sha3_224(f'{text} {salt}'.encode()).hexdigest()