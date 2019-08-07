"""
    autor: zqc
    date:  20190806
    version: v3.0
    feature: 模拟掷骰子
    feature: 2.0  两次掷骰子
    feature: 3.0  可视化两次掷骰子结果。
"""

##导入随机数生成包
import random
import matplotlib.pyplot as plt

##模拟掷骰子方法(函数)
def roll_dice():
    roll = random.randint(1, 6)
    return roll

def main():
    """
        主函数
    """
    ##限定随机次数
    total_times = 6
    ##初始化列表，存储随机数[0，0，0，0，0，0]
    result_list = [0] * 11

    #记录骰子的结果
    roll1_list = []
    roll2_list = []

    ##初始化点数列表
    roll_list = list(range(2, 13))
    roll_dict = dict(zip(roll_list, result_list))

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll1_list.append(roll1)
        roll2_list.append(roll2)

        for j in range(2, 13):
            if (roll1 + roll2) == j:
                roll_dict[j] += 1

    for a, result in roll_dict.items():
        print('点数{}的次数:{},频率:{}.'.format(a, result, result / total_times))
    print(roll_dict)

    ##数据可视化、针对上面的结果可视化
    x = range(1, total_times + 1)
    plt.scatter(x, roll1_list, c='red', alpha=0.5)
    plt.scatter(x, roll2_list, c='green', alpha=0.5)
    plt.show()


if __name__ == '__main__':
    main()
