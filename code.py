# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename, 'r') as f:
        file = f.read()
        return file

output = read_file_content('story.txt')
print(output)


def count_words():
    text = open("./story.txt", 'r')
    # [assignment] Add your code here
    counts =  dict()
    words = str.split(" ")

    for line in text:
        line = line.strip()
        for character in string.punctuation:
            line = line.replace(character, "")
        line = line.lower()
        words = line.split(" ")

    for word in words:

        if word in counts:
          counts[words] += 1
        else:
          counts[word] = 1

    for key in list(counts.keys()):
        print (key, ":", counts[key])

count_words()
