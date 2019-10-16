import requests
import json

example = [[10, 11, 12, 13, 14], [9, 10, 11, 12, 13], [8, 9, 10, 11, 12], [7, 8, 9, 10, 11],
           [6, 7, 8, 9, 10], [5, 6, 7, 8, 9], [4, 5, 6, 7, 8], [3, 4, 5, 6, 7], [2, 3, 4, 5, 6]]

# 检查涉及到“1”的牌型！！！！！！！！！！！！！！！！！！！！！！！！！！！！
car = "$3 $4 $5 $6 $7 *6 &8 *8 *9 *10 #J #Q #K"
# 只用于测试
cards = car.split(" ")  # 将字符串划分为单个牌元素


# 判断特殊牌型-------------------
def judge_spci1(mark, numbers):  # 至尊清龙
    num1 = mark.count(13)
    if num1 == 1:
        print("至尊清龙")
        return 1
    else:
        return 0


def judge_spci2(mark, numbers):  # 一条龙
    num2 = numbers.count(1)
    if num2 == 13:
        print("一条龙")
        return 1
    else:
        return 0


def judge_spci3(mark, numbers):  # 十二皇族
    if (numbers[9] + numbers[10] + numbers[11] + numbers[12]) == 12:
        print("十二皇族")
        return 1
    else:
        return 0


def judge_spci5(mark, numbers):  # 三分天下

    t = numbers.count(4)
    if t == 3:
        print("三分天下")
        return 1
    else:
        return 0


def judge_spci6(mark, numbers):  # 全大

    s = sum(numbers[0:6])
    if s == 0:
        print("全大")
        return 1
    else:
        return 0


def judge_spci7(mark, numbers):  # 全小
    sum3 = sum(numbers[7:])
    if sum3 == 0:
        print("全小")
        return 1
    else:
        return 0


def judge_spci_e(mark, numbers):  # 凑一色
    if mark[0] + mark[1] == 13:
        print("凑一色")
        return 1
    elif mark[2] + mark[3] == 13:
        print("凑一色")
        return 1
    else:
        return 0


def judge_spci8(mark, numbers):  # 双怪冲三
    n1 = numbers.count(1)
    n2 = numbers.count(2)
    n3 = numbers.count(3)
    if n1 == 1 and n2 == 3 and n3 == 2:
        print("双怪冲三")
        return 1
    else:
        return 0


def judge_spci9(mark, numbers):  # 四套三条
    n3 = numbers.count(3)
    n1 = numbers.count(1)
    if n1 == 1 and n3 == 4:
        print("四套三条")
        return 1
    else:
        return 0


def judge_spci_a(mark, numbers):  # 五队三条
    n2 = numbers.count(2)
    n3 = numbers.count(3)
    if n2 == 1 and n3 == 4:
        print("四套三条")
        return 1
    else:
        return 0


def judge_spci_b(mark, numbers):  # 六对半
    n2 = numbers.count(2)  # 相同牌号数量为2的个数
    n1 = numbers.count(1)  # 相同牌号数量为1的个数
    if n2 == 6 and n1 == 1:
        print("六对半")
        return 1
    else:
        return 0


def judge_spci_d(mark, numbers):  # 三同花
    flag = 0
    n1 = mark.count(3)  # 相同花色数量为3的个数
    n2 = mark.count(5)  # 相同花色数量为5的个数
    n3 = mark.count(8)  # 相同花色数量为8的个数
    n10 = mark.count(10)  # 相同花色数量为10的个数
    if n1 == 1 and n2 == 2:  # 3 5 5
        print("三同花")
        return 1
    elif n2 == 1 and n3 == 1:  # 5 8
        print("三同花")
        return 1
    elif n10 == 1 and n1 == 1:  # 3  10
        print("三同花")
        return 1
    else:
        return 0


# ===============================================

# 以下都没有就是散牌

example = [[10, 11, 12, 13, 14], [9, 10, 11, 12, 13], [8, 9, 10, 11, 12], [7, 8, 9, 10, 11],
           [6, 7, 8, 9, 10], [5, 6, 7, 8, 9], [4, 5, 6, 7, 8], [3, 4, 5, 6, 7], [2, 3, 4, 5, 6]]


def list_num_zu(cards, sym):  # 同一符号的所有数字的列表    纯数字
    ty = []
    for card in cards:
        if card[0] == sym:
            if card[1] == "1":
                ty.append(10)
            elif card[1] == "J":
                ty.append(11)
            elif card[1] == "Q":
                ty.append(12)
            elif card[1] == "K":
                ty.append(13)
            elif card[1] == "A":
                ty.append(14)
            elif card[1] == "2":
                ty.append(2)
            elif card[1] == "3":
                ty.append(3)
            elif card[1] == "4":
                ty.append(4)
            elif card[1] == "5":
                ty.append(5)
            elif card[1] == "6":
                ty.append(6)
            elif card[1] == "7":
                ty.append(7)
            elif card[1] == "8":
                ty.append(8)
            elif card[1] == "9":
                ty.append(9)

    return ty


def normal_a(cards, mark):  # 判断同花顺 
    example = [[10, 11, 12, 13, 14], [9, 10, 11, 12, 13], [8, 9, 10, 11, 12], [7, 8, 9, 10, 11],
               [6, 7, 8, 9, 10], [5, 6, 7, 8, 9], [4, 5, 6, 7, 8], [3, 4, 5, 6, 7], [2, 3, 4, 5, 6]]

    selected = ['@']
    weight = 0
    t = mark.count(0) + mark.count(1) + mark.count(2) + mark.count(3) + mark.count(4)
    if t == 4:
        return selected
    else:
        for i in range(0, 4):
            if mark[i] >= 5:
                if i == 0:  # 找出多于五张的花色
                    sym = '$'
                elif i == 1:
                    sym = '&'
                elif i == 2:
                    sym = '*'
                elif i == 3:
                    sym = '#'

                list1 = list_num_zu(cards, sym)  # 列出这种花色的所有牌号
                set1 = set(list1)
                op = 9
                for q in range(0, 9):
                    set2 = set(example[q])
                    x = set2.issubset(set1)
                    if x:
                        if op >= weight:
                            weight = op
                            df = list(set2)
                            selected = df[:]
                            selected.append(sym)  # 例如selected=[1,2,3,4,5,'$']
                            for t in range(0, 5):  # 转为全字符数组
                                b = selected[t]
                                if b == 14:
                                    selected[t] = "A"
                                elif b == 13:
                                    selected[t] = "K"
                                elif b == 12:
                                    selected[t] = "Q"
                                elif b == 11:
                                    selected[t] = "J"
                                elif b == 10:
                                    selected[t] = "1"
                                else:
                                    selected[t] = str(b)

                        break
                    else:
                        op -= 1
            else:
                continue
        return selected


def normal_b(cards, numbers):  # 判断炸弹
    selected = ['@']
    if (numbers.count(0) + numbers.count(1) + numbers.count(2) + numbers.count(3)) == 13:
        return selected
    else:
        renum = list(reversed(numbers))
        for i in range(0, 13):
            if renum[i] >= 4:
                renum[i] -= 4
                tp = 14 - i
                if tp == 14:
                    re4 = "A"
                elif tp == 13:
                    re4 = "K"
                elif tp == 12:
                    re4 = "Q"
                elif tp == 11:
                    re4 = "J"
                elif tp == 10:
                    re4 = "1"
                else:
                    re4 = str(tp)
                selected = [re4]
                break
        j = 0
        for card in cards:  # 取符号
            if card[1] == selected[0]:
                selected.append(card[0])
                j += 1
            if j == 4:
                break
        for card in cards:
            if card[1] == "2":
                if renum[12] != 4:
                    selected.append(card[0])
                    selected.append(card[1])
                    break

            elif card[1] == "3":
                if renum[11] != 4:
                    selected.append(card[0])
                    selected.append(card[1])
                    break

            elif card[1] == "4":
                if renum[10] != 4:
                    selected.append(card[0])
                    selected.append(card[1])
                    break
            elif card[1] == "5":
                if renum[9] != 4:
                    selected.append(card[0])
                    selected.append(card[1])
                    break
            elif card[1] == "6":
                if renum[8] != 4:
                    selected.append(card[0])
                    selected.append(card[1])
                    break
            elif card[1] == "7":
                if renum[7] != 4:
                    selected.append(card[0])
                    selected.append(card[1])
                    break
            elif card[1] == "8":
                if renum[6] != 4:
                    selected.append(card[0])
                    selected.append(card[1])
                    break
            elif card[1] == "9":
                if renum[5] != 4:
                    selected.append(card[0])
                    selected.append(card[1])
                    break
            elif card[1] == "1":
                if renum[4] != 4:
                    selected.append(card[0])
                    selected.append(card["10"])
                    break
            elif card[1] == "J":
                if renum[3] != 4:
                    selected.append(card[0])
                    selected.append(card[1])
                    break
            elif card[1] == "Q":
                if renum[2] != 4:
                    selected.append(card[0])
                    selected.append(card[1])
                    break
            elif card[1] == "K":
                if renum[1] != 4:
                    selected.append(card[0])
                    selected.append(card[1])
                    break
            elif card[1] == "A":
                if renum[0] != 4:
                    selected.append(card[0])
                    selected.append(card[1])
                    break

        return (selected)


def normal_c(cards,numbers):  # 判断葫芦
    selected = ['@']
    if numbers.count(3) == 0:
        return selected
    else:
        renum = list(reversed(numbers))
        for i in range(0, 13):
            if renum[i] == 3:
                tp = 14 - i
                if tp == 14:
                    re3 = "A"
                elif tp == 13:
                    re3 = "K"
                elif tp == 12:
                    re3 = "Q"
                elif tp == 11:
                    re3 = "J"
                elif tp == 10:
                    re3 = "1"
                else:
                    re3 = str(tp)
                selected[0] = re3
                num3 = 0
                for card in cards:
                    if card[1] == res3:
                        selected.append(card[0])
                        num3 += 1
                    if num3 == 3:
                        break
                renum[i] -= 3
                if (renum.count(0) + renum.count(1)) == 13:
                    selected = ["@"]
                    return selected
                else:
                    for j in range(0, 13):
                        if renum[j] == 2:
                            tp2 = 14 - j
                            if tp2 == 14:
                                re2 = "A"
                            elif tp == 13:
                                re2 = "K"
                            elif tp == 12:
                                re2 = "Q"
                            elif tp == 11:
                                re2 = "J"
                            elif tp == 10:
                                re2 = "1"
                            else:
                                re2 = str(tp)
                            selected[4] = re2
                            num2 = 0
                            for card in cards:
                                if card[1] == res2:
                                    selected.append(card[0])
                                    num2 += 1
                                if num2 == 2:
                                    break
                            break
                break
        return selected


def normal_d(cards, mark):  # 判断同花
    selected = ["@"]
    if mark.count[0 or 1 or 2 or 3 or 4] == 4:
        return selected
    else:
        weight = [0] * 5
        for i in range(0, 4):
            if mark[i] >= 5:
                if i == 0:  # 找出多于五张的花色
                    sym = '$'
                elif i == 1:
                    sym = '&'
                elif i == 2:
                    sym = '*'
                elif i == 3:
                    sym = '#'
                list2 = list_num_zu(cards, sym)  # 列出这种花色的所有牌号
                we = list(reversed(list2))  # 倒序
                for j in range(0, 5):
                    if we[j] > weight[j]:  # 若为最大权值
                        weight = we[:]
                        selected = we[:]
                        selected.append(sym)
                        break
                    elif we[j] == weight[j]:
                        continue
                    else:
                        break
        for t in range(0, 5):
            b = selected[t]
            if b == 14:
                selected[t] = "A"
            elif b == 13:
                selected[t] = "K"
            elif b == 12:
                selected[t] = "Q"
            elif b == 11:
                selected[t] = "J"
            elif b == 10:
                selected[t] = "1"
            else:
                selected[t] = str(b)
        return selected


