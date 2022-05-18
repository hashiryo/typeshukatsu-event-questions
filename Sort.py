def main():
    # ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]


def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    left = 0
    right = len(array) - 1
    while True:
        while left < right and array[left] < pivot:
            left += 1
        while left < right and array[right] >= pivot:
            right -= 1
        if left == right:
            break
        array[left], array[right] = array[right], array[left]
    if left == 0 or left == len(array) - 1:
        return array
    return sort(array[:left]) + sort(array[left:])
    # ここまで記述


if __name__ == '__main__':
    a = [1, 2, 3]
    main()
