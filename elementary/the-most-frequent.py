def most_frequent(data: list) -> str:
    max_item = ""
    max_count = 0
    for item in set(data):
        if data.count(item) > max_count:
            max_count = data.count(item)
            max_item = item
    return max_item

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]))
    
    assert most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
