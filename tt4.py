from typing import List


def find_median(array):
    sorted(array)
    return array[(len(array) - 1) // 2]


def get_subencrypted_string(message: List[str]):
    if not message:
        return ""

    subencrypted, mid_char = [], ''
    length, total_num = len(message[0]), len(message)
    for idx in range((length - 1) // 2):
        left, right = idx, length - 1 - idx
        arr = []
        for mess in message:
            arr.append(ord(mess[left]))
            arr.append(ord(mess[right]))

        med = find_median(arr)
        subencrypted.append(chr(med))

    if length % 2 == 1:
        idx = length // 2
        arr = []
        for mess in message:
            arr.append(ord(mess[idx]))

        med = find_median(arr)
        mid_char = chr(med)

    return ''.join(subencrypted) + mid_char + ''.join(subencrypted[::-1])


if __name__ == '__main__':
    assert get_subencrypted_string(['aba', 'cbd']) == 'aba'
