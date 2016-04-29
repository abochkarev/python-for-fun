# Atbash is a simple substitution cipher originally for the Hebrew alphabet,
# but possible with any known alphabet. It emerged around 500-600 BCE.
# It works by substituting the first letter of an alphabet for the last letter,
# the second letter for the second to last and so on, effectively reversing
# the alphabet. Here is the Atbash substitution table:
# Plain:  abcdefghijklmnopqrstuvwxyz
# Cipher: ZYXWVUTSRQPONMLKJIHGFEDCBA

# Amusingly, some English words Atbash into their own reverses,
# e.g., "wizard" = "draziw."

# Examples:
# foobar -> ullyzi
# wizard -> draziw
# gsrh rh zm vcznkov lu gsv zgyzhs xrksvi -> this is an example of the atbash cipher


class Cipher(object):
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

    def __init__(self):
        super(Cipher, self).__init__()
        self.cipher_map = dict(zip(self.plain, self.cipher))

    def encode_decode(self, string):
        return ''.join([self.cipher_map.get(s, s).lower() for s in string])


c = Cipher()
print c.encode_decode('foobar')
print c.encode_decode('wizard')
print c.encode_decode('gsrh rh zm vcznkov lu gsv zgyzhs xrksvi')
