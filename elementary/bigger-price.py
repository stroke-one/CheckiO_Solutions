def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    bigger_dict = []
    price_filter = sorted([d['price'] for d in data], reverse=True)[:limit]
    print(price_filter)

    while price_filter:
        price_target = price_filter.pop(0)
        for price_dict in data:
            if price_dict['price'] == price_target:
                bigger_dict.append(price_dict)
    print(bigger_dict)
    return bigger_dict


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')
