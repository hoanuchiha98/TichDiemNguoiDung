from _sha3 import sha3_224

salt = '2x4HOYylkHoa7'

def lazy_hashing(text):
    return sha3_224(f'{text} {salt}'.encode()).hexdigest()