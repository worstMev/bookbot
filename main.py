from stats import count_words, count_chars, sort_char_stats

def get_book_text(file_path):
    content = None
    with open(file_path) as f :
        content = f.read()
    return content

def main() :
    path = "./books/frankenstein.txt"
    content = get_book_text(path)
    num_words = count_words(content)
    stats_char = count_chars(content)
    stats_char = sort_char_stats(stats_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for el in stats_char:

        print(f"{el["char"]}: {el["num"]}")

    print("============= END ===============")


main()
