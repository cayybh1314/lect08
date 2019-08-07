"""
    autor: zqc
    date:  20190807
    version: v5.0
    feature: 模拟掷骰子
    feature: 2.0  两次掷骰子
    feature: 3.0  可视化两次掷骰子结果。
    feature: 4.0   直方图展示结果
    feature: 5.0   科学计算
"""

##导入随机数生成包
#import random
import matplotlib.pyplot as plt
import numpy as np

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

##模拟掷骰子方法(函数)
def roll_dice():
    roll = random.randint(1, 6)
    return roll

def main():
    """
        主函数
    """
    ##限定随机次数
    total_times = 3
    ##初始化列表，存储随机数[0，0，0，0，0，0]
    # result_list = [0] * 11
    roll1_arr = np.random.randint(1, 7, size=total_times)
    roll2_arr = np.random.randint(1, 7, size=total_times)
    roll3_arr = np.random.randint(1, 7, size=total_times)
    rusult_arr = roll1_arr + roll2_arr + roll3_arr
    print('roll1_arr:{}+roll2_arr:{}+roll3_arr:{} = rusult_arr:{}'.format(roll1_arr, roll2_arr, roll3_arr, rusult_arr))


    # #记录骰子的结果
    # roll_list = []
    # roll1_list = []
    # roll2_list = []

    ##初始化点数列表
    # roll_list = list(range(2, 13))
    # roll_dict = dict(zip(roll_list, result_list))

    # for i in range(total_times):
    #     roll1 = roll_dice()
    #     roll2 = roll_dice()
    #
    #     roll_list.append(roll1+roll2)
    #     roll1_list.append(roll1)
    #     roll2_list.append(roll2)
    #
    #     for j in range(2, 13):
    #         if (roll1 + roll2) == j:
    #             roll_dict[j] += 1
    #
    # for a, result in roll_dict.items():
    #     print('点数{}的次数:{},频率:{}.'.format(a, result, result / total_times))
    # print(roll_dict)

    hist, bins = np.histogram(rusult_arr, bins=range(3, 19))
    print(hist)
    print(bins)

    ##数据可视化、针对上面的结果可视化
    # x = range(1, total_times + 1)
    # plt.scatter(x, roll1_list, c='red', alpha=0.5)
    # plt.scatter(x, roll2_list, c='green', alpha=0.5)
    # plt.show()
    tick_labels = []
    plt.hist(rusult_arr, bins=range(3, 19), normed=1, edgecolor='black', linewidth=1, rwidth=0.8)

    # 设置x轴坐标点显示
    tick_labels = ['3点', '4点', '5点',
                   '6点', '7点', '8点', '9点', '10点', '11点', '12点', '13点', '14点', '15点', '16点', '17点', '18点', '19点']
    tick_pos = np.arange(3, 19) + 0.5
    plt.xticks(tick_pos, tick_labels)

    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()


if __name__ == '__main__':
    main()
