"""
    autor: zqc
    date:  20190806
    version: v2.0
    feature: 模拟掷骰子
    feature: 2.0  两次掷骰子
"""

##导入随机数生成包
import random

##模拟掷骰子方法(函数)
def roll_dice():
    roll = random.randint(1, 6)
    return roll

def main():
    """
        主函数
    """
    ##限定随机次数
    total_times = 100
    ##初始化列表，存储随机数[0，0，0，0，0，0]
    result_list = [0] * 11

    ##初始化点数列表
    roll_list = list(range(2, 13))
    roll_dict = dict(zip(roll_list, result_list))

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()

        for j in range(2, 13):
            if (roll1 + roll2) == j:
                roll_dict[j] += 1

    for a, result in roll_dict.items():
        print('点数{}的次数:{},频率:{}.'.format(a, result, result / total_times))
    print(roll_dict)


if __name__ == '__main__':
    main()