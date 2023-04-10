import sympy
import numpy as np
from math import gcd

def mod_inv_matrix(M, n):
    det = int(np.round(np.linalg.det(M)))
    det_inv = pow(det, -1, n)
    adj = np.round(det * np.linalg.inv(M)).astype(int)
    return (det_inv * adj) % n

msg = 'bkujfdr kr tlvm gomuqng da bg ej eeeze dalkj jfdryje qei wteh pivb pigsl ricl cnrhui ig uonv'.replace(' ', '')
charset = {chr(97+i) : i for i in range(26)}
inv_charset = {charset[i] : i for i in charset}

n = len(charset)
print('Modulus : {}'.format(len(charset)))

raw = []
for c in msg:
    raw.append(charset[c])

# Compute trigrams
tri = []
for i in range(0, len(raw), 3):
    tri.append(raw[i:i+3])

# Here, clear texte known is hillcipher
clears = 'illcipher'
clears = [clears[0:3], clears[3:6], clears[6:9]]
clears_raw = []
for clear in clears:
    clears_raw.append([charset[c] for c in clear])

# For each trigrams of the cipher text
for j in range(0, len(msg) - 6, 3):
    cyphers = [msg[j:j+3], msg[j+3:j+6], msg[j+6:j+9]]
    cyphers_raw = []
    for cypher in cyphers:
        cyphers_raw.append([charset[c] for c in cypher])

    # Calculate the matrix representing the linear system
    a = sympy.Matrix(clears_raw)
    bs = [sympy.Matrix([cyphers_raw[0][0], cyphers_raw[1][0], cyphers_raw[2][0]]), 
        sympy.Matrix([cyphers_raw[0][1], cyphers_raw[1][1], cyphers_raw[2][1]]), 
        sympy.Matrix([cyphers_raw[0][2], cyphers_raw[1][2], cyphers_raw[2][2]])]
    m = n

    key = [[], [], []]
    # Inverse the Matrix modulus n to solve the system
    for i, b in enumerate(bs):
        det = int(a.det())
        if gcd(det, m) == 1:
            ans = pow(det, -1, m) * a.adjugate() @ b % m
            key[i] = [int(x) for x in ans]
        else:
            print("Matrix not inversible")

    key = np.array(key)
    try:
        # Get the invert matrix of the key
        clear_txt = ''
        inv_key = mod_inv_matrix(key, n)
        
        # Uncypher the text 
        answer = []
        for t in tri:
            t = np.dot(inv_key, t) % n
            for x in t:
                clear_txt += inv_charset[x]
        print(clear_txt)
    except:
        pass
    # print('Uncipher key : \n{}'.format(inv_key))


    