def normal_e(cards, list_num):  # 判断顺子
    example = [[10, 11, 12, 13, 14], [9, 10, 11, 12, 13], [8, 9, 10, 11, 12], [7, 8, 9, 10, 11],
               [6, 7, 8, 9, 10], [5, 6, 7, 8, 9], [4, 5, 6, 7, 8], [3, 4, 5, 6, 7], [2, 3, 4, 5, 6]]

    selected = ["@"]
    set3 = set(list_num)
    for s in range(0, 9):
        set4 = set(example[s])
        rt = set4.issubset(set3)
        if rt:
            k = list(set4)
            selected = k[:]
            break
        else:
            continue
    for t in range(0, 5):
        b = selected[t]
        if b == 14:
            selected[t] = "A"
        elif b == 13:
            selected[t] = "K"
        elif b == 12:
            selected[t] = "Q"
        elif b == 11:
            selected[t] = "J"
        elif b == 10:
            selected[t] = "1"
        else:
            selected[t] = str(b)
    for d in range(0, 5):
        for card in cards:
            if card[1] == selected[d]:
                selected[d + 5] = card[0]
                break
    for d in range(0, 5):
        if selected[d] == "1":
            selected[d] = "10"
    return selected


def normal_f(cards, numbers):  # 判断三条
    selected = ["@"]
    if numbers.count(3) == 0:
        return selected
    else:
        n1 = 0
        n3 = 0
        sit = 4
        ren = list(reversed(numbers))
        for i in range(0, 13):
            if n3 < 1:
                if ren[i] == 3:
                    tp = 14 - i
                    if tp == 14:
                        re3 = "A"
                    elif tp == 13:
                        re3 = "K"
                    elif tp == 12:
                        re3 = "Q"
                    elif tp == 11:
                        re3 = "J"
                    elif tp == 10:
                        re3 = "1"
                    else:
                        re3 = str(tp)
                    selected[0] = re3
                    ren[i] -= 3
                    n3 += 1
            if n1 < 2:
                if ren[i] == 1:
                    tp = 14 - i
                    if tp == 14:
                        re1 = "A"
                    elif tp == 13:
                        re1 = "K"
                    elif tp == 12:
                        re1 = "Q"
                    elif tp == 11:
                        re1 = "J"
                    elif tp == 10:
                        re1 = "1"
                    else:
                        re1 = str(tp)
                    selected[sit] = re1
                    sit += 1
                    ren[i] -= 1
                    n1 += 1
            else:
                break
        n0 = 0
        n4 = 0
        n5 = 0
        for card in cards:
            if n4 < 1:
                if card[1] == selected[4]:
                    selected[6] = card[0]
                n4 += 1

            if n5 < 1:
                if card[1] == selected[5]:
                    selected[7] = card[0]
                n5 += 1

            if n0 < 3:
                n0 += 1
                if card[1] == selected[0]:
                    selected[n0] = card[0]
            else:
                break

        return selected


