# 顺序查找，遍历列表，查找
# 问题规模：数组长度， 一个for循环，没有循环减半(logn),即时间复杂度为 O(n)
def linear_search(list_data, k):
    for index, value in enumerate(list_data):
        if k == value:
            print(f"在列表中第{index + 1}个元素中找到了{value}")
            return index
    return None


if __name__ == '__main__':
    list_data = ["1", "2", "3"]
    linear_search(list_data, "3")
