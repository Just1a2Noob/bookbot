def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

# Uses split() to creating a list of words and 
# if the length of an index list is >0 then add 1 to the counter
def number_of_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        n_words = 0
        for i in file_contents.split():
            if len(i) > 0:
                n_words += 1
        
        return n_words

