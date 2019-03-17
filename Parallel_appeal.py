import numpy as np

MY_RANK = 3
SIZE = 10
ARR_SIZE = 10


# checks if a boolean array is full (0.0 is false and 1 is true, the logic is of boolean)
def full(indexes):
    for i in range(indexes.__len__()):
        if indexes[i] == 0:  # in the exam i wrote "if indexes[i] == 1"
            return False
    return True


# generate subset of arr by indexes values
def gen_set(indexes, arr):
    res = []
    for i in range(indexes.__len__()):
        if indexes[i] == 1:
            res.append(arr[i])
    return res


# increments indexes by 1 (treats subset choice as a boolean vector)
def next_func(indexes):
    if full(indexes):
        return indexes
    i = 0

    # this part is wrong, cant figure out why i wrote it, but if you just remove it, it works

    # while(indexes[i]) == 0:
    # i += 1
    # indexes[i] = 0
    # i += 1

    # end of the wrong part

    while (indexes[i] == 1):
        indexes[i] = 0
        i += 1
    if i < indexes.__len__():
        indexes[i] = 1
    return indexes


def subset_generator(arr):
    rank = MY_RANK
    size = SIZE
    chosen_set = np.zeros(arr.__len__())

    chosen_set[0] = 1  # this is a mistake, makes it skip the empty subset possibility

    # the logic is as follow:
    # all of the processes iterates with the same order on subsets of arr,
    # in the first iteration every process takes an offset of its own rank
    # in every other iteration every process jumps SIZE iterations forwards
    # in the last iteration all of the processes will check the full subset, as its simplify
    # the logic and take almost no performance price

    # makes for each rank a different "offset" in the subsets
    for i in range(rank):
        chosen_set = next_func(chosen_set)
    yield (gen_set(chosen_set, arr))  # in exam i wrote "yield gen_set(chosen_set)"

    while not full(chosen_set):
        # jumps <size> iterations forward
        for _ in range(size):
            chosen_set = next_func(chosen_set)
        yield gen_set(chosen_set, arr)  # in exam i wrote "yield gen_set(chosen_set)"


if __name__ == "__main__":
    arr = np.array(range(ARR_SIZE))
    for i in subset_generator(arr):
        print(i)
