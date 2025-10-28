def count_words(text):
    words_array = text.split()
    return len(words_array)

def count_chars(text):
    counts = {} # char : count
    text = text.lower()
    for c in text:
        counts[c] = counts.get(c, 0) + 1
    return counts

def sort_char_stats(char_stats):
    res = []
    for char, count in char_stats.items():
        if char.isalpha():
            res.append(
                    {
                        "char" : char,
                        "num" : count
                        }
                    )
    res.sort(reverse=True, key = lambda el: el["num"])
    return res
        
