def gcd(x, y):
    if x == 0 and y != 0:
        return y
    elif x == 0 and y == 0:
        return None
    else:
        return gcd(y % x, x)


def mod_inv(x, y):
    r = []
    s = []
    t = []
    q = []

    inverse = gcd(x, y)

    if inverse is None:
        return None
    else:
        i = 1
        r.append(x)
        r.append(y)
        s.append(1)
        s.append(0)
        t.append(0)
        t.append(1)

        while r[i] != 0:
            quotient = r[i-1] // r[i]
            q.append(quotient)
            remainder = r[i-1] % r[i]
            r.append(remainder)
            if remainder == 0:
                break
            s_value = s[i-1] - quotient*s[i]
            s.append(s_value)
            t_value = t[i-1] - quotient*t[i]
            t.append(t_value)

            i += 1

    return s[-1] % y


def mod_exp(x, y, n):
    # this is where you encrypt M to produce a ciphertext

    p = 1  # p holds the partial result
    s = x  # s holds the current x
    r = y  # r is used to compute the binary expansion of y

    while r > 0:
        if r % 2 == 1:
            p = (p * s) % n
        s = (s * s) % n
        r = r // 2

    return p


def generate_rsa_keys(p, q):
    private = []
    rsa = []

    # step 1: find n and phi
    n = p * q
    phi = (p-1) * (q-1)

    private.append(n)

    # step 3: find some integer ''e'' that is relatively prime to phi
    e = 3
    while phi % e == 0:
        e += 2

    private.append(e)

    d = mod_inv(e, phi)

    rsa.append(private)
    rsa.append(d)

    return rsa


if __name__ == "__main__":
    p = int(input("Enter a prime integer: "))

    q = int(input("Enter a second prime integer: "))

    # Alice gets Bob's public key (n, e)
    list1 = generate_rsa_keys(p, q)

    public_key = list1[0]
    n = public_key[0]
    e = public_key[1]
    d = list1[1]

    # display the RSA public and private keys that are generated
    print("Public key is: n: ", n, " e: ", e)
    print("Private key is: ", d)

    # Alice prepares her plaintext
    m = int(input("Enter your plaintext integer M: "))
    c = mod_exp(m, e, n)
    print("After encryption: ")
    print("Ciphertext C is: ", c)

    # Alice then sends the ciphertext to Bob to have him decrypt it. Result is plaintext originally sent by Alice
    print("After decryption: ")
    print("M: ", mod_exp(c, d, n))
