# Credit to Brtwrst from the Engineer Man discord for turning my 76 line program into an 8 liner.

conversion_lookup = (
    ('', 'M', 'MM', 'MMM'),
    ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'),
    ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'),
    ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')
)
num = input()
print(''.join([conversion_lookup[i][int(n)] for i,n in enumerate(num.zfill(4))]))
