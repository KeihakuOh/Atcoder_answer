from collections import Counter

def is_good_string(s):
    freq = Counter(s)
    #{'a': 2, 'b': 2, 'c': 2, 'e': 1}
    count_freq = Counter(freq.values())
    for count in count_freq.values():
        if count != 0 and count != 2:
            return "No"
    return "Yes"

s = str(input())
print(is_good_string(s)) 
