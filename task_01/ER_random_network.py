# @Time    : 2023/4/16 14:41
# @Author  : wang song
# @File    : ER_random_network.py
# @Description : 第一个作业的代码，主要实现思路见同级目录下readme文件。
import networkx as nx
import matplotlib.pyplot as plt
import math


def plot_degree_distribution(n, p):
    """
    根据给出的不同n和p画出不同的度分布图
    :param n:顶点的个数
    :param p:ER随机图的边连接概率
    :return:
    """
    # 生成ER随机图
    ER = nx.erdos_renyi_graph(n, p)

    # 获取节点度分布
    degree_list = nx.degree_histogram(ER)

    # 计算节点度分布的横坐标和纵坐标的值
    x = range(len(degree_list))
    y = [degree_num / float(sum(degree_list)) for degree_num in degree_list]
    k = range(30)
    # 公式3.16
    pk = [(15 ** i) * (math.exp(-15)) / math.factorial(i) for i in k]

    # 画出度分布散点图和曲线图
    plt.plot(k, pk, color='red', linewidth=0.6)
    plt.scatter(x, y, color='blue', alpha=0.4, s=25)

    # x，y轴的标签及范围
    plt.xlabel('k')
    plt.ylabel('p(k)')
    plt.xlim(0, 35)
    plt.ylim(0, 0.12)
    plt.show()


# 可以尝试不同的n p ---> k = n * p
# plot_degree_distribution(1000, 0.015)
plot_degree_distribution(10000, 0.0015)
# plot_degree_distribution(100, 0.15)
