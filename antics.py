# CIS-117 Lab3
# description_____
# Group 9
# names: Angela Wu, ___, ___

print('hello testing')

# test if input is abecedarian meaning in alphabetical order
def is_abecedarian(word_in):
    word = word_in.lower()
    previous = word[0]
    for i in word:
        if i < previous:
            return False
        previous = i
    return True

# test is input has exactly two of same letters in string
def is_dobloon(word):
    for i in word:
        count = 1
        for j in word[1:]:
            if i == j:
                count += 1
                if count > 2:
                    return False
        if count == 1:
            return False
        return True 



print(is_abecedarian('bacd'))
print(is_abecedarian('abcd'))
print('if two:', is_dobloon('mammal'))
print('if two:' , is_dobloon('noon')) 
