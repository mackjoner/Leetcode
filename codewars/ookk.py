
# okkOokOo
'''
Syntax Elements

Ook! has only three distinct syntax elements:
Ook.
Ook?
Ook!
These are combined into groups of two, and the various pair combinations specify commands. Programs must thus contain an even number of "Ook"s. Line breaks are ignored.'
'''

# Commands
'''
Ook. Ook?    Move the Memory Pointer to the next array cell.
Ook? Ook.    Move the Memory Pointer to the previous array cell.
Ook. Ook.    Increment the array cell pointed at by the Memory Pointer.
Ook! Ook!    Decrement the array cell pointed at by the Memory Pointer.
Ook. Ook!    Read a character from STDIN and put its ASCII value into the cell pointed at by the Memory Pointer.
Ook! Ook.    Print the character with ASCII value equal to the value in the cell pointed at by the Memory Pointer.
Ook! Ook?    Move to the command following the matching Ook? Ook! if the value in the cell pointed at by the Memory Pointer is zero. Note that Ook! Ook? and Ook? Ook! commands nest like pairs of parentheses, and matching pairs are defined in the same way as for parentheses.
Ook? Ook!    Move to the command following the matching Ook! Ook? if the value in the cell pointed at by the Memory Pointer is non-zero.
Um, that's it.
That's the whole language. What do you expect for something usable by orang-utans?
'''


def okkOokOo_r(s):
    output = ''
    maps={'Ok, Ook, Ooo':'H', 'Okk, Ook, Ok':'e',
    'Okk, Okk, Oo':'l', 'Okk, Okkkk':'o'
    }
    maps = dict(zip(maps.values(), maps.keys()))
    for idx, char in enumerate(s):
        if idx < len(s) - 1:
            output += maps[char]+'? '
        else:
            output += maps[char]+'!'
    return output

import re
def okkOokOo(s):
    output = ''
    maps={'Ok, Ook, Ooo':'H', 'Okk, Ook, Ok':'e',
    'Okk, Okk, Oo':'l', 'Okk, Okkkk':'o'
    }

    tokens = re.split('(\? )|(!)', s)
    for idx, token in enumerate(tokens):
        if token in maps:
            output += maps[token]
    return output


print okkOokOo('Ok, Ook, Ooo!') #, 'H')
print okkOokOo('Okk, Ook, Ok!') #, 'e')
print okkOokOo('Okk, Okk, Oo!') #, 'l')
print okkOokOo('Okk, Okkkk!') #, 'o')

print okkOokOo('Ok, Ook, Ooo? Okk, Ook, Ok? Okk, Okk, Oo? Okk, Okk, Oo? Okk, Okkkk!') #, 'Hello')
# print('Ok, Ook, Ooo? Okk, Ook, Ok? Okk, Okk, Oo? Okk, Okk, Oo? Okk, Okkkk!')
# print(
#     "> " + okkOokOo('Ok, Ook, Ooo? Okk, Ook, Ok? Okk, Okk, Oo? Okk, Okk, Oo? Okk, Okkkk!'))


