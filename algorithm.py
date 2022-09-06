# SERACH
def search(num_list, num, idx=0):
    if idx >= len(num_list):
        return "Not Found"
    if num_list[idx] == num:
        return f"target {num} Found at position {idx + 1}"
    return search(num_list, num, idx + 1)


# print(search([1, 21, 4, 5, 12, 75, 42, 19], 20))