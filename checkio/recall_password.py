import numpy as np
import pdb

def recall_password(cipher_grille, ciphered_password):
    
    cipher_grille = [list(arg) for arg in cipher_grille]
    cipher_grille = [np.array(cipher_grille), np.rot90(cipher_grille, -1), np.rot90(cipher_grille, -2), np.rot90(cipher_grille, -3) ]

    ciph_g = np.array(cipher_grille)
    ciph_g = ciph_g.flatten()                 

    ciphered_password = [list(arg) for arg in ciphered_password]
    ciphered_password = [ciphered_password]*4
    ciph_p = np.array(ciphered_password)
    ciph_p = ciph_p.flatten()

    password = [ciph_p[i] for i in range(len(ciph_p)) if ciph_g[i] == 'X']
    password = ''.join(password)

    return password

password = recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr'))

print password   