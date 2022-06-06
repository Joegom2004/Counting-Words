# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, 'r') as f:
        return f.read()

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    result = {}
    for word in text.split():
        if word[-1] == '.' or word[-1] == ',' or word[-1] == '?':
            word = word[:-1]
            appearances = text.count(word)
            result.update({word: appearances})
        else:
            appearances = text.count(word)
            result.update({word: appearances})
    # return {"as": 10, "would": 20}
    return result

print(count_words())