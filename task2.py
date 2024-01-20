def binary_search_upperbound(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    upper_bound = arr[-1]
    iteration = 0

    if upper_bound < x:
        return iteration, None
 
    while low <= high:
        iteration += 1
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
            upper_bound = arr[mid]
 
        # інакше x присутній на позиції і повертаємо його
        else:
            return iteration, arr[mid]
 
    # якщо елемент не знайдений
    return iteration, upper_bound


if __name__ == '__main__':
    arr = [0.555, 0.9, 1.1, 2.3, 4.0, 5.6, 7.2]
    x = 5.6

    result = binary_search_upperbound(arr, x)

    print(result)