def bubble_sort(items):
    did_sort = True
    while did_sort is True:
        did_sort = False
        for x in range(0, len(items)-1):
            if items[x] > items[x+1]:
                temp = items[x]
                items[x] = items[x+1]
                items[x+1] = temp
                did_sort = True
    return items


def merge_sort(items):
    if len(items) <= 1:
        return items
    else:
        zz = merge_sort(items[:int(len(items)/2)])
        yy = merge_sort(items[int(len(items)/2):len(items)])

        temp = []
        while len(zz) != 0 or len(yy) != 0:
            if len(yy) == 0:
                temp = temp + [zz[0]]
                zz = zz[1:]
            elif len(zz) == 0:
                temp = temp + [yy[0]]
                yy = yy[1:]
            elif zz[0] < yy[0]:
                temp = temp + [zz[0]]
                zz = zz[1:]
            else:
                temp = temp + [yy[0]]
                yy = yy[1:]

    return temp


def quick_sort(items):
    if len(items) <= 1:
        return items
    pivot_value = items[len(items)-1]
    set1 = []
    set2 = []
    for x in items[:len(items)-1]:
        if x < pivot_value:
            set1 = set1 + [x]
        else:
            set2 = set2 + [x]
    return quick_sort(set1) + [pivot_value] + quick_sort(set2)
