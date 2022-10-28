string1 = "lost"
string2 = "Lsot"

def is_permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    else:
        string1 = string1.casefold()
        string2 = string2.casefold()
        chars = {}
        for char in string1:
            chars[char] = 1
        for char in string2:
            try: chars[char]
            except: return False
        else:
            return True
        
print(is_permutation(string1, string2))
        