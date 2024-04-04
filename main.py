def letters(text):
    d = {}
    l= []
    low = text.lower()
    for i in range(0,len(low)):
        if low[i] in d:
            d[low[i]] += 1
        else: d[low[i]] =1
    for e in d:
        if e.isalpha():
            l.append({"name":e,"count":d[e]})
    return l    
def sort_on(dict):
    return dict["count"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    lst = letters(file_contents)
    lst.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")
    for d in lst:
        print(f"The '{d["name"]}' character was found '{d["count"]}' times")
    print("--- End report ---")

main()