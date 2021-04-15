import os


def main():
    print_header()
    folder_path = get_search_folder()

    if not folder_path:
        print("Sorry, we couldn't find that folder")
        return

    text = get_search_text()
    if not text:
        print("We cannot search for nothing")
        return

    search_folder(folder_path, text)


def print_header():
    print('--------------------------------')
    print('       FILE SEARCHER APP   ')
    print('--------------------------------')
    print('')


def get_search_folder():
    folder = input("Where to do want to conduct your search? ")

    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    print(os.path.abspath(folder))
    return os.path.abspath(folder)


def get_search_text():
    text = input("What would you like to search for? ")

    return text.lower().strip()


def search_folder(folder, text):
    all_matches = []
    items = os.listdir(folder)

    for item in items:
        full_path = os.path.join(folder, item)
        if os.path.isdir(full_path):
            continue

    matches = search_file(full_path, text)
    all_matches.extend(matches)

    return all_matches


def search_file(filename, text):
    print(filename)
    all_matches = []
    with open(filename, 'r', encoding='utf-8') as fin:

        for line in fin:
            if line.lower().find(text) >= 0:
                all_matches.append(line)

    return all_matches


if __name__ == '__main__':
    main()
