"""
    autor: zqc
    date:  20190806
    version: v1.0
    feature: 模拟掷骰子
"""

##导入随机数生成包
import random

##模拟掷骰子方法(函数)
def roll_dice():
    roll = random.randint(1,6)
    return roll

def main():
    """
        主函数
    """
    ##限定随机次数
    total_times = 100000
    ##初始化列表，存储随机数[0，0，0，0，0，0]
    result_list = [0] * 6

    for i in range(total_times):
        roll = roll_dice()
        for j in range(1,7):
            if roll == j:
                result_list[j - 1] += 1

    for a,result in enumerate(result_list):
        print('点数{}的次数:{},频率:{}.'.format(a,result,result / total_times))
    print(result_list)


if __name__ == '__main__':
    main()