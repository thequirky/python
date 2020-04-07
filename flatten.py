def flatten(lst):
    """
    flatten a list of lists
    """

    return [item for sublist in lst for item in sublist]


if __name__ == "__main__":
    print(flatten([[1, 2], [3, 4]]))
