def generate_hash(orderId):
    hashed=hash(orderId)
    return hashed

def verify_hash(orderId,hashedValue):
    calculated_hash = generate_hash(orderId)
    return calculated_hash== hashedValue

if __name__ == '__main__':
    hash=generate_hash(90)
    print verify_hash(90,hash)