def normal_g(cards,numbers):  # 判断二对
    selected = ["@"]
    if numbers.count(2) < 2:
        return selected
    else:
        renum = list(reversed(numbers))
        n2 = 0
        n1 = 0
        f = 0
        for i in range(0, 13):
            if n1 < 1:
                if renum[i] == 1:
                    if tp == 14:
                        re1 = "A"
                    elif tp == 13:
                        re1 = "K"
                    elif tp == 12:
                        re1 = "Q"
                    elif tp == 11:
                        re1 = "J"
                    elif tp == 10:
                        re1 = "1"
                    else:
                        re1 = str(tp)
                    selected[6] = re1
                    renum[i] -= 1
                    n1 += 1
            if n2 < 2:
                if renum[i] == 2:
                    tp = 14 - i
                    if tp == 14:
                        re2 = "A"
                    elif tp == 13:
                        re2 = "K"
                    elif tp == 12:
                        re2 = "Q"
                    elif tp == 11:
                        re2 = "J"
                    elif tp == 10:
                        re2 = "1"
                    else:
                        re2 = str(tp)
                    selected[f] = re2
                    f += 3
                    renum[i] -= 2
                    n2 += 1
            else:
                break
        for a in range(1, 3):
            for card in cards:
                if card[1] == selected[0]:
                    selected[a] = card[0]
                    break
        for a in range(4, 6):
            for card in cards:
                if card[1] == selected[3]:
                    selected[a] = card[0]
                    break
        for card in cards:
            if card[1] == selected[6]:
                selected[7] = card[0]
                break
        return selected


def normal_h(cards, numbers):  # 判断一对
    selected = ["@"]
    if numbers.count(2) == 0:
        return selected
    else:
        n1 = 0
        n2 = 0
        f = 3
        ren = list(reversed(numbers))

        for i in range(0, 13):
            if n2 < 1:
                if ren[i] == 2:
                    tp = 14 - i
                    if tp == 14:
                        re2 = "A"
                    elif tp == 13:
                        re2 = "K"
                    elif tp == 12:
                        re2 = "Q"
                    elif tp == 11:
                        re2 = "J"
                    elif tp == 10:
                        re2 = "1"
                    else:
                        re2 = str(tp)
                    renum[i] -= 2
                    n2 += 1
                    selected[0] = re2

            if n1 < 3:
                if renum[i] == 1:
                    if tp == 14:
                        re1 = "A"
                    elif tp == 13:
                        re1 = "K"
                    elif tp == 12:
                        re1 = "Q"
                    elif tp == 11:
                        re1 = "J"
                    elif tp == 10:
                        re1 = "1"
                    else:
                        re1 = str(tp)
                    selected[f] = re1
                    renum[i] -= 1
                    n1 += 1
                    f += 1
            else:
                break

        for z in range(1, 3):
            for card in cards:
                if card[1] == selected[0]:
                    selected[z] = card[0]
                    break

        for z in range(3, 6):
            for card in cards:
                if card[1] == selected[z]:
                    selected[z + 3] = card[0]
                    break

        return selected


def dived(cards):    # 特殊牌型和散牌划分
    back[0]=cards[0] + " " + cards[1] + " " + cards[2]
    back[1]=cards[3] + " " + cards[4] + " " + cards[5] + " " + cards[6] + " " + cards[7]
    back[2]=cards[8] + " " + cards[9] + " " + cards[10] + " " + cards[11] + " " + cards[12]
    return back


def spec(mark, numbers):  # 检测有无特殊牌型
    if judge_spci1(mark, numbers) == 1:
        return 1
    elif judge_spci2(mark, numbers) == 1:
        return 1
    elif judge_spci3(mark, numbers) == 1:
        return 1
    elif judge_spci5(mark, numbers) == 1:
        return 1
    elif judge_spci6(mark, numbers) == 1:
        return 1
    elif judge_spci7(mark, numbers) == 1:
        return 1
    elif judge_spci_e(mark, numbers) == 1:
        return 1
    elif judge_spci8(mark, numbers) == 1:
        return 1
    elif judge_spci9(mark, numbers) == 1:
        return 1
    elif judge_spci_a(mark, numbers) == 1:
        return 1
    elif judge_spci_b(mark, numbers) == 1:
        return 1
    elif judge_spci_d(mark, numbers) == 1:
        return 1
    else:
        return 0


