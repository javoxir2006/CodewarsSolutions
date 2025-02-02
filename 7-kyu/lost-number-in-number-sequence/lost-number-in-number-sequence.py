def find_deleted_number(arr, mixed_arr):
    lost = 0
    for x in arr:
        if x not in mixed_arr:
            lost = x
            break
    return lost