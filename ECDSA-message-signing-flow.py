import hashlib
import secrets
import ecdsa
from ecdsa import SECP256k1, ellipticcurve



def generate_keys():
    """Generates a private and public key pair."""
    # Generate a random 256-bit integer as a private key
    private_key = secrets.randbits(256)
    sk = ecdsa.SigningKey.from_string(private_key.to_bytes(32, byteorder="big"), curve=SECP256k1)
    sk_int = int.from_bytes(sk.to_string(), byteorder="big")

    # Calculate the public key using the private key
    generator_point = ellipticcurve.Point(SECP256k1.curve, SECP256k1.generator.x(), SECP256k1.generator.y(), SECP256k1.order)
    pk = generator_point * sk_int
    public_key = ecdsa.VerifyingKey.from_public_point(pk, curve=SECP256k1)

    return sk, public_key, generator_point


def hash_message(message):
    """Hashes a message using SHA-256."""
    return hashlib.sha256(message.encode('utf-8')).digest()

def print_keys(key):
    """Changes the format of a key to print it in various formats"""
    printable_key = int.from_bytes(key.to_string(), byteorder="big")
    return printable_key


def sign_message(private_key, message_hash, generator_point):
    """Signs a message."""
    random_key = secrets.randbelow(SECP256k1.order)
    print(f'\nRandomKey={random_key}')
    R = random_key * generator_point
    r = R.x() % SECP256k1.order
    sk_int = int.from_bytes(private_key.to_string(), byteorder="big")
    message_hash_int = int.from_bytes(message_hash, byteorder="big")
    s = (pow(random_key, -1, SECP256k1.order) * (message_hash_int + sk_int * r)) % SECP256k1.order

    return r, s


def verify_signature(public_key, message_hash, r, s, generator_point):
    """Verifies a signature."""
    message_hash_int = int.from_bytes(message_hash, byteorder="big")
    c = pow(s, -1, SECP256k1.order)
    print(f'\nc={c}')
    u1 = (message_hash_int * c) % SECP256k1.order
    print(f'\nu1={u1}')
    u2 = (r * c) % SECP256k1.order
    print(f'\nu1={u2}')
    u1G = u1 * generator_point
    print(f'\nu1 * G={int(u1G.to_bytes().hex(), 16)}')
    u2PK = u2 * public_key.pubkey.point
    print(f'\nu2 * PublicKey={int(u2PK.to_bytes().hex(), 16)}')
    v = (u1G + u2PK).x() % SECP256k1.order
    print(f'\nv={v}')
    print(f'\nr={r}')

    return v == r


if __name__ == "__main__":
    print("\nProcess: Generating Keys\n")
    sk, public_key, g = generate_keys()
    print(f"\nKeys:\nPrivateKey={print_keys(sk)}\nPublicKey={print_keys(public_key)}\n\n")
    #print(f"\nKeys in Hexadecimal:\nPrivateKey={hex(print_keys(sk))}\nPublicKey={hex(print_keys(public_key))}\n")

    print("\nProcess: Signing\n\n")
    message = input("Enter the message to sign: ")
    message_hash = hash_message(message)
    r, s = sign_message(sk, message_hash, g)
    print(f"\nSignature: (r={r}, s={s})\n\n")

    # Assuming the user re-enters the message for verification for simplicity
    print("\nProcess: Verifying\n")
    verification_message = input("Enter the message for verification: ")
    verification_hash = hash_message(verification_message)
    verification_result = verify_signature(public_key, verification_hash, r, s, g)
    print("\nThe signature is valid." if verification_result else "\nThe signature is not valid.")
