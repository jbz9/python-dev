# 汉诺塔 ,将n个盘子从a经过b,移动到c
def hanoi(n, a, b, c):
    if n > 0:
        # 将 n-1个盘子，看做整体，将它从A经过C移动到B
        hanoi(n - 1, a, c, b)
        print("从%s 移动到 %s" % (a, c))
        hanoi(n - 1, b, a, c)


if __name__ == '__main__':
    hanoi(3, "A", "B", "C")
