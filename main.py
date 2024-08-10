

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_chars = count_chars(text)
    chars_sorted_list = chars_sorted(num_chars)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    
    for c in chars_sorted_list:
        if not c["char"].isalpha():
            continue
        print(f"The '{c['char']}' character was found {c['num']} times")

    print("--- End Report ---")
# Read the file in the path
def get_book_text(path):
    with open(path) as f:
        return f.read()

#Counts the word using the split on the string provided
def count_words(text):
    words = text.split()
    return len(words)
# counts the characters and adds them to a dictonary
def count_chars(text):
    chars ={}
    #for c in the sting, make a new lowercase string, if the sting is already in the dict then add one to that slot, if not set it equal to one
    for c in text:
        lower = c.lower()
        if lower in chars:
            chars[lower] +=1
        else:
            chars[lower] = 1
    return chars
    
def sort(dict):
    return dict["num"]
#sort using the character dictionary we set earlier
def chars_sorted(num_chars):
     occurances = []
     #for c in the dictionary we are appending occurances with a dictionary that contains the format "char" and the number. We then use the Number to sort
     for c in num_chars:
        occurances.append({"char": c, "num": num_chars[c]})
     occurances.sort(reverse=True, key=sort)
     return occurances


main()