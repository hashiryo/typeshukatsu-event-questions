def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)


def serch_index(sorted_array, target_number):

    # ここから記述
    low = 0
    high = len(sorted_array)
    while high - low > 1:
        mid = (high + low) // 2
        if sorted_array[mid] <= target_number:
            low = mid
        else:
            high = mid
    if sorted_array[low] == target_number:
        return low
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1


if __name__ == '__main__':
    main()
