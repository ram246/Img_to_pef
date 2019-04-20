import math

def merge_sort(l):
    if len(l) == 1:
        return l
    mid_point = math.floor(len(l) / 2)
    merge_left = merge_sort(l[:mid_point])
    merge_right = merge_sort(l[mid_point:])
    i = 0
    j = 0
    while (i + j) != len(l):
        if (i == len(merge_left)):
            l[i + j] = merge_right[j]
            j += 1
        elif (j == len(merge_right)):
            l[i + j] = merge_left[i]
            i += 1
        else:
            if merge_right[j] > merge_left[i]:
                l[i + j] = merge_left[i]
                i += 1
            else:
                l[i + j] = merge_right[j]
                j += 1
    return l
