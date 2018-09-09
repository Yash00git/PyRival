from math import sqrt


class bitArray:
    def __init__(self, size):
        self.bytes = bytearray((size >> 3) + 1)

    def __getitem__(self, index):
        return (self.bytes[index >> 3] >> (index & 0b111)) & 1

    def __setitem__(self, index, value):
        if value:
            self.bytes[index >> 3] |= 1 << (index & 0b111)
        else:
            self.bytes[index >> 3] &= ~(1 << (index & 0b111))


def get_primes(n):
    # does not return 2 and 3
    m = n + 6 - (n % 6)
    sieve = bitArray(m//3)
    for i in range(1, int(sqrt(m) // 3 + 1)):
        if not sieve[i]:
            k = (3 * i + 1) | 1
            for j in range(k * k // 3, m // 3, 2 * k): sieve[j] = 1
            for j in range(k * (k - 2 * (i & 1) + 4) // 3, m // 3, 2 * k): sieve[j] = 1

    return ((3*i + 1) | 1 for i in range(1, m//3 - (n % 6 > 1)) if not sieve[i])