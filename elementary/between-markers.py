def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    index1 = text.find(begin)
    if index1 == -1:
        index1 = 0
    else:
        index1 += len(begin)

    index2 = text.find(end)
    if index2 == -1:
        index2 = len(text)

    if index1 > index2:
        return ''

    print(text[index1:index2])
    return text[index1:index2]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
