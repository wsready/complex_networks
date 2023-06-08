# @Time    : 2023/4/20 20:32
# @Author  : wang song
# @File    : WS_smallworld_network.py
# @Description : 第一个作业的代码，主要实现思路见同级目录下readme文件。
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def plot_smallworld_network(N, K, samples):
    """
    生成并画出一个小世界网络的图，图中包含不同重连概率下的平均集聚系数和平均最短路径长度的变化情况
    :param N:小世界网络的节点数
    :param K:每个节点的邻居数
    :param samples:进行多次采样，以获取在每个重连概率下的平均集聚系数和平均最短路径长度的稳定估计
    :return:
    """
    # p_list为重连概率列表，利用np.logspace()生成从0.0001到1的10个等比递增的元素，用于表示重连概率p的不同取值
    p_list = np.logspace(0, 4, samples) / 10000

    # 声明两个list来装填平均集聚系数(C)和平均最短路径长度(L)
    C = []
    L = []

    # 计算不同重连概率下的平均集聚系数(C)和平均最短路径长度(L)
    for p in p_list:
        # 存储每次采样得到的集聚系数和最短路径长度
        clustering_values = []
        path_length_values = []

        # 循环采样
        for _ in range(samples):
            # 生成一个小世界网络，其中节点数为N,邻居数为K,重连概率为p
            G = nx.watts_strogatz_graph(N, K, p)
            # 计算当前重连概率下的小世界网络的集聚系数,并将其追加到之前声明的clustering_values[]中
            clustering_values.append(nx.average_clustering(G))
            # 由于重连操作可能会导致某些节点之间的连接被打破,使用try-except捕获异常并处理
            try:
                # 计算当前重连概率下的小世界网络的最短路径长度，并将其追加到之前声明的path_length_values[]中
                path_length_values.append(nx.average_shortest_path_length(G))
            except nx.NetworkXError:  # 抛出异常
                pass

        # 利用np.mean()计算clustering_values[]和path_length_values[]中的平均值，并分别将其追加到之前声明的C和L中
        C.append(np.mean(clustering_values))
        L.append(np.mean(path_length_values))

    # 画出WS小世界网络的集聚系数和平均距离随重连概率p的变化关系
    plt.plot(p_list, np.array(C) / C[0], 'ro', label='$C(p)/C(0)$')
    plt.plot(p_list, np.array(L) / L[0], 'bs', label='$L(p)/L(0)$')
    plt.legend(loc=0, fontsize=10)
    plt.xlabel("$p$")
    plt.xscale("log")
    plt.show()


# 调用函数
plot_smallworld_network(N=1000, K=10, samples=10)
