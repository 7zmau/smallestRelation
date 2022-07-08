# Copyright 2022 Princeton Gomes
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# This program finds the smallest string from a set of derived strings
# based on relationship rules on the input strings

import sys

inp = '''adfd
sfdd
ddfd'''

# ls: list of the given input strings.
ls = []
# relmap: dictionary of characters mapped to the list of
# characters which it can be replaced by.
relmap = {}


# Maps characters in the strings
# with the same index
def find_irreflexive():
    # Traversing first two strings
    for i in range(2):
        # Traversing individual characters of the first string
        for j in range(len(ls[i])):
            # Comparing with the same index of the second string

            # Skip if same characters
            if ls[i][j] == ls[i + 1][j]:
                continue
            else:
                if ls[i][j] in relmap:
                    # if character already in dictionary
                    # get list of mappings of current character
                    a = relmap[ls[i][j]]
                    # append to the list the character at the same index
                    # in the second string if not already exists
                    if ls[i + 1][j] not in a:
                        a.append(ls[i + 1][j])
                else:
                    # create a mapping of the character with
                    # the character in the second string
                    relmap[ls[i][j]] = [ls[i + 1][j]]


# Finds the transitive relation
# among the characters
def find_transitive(keylist):
    # for every key in dictionary
    for k in keylist:
        # v: List of current mappings of key
        v = relmap[k]
        for i in v:
            # get the mapping of the current character in v
            l = relmap[i].copy()
            # remove if same character
            if k in l:
                l.remove(k)
            # add mappings of v with key
            relmap[k] = sorted(list(set(l).union(set(v))))


# Create a mapping of characters with
# the list of characters which it can be replaced
def map_relations():
    find_irreflexive()
    ls.reverse()
    find_irreflexive()
    # keylist: list of individual characters in the input strings
    keylist = sorted(list(relmap.keys()))
    for i in range(len(keylist)):
        find_transitive(keylist)
    keylist.reverse()
    for i in range(len(keylist)):
        find_transitive(keylist)


# Run the script.
if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print('Error running script.\nUsage: main.py s1 s2 s3')
        exit(1)
    for arg in range(len(args)):
        if arg == 0:
            continue
        elif arg == 1:
            ls.append(args[arg])
        else:
            assert len(ls[0]) == len(args[arg])
            ls.append(args[arg])

    map_relations()
    # get the length of the smallest list in relmap
    lensma = min([len(relmap[k]) for k in relmap])
    # lrel: list of keys with the least relations
    lrel = [key for key, val in relmap.items() if len(val) == lensma]
    # sort the list lexicographically and get the first element
    g = sorted(lrel)[0]
    # construct a string by replacing the
    # elements in the relation with the key
    res = ''
    for v in relmap[g]:
        res += g

    print(res)