def make_list_num(cards):  # 将所有数字存入列表
    list_num=[]
    for card in cards:
        if card[1] == "1":
            list_num.append(10)
        elif card[1] == "J":
            list_num.append(11)
        elif card[1] == "Q":
            list_num.append(12)
        elif card[1] == "K":
            list_num.append(13)
        elif card[1] == "A":
            list_num.append(14)
        elif card[1] == "2":
            list_num.append(2)
        elif card[1] == "3":
            list_num.append(3)
        elif card[1] == "4":
            list_num.append(4)
        elif card[1] == "5":
            list_num.append(5)
        elif card[1] == "6":
            list_num.append(6)
        elif card[1] == "7":
            list_num.append(7)
        elif card[1] == "8":
            list_num.append(8)
        elif card[1] == "9":
            list_num.append(9)
       

    list_num=list(reversed(list_num) ) # list按大到小排序
    return list_num


def make_mark(cards):  # 统计各符号桶内的个数
    for card in cards:
        if card[0] == "$":
            mark[0] += 1
        elif card[0] == "&":
            mark[1] += 1
        elif card[0] == "*":
            mark[2] += 1
        elif card[0] == "#":
            mark[3] += 1
    return mark


def make_numbers(cards):  # 数字桶
    for card in cards:
        if card[1] == "2":
            numbers[0] += 1
        elif card[1] == "3":
            numbers[1] += 1
        elif card[1] == "4":
            numbers[2] += 1
        elif card[1] == "5":
            numbers[3] += 1
        elif card[1] == "6":
            numbers[4] += 1
        elif card[1] == "7":
            numbers[5] += 1
        elif card[1] == "8":
            numbers[6] += 1
        elif card[1] == "9":
            numbers[7] += 1
        elif card[1] == "1":
            numbers[8] += 1
        elif card[1] == "J":
            numbers[9] += 1
        elif card[1] == "Q":
            numbers[10] += 1
        elif card[1] == "K":
            numbers[11] += 1
        elif card[1] == "A":
            numbers[12] += 1
    return numbers


flag = 0  # 0:散牌   1:特殊牌型    2:普通牌型
back = [0]*3  # 返回值 字符串数组
list_num = []  # 数字列表 纯数字  之后用set()函数转为集合，用于计算顺子
mark = [0] * 4  # 符号桶
numbers = [0] * 13  # 数字桶

now_dun=[0]*5
mark = make_mark(cards)
numbers = make_numbers(cards)
list_num = make_list_num(cards)

print(cards)
print(mark)
print(numbers)
print(list_num)

flag = spec(mark, numbers)
if flag == 1:
    back = dived(cards)
