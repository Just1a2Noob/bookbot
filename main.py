def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

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

def number_of_letters():
    file_contents = main()
    file_contents = file_contents.lower()
    letters_dict = {}
    for i in file_contents:
        if i != " " and i.isalpha() == True:
            if i in letters_dict:
                letters_dict[i] += 1
            else:
                letters_dict[i] = 1
    return letters_dict


def create_report():
    print("--- Begin report of books/frankenstein.txt ---")
    print(number_of_words(), "words found in the document")
    letters_dict = number_of_letters()
    sort_letters_dict = sorted(letters_dict.items(), key=lambda x:x[1], reverse=True)
    for d in sort_letters_dict:
        print("The", d[0], "character was found", d[1], "times")
