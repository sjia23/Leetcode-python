from typing import List


def find_median(array):
    sorted(array)
    return array[(len(array) - 1) // 2]


def minimize_distortion(packets: List[int], max_frame: int):
    array_to_find_mediam = []
    for idx, packet in enumerate(packets):
        if idx > 0 and packet == 0:
            array_to_find_mediam.append(packets[idx - 1])

        if idx < len(packets) - 1 and packet == 0:
            array_to_find_mediam.append(packets[idx + 1])

    median = find_median(array_to_find_mediam)
    packet_val = min(max_frame, median)

    min_distort = 0
    for idx, packet in enumerate(packets):
        packets[idx] = packet_val if packet == 0 else packet
        if idx > 0:
            min_distort = max(min_distort, abs(packets[idx - 1] - packets[idx]))

    return min_distort


if __name__ == '__main__':
    # packets = [4,0,3,2,0,8,9,0,6]
    packets = [4, 0, 3, 2]
    assert minimize_distortion(packets, 2) == 2
    # packets = [4,x,3,2,x,8,9,x,6]
    # [10, 0, 1, 100]