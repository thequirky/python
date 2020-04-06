output = []


def flatten_nested(lst):
    """flatten a nested list"""

    for i in lst:
        if isinstance(i, list):
            flatten_nested(i)
        else:
            output.append(i)

    return output


if __name__ == "__main__":
    print(flatten_nested([1, 2, [3, 4]]))
