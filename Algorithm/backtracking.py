from typing import List


def full_array(nums):
    backtracking(nums, [])


def backtracking(options: List, tracks: List):
    if len(options) == 0:
        print(tracks)
        return tracks
    for i in options:
        options.remove(i)
        tracks.append(i)
        backtracking(options, tracks)
        options.append(i)
        tracks.remove(i)


if __name__ == '__main__':
    full_array([1, 2, 3])
