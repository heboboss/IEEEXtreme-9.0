from __future__ import print_function
from __future__ import division


ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def base62_encode(num, alphabet=ALPHABET):
    """Encode a number in Base X

    num: The number to encode
    alphabet: The alphabet to use for encoding
    """
    if (num == 0):
        return alphabet[0]

    arr = []
    base = len(alphabet)
    while num:
        rem = num % base
        # TODO
        num = num // base
        arr.append(alphabet[rem])

    arr.reverse()

    return ''.join(arr)


base = raw_input()

# number of URLs
n = int(raw_input())

tmp = []
# TODO
# unicode?
base_utf = []
for c in base:
    base_utf.append(ord(c))

tmp = base_utf[:]

for _ in range(n):
    target = raw_input()
    target_utf = []
    base_utf = tmp[:]
    for c in target:
        target_utf.append(ord(c))


    k = 0
    #
    for _ in range(len(base_utf), len(target_utf)):
        base_utf.append(base_utf[k])
        # k = (k+1) % (len(base_utf))
        k += 1

    xorurl = []
    for j in range(len(base_utf)):
        xorurl.append(target_utf[j] ^ base_utf[j])
    #print(xorurl)
    num = []
    num = xorurl[len(xorurl)-8:len(xorurl)]

    hexstr = ''
    hexstr += '0x' + '0' * (2-len(hex(num[0])[2:])) + hex(num[0])[2:]
    for j in range(1, len(num)):
        hexstr += '0' * (2-len(hex(num[j])[2:])) + hex(num[j])[2:]

    res = base62_encode(int(hexstr, 0))
    print(base + "/" + res)
