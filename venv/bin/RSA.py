'''
       This program is an implemenation of the encryption algorithm RSA  , we use the package sympy because we need functions to
       take the nextprime integer for a range of integer , to take te Modular multiplicative inverse integer and to check if an integer
       is prime . This packages holds function for this three activities and even more .

       We try the algorithm with an example , we use the message = "University "
'''

import sympy

# The function lst2str receives a list of numbers and returns an alphanumeric

def lst2str(list):

    return ''.join([chr(x+65) for x in list])

# The 'encryption' function encrypts the string 'string' using the key 'key'

def encryption(string, key):

    pln = str2lst(string)
    plnsf = [(x + key ) % 26 for x in pln]
    return lst2str(plnsf)

# The 'decryption' function performs the decryption of the string 'string using the key 'key'


def generate_keypair(p, q):
    if not (sympy.isprime(p) and sympy.isprime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    # n = pq
    n = p * q

    # Phi is the totient of n
    phi = (p - 1) * (q - 1)


    # We use the function randprime to return random prime number in the range [1, phi)
    e = sympy.randprime(1,phi)

    # We use the function mod_inverse to take the Modular multiplicative inverse d
    d = sympy.mod_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)


if __name__ == '__main__':

    p = sympy.nextprime(7)
    q = sympy.nextprime(21)
    public, private = generate_keypair(p, q)
    print ("Your public keypair is ", public, " and your private keypair is ", private)
    message = "University"
    print ("The message that you are going to encrypt is : ",message)
    encrypted_msg = encrypt(private, message)
    print("The encrypted message is : " ,lst2str(encrypted_msg))
    print ("The decrypted message is : " , decrypt(public, encrypted_msg))