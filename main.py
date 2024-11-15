#! python

def main():

    filename = "./books/frankenstein.txt"

    with open(filename) as f:
        file_contents = f.read()
        words = len(file_contents.split())
        letters = count_characters(file_contents)

        print(f'--- Begin report of {filename.split("/")[-1]} ---')
        print(f'{words} words found in the document')
        print()

        letters = {k: v for k, v in sorted(letters.items(), key=lambda item: item[1], reverse=True)}

        for k, v in letters.items():
            if k.isalpha():
                print(f"The '{k}' character was found {v} times")

        print(f'--- End report ---')


def count_characters(text):
    results = {}
    for char in text:
        char = char.lower()
        if char in results:
            results[char] += 1
        else:
            results[char] = 1
    return results

def count_words(text):
    return len(text.split())

if __name__ == "__main__":
   main()