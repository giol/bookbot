def main():
    with open('books/frankenstein.txt', 'r') as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        word_count = count_words_in_text(file_contents)
        print(f"{word_count} words found in the document")
        print("")
        print_character_frequency(file_contents)
        print("--- End report ---")


def count_words_in_text(contents: str) -> int:
    words = contents.split()
    return len(words)


def count_characters_in_text(contents: str) -> dict[str, int]:
    result: dict[str, int] = {}
    for c in contents:
        c = c.lower()
        if c not in result:
            result[c] = 0
        result[c] += 1
    return result


def sort_on(dict):
    return dict['count']


def print_character_frequency(contents: str) -> None:
    cfreq = count_characters_in_text(contents=contents)
    dfreq = []
    for k, v in cfreq.items():
        dfreq.append({'character': k, 'count': v})
    dfreq.sort(reverse=True, key=sort_on)
    for charcount in dfreq:
        print(f"The '{charcount['character']}' character was found {
              charcount['count']} times")


main()
