from reader import read_file
from processor import get_top_words
from writer import write_result


def main():
    input_file = "input.txt"
    output_file = "output.txt"

    text = read_file(input_file)
    top_words = get_top_words(text)
    write_result(output_file, top_words)


if __name__ == "__main__":
    main()