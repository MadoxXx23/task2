from random import sample


def search_target_index(list_digits: list, target: int):
    left, right = 0, len(list_digits) - 1
    while left <= right:
        middle = (left + right) // 2
        if list_digits[middle] < target:
            left = middle + 1
        elif list_digits[middle] > target:
            right = middle - 1
        else:
            return middle
    return


def main():
    size_list = 10
    rand_list = sorted(sample(range(0, 101, 2), size_list))
    print(rand_list)
    try:
        target = int(input('Pick a number between 0-100: '))
        target_index = search_target_index(rand_list, target)

        print(f'List: {rand_list}')
        if target_index is not None:
            print(f'Found {target} in index {target_index}')
        else:
            print(f'Cannot find {target} in the list')
    except ValueError:
        print('Invalid input')


if __name__ == "__main__":
    main()