else:
    for bp in range(0,2):  # 从第三墩开始找
        sec = normal_a(cards, mark)
        if sec[0] != "@":  # 找到同花顺！
            for i in range(0,5):
                if sec[i] == '1':
                    now_dun[i] = sec[5] + sec[i] + '0'
                else:
                    now_dun[i] = sec[5] + sec[i]
            # 开始清理数据
            for hp in now_dun:
                cards.remove(hp)
            mark = make_mark(cards)
            numbers = make_numbers(cards)
            list_num = make_list_num(cards)

            back[2 - bp] = " ".join(now_dun)

        else:
            sec = normal_b(cards, numbers)
            if sec[0] != "@":  # 找到炸弹！
                flag = 2
                if sec[0] == "1":
                    for i in range(0,4):
                        now_dun[i] = sec[i + 1] + "10"
                    now_dun[4] = sec[5] + sec[6]
                else:
                    for i in range(0,4):
                        now_dun[i] = sec[i + 1] + sec[0]
                    now_dun[4] = sec[5] + sec[6]
                # 开始清理数据
                for hp in now_dun:
                    cards.remove(hp)
                mark = make_mark(cards)
                numbers = make_numbers(cards)
                list_num = make_list_num(cards)

                back[2 - bp] = " ".join(now_dun)

            else:
                sec = normal_c(cards,numbers)
                if sec[0] != "@":  # 找到葫芦！
                    flag = 2
                    for w in range(0,3):
                        now_dun[w] = sec[w + 1] + sec[0]
                    for j in range(3,5):
                        now_dun[j] = sec[w + 2] + sec[4]
                    # 开始清理数据
                    for hp in now_dun:
                        cards.remove(hp)
                    mark = make_mark(cards)
                    numbers = make_numbers(cards)
                    list_num = make_list_num(cards)

                    back[2 - bp] = " ".join(now_dun)

                else:
                    sec = normal_d(cards, mark)
                    if sec[0] != "@":  # 找到同花！
                        flag = 2
                        for x in range(0,5):
                            now_dun[x] = sec[5] + sec[x]
                        # 开始清理数据
                        for hp in now_dun:
                            cards.remove(hp)
                        mark = make_mark(cards)
                        numbers = make_numbers(cards)
                        list_num = make_list_num(cards)

                        back[2 - bp] = " ".join(now_dun)

                    else:
                        sec = normal_e(cards, list_num)
                        if sec[0] != "@":  # 找到顺子！
                            flag = 2
                            for e in range(0,5):
                                if sec[e] == "1":
                                    now_dun[e] = sec[e + 5] + "10"
                                else:
                                    now_dun[e] = sec[e + 5] + sec[e]
                            # 开始清理数据
                            for hp in now_dun:
                                cards.remove(hp)
                            mark = make_mark(cards)
                            numbers = make_numbers(cards)
                            list_num = make_list_num(cards)

                            back[2 - bp] = " ".join(now_dun)
                        else:
                            sec = normal_f(cards, numbers)
                            if sec[0] != "@":  # 找到三条！
                                flag = 2
                                for tr in range(0,3):
                                    if sec[0] == "1":
                                        now_dun[tr] = sec[tr + 1] + "10"
                                    else:
                                        now_dun[tr] = sec[tr + 1] + sec[0]
                                for tr in range(3,5):
                                    if sec[tr + 1] == "1":
                                        now_dun[tr] = sec[tr + 3] + "10"
                                    else:
                                        now_dun[tr] = sec[tr + 3] + sec[tr + 2]
                                # 开始清理数据
                                for hp in now_dun:
                                    cards.remove(hp)
                                mark = make_mark(cards)
                                numbers = make_numbers(cards)
                                list_num = make_list_num(cards)

                                back[2 - bp] = " ".join(now_dun)

                            else:
                                sec = normal_g(cards,numbers)
                                if sec[0] != "@":  # 找到二对！
                                    flag = 2
                                    for b in range(0,2):
                                        if sec[0] == "1":
                                            now_dun[b] = sec[b + 1] + "10"
                                        else:
                                            now_dun[b] = sec[b + 1] + sec[0]
                                    for b in range(2,4):
                                        if sec[3] == "1":
                                            now_dun[b] = sec[b + 2] + "10"
                                        else:
                                            now_dun[b] = sec[b + 2] + sec[3]
                                    if sec[6] == "1":
                                        now_dun[4] = sec[7] + "10"
                                    else:
                                        now_dun[4] = sec[7] + sec[6]
                                    # 开始清理数据
                                    for hp in now_dun:
                                        cards.remove(hp)
                                    mark = make_mark(cards)
                                    numbers = make_numbers(cards)
                                    list_num = make_list_num(cards)

                                    back[2 - bp] = " ".join(now_dun)
                                else:
                                    sec = normal_h(cards, numbers)
                                    if sec[0] != "@":  # 找到一对！
                                        flag = 2
                                        for r in range(0,2):
                                            if sec[0] == "1":
                                                now_dun[r] = sec[r + 1] + "10"
                                            else:
                                                now_dun[r] = sec[r + 1] + sec[0]
                                        for r in range(2,5):
                                            if sec[r + 1] == "1":
                                                now_dun[r] = sec[r + 4] + "10"
                                            else:
                                                now_dun[r] = sec[r + 4] + sec[r + 1]
                                        # 开始清理数据
                                        for hp in now_dun:
                                            cards.remove(hp)
                                        mark = make_mark(cards)
                                        numbers = make_numbers(cards)
                                        list_num = make_list_num(cards)
                                        back[2 - bp] = " ".join(now_dun)
if flag != 2:
    back = dived(cards)

print(back)

















