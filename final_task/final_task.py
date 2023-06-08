# @Time    : 2023/6/4 15:36
# @Author  : wang song
# @File    : final_task.py
# @Description : 期末考核代码实现
import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt


def create_scale_free_network(N, m):
    """
    创建BA无标度网络
    :param N: 节点数量
    :param m: 新增节点时与现有节点建立的边数
    :return: G: 创建的BA无标度网络
    """
    G = nx.barabasi_albert_graph(N, m)
    return G


def play_game(G, decisions):
    """
    进行决策博弈
    :param G: BA无标度网络
    :param decisions: 节点的决策行为数组
    :return: 节点的效益数组
    """
    N = len(decisions)
    utilities = np.zeros(N)
    # 定义决策博弈的规则
    for i in range(N):
        for neighbor in G.neighbors(i):
            if decisions[i] == 'A' and decisions[neighbor] == 'A':
                utilities[i] += 3
            elif decisions[i] == 'A' and decisions[neighbor] == 'B':
                utilities[i] += 0
            elif decisions[i] == 'B' and decisions[neighbor] == 'A':
                utilities[i] += 5
            elif decisions[i] == 'B' and decisions[neighbor] == 'B':
                utilities[i] += 1

    return utilities


def update_decisions(G, decisions, utilities):
    """
    更新决策行为
    :param G: BA无标度网络
    :param decisions: 节点的决策行为数组
    :param utilities: 节点的效益数组
    :return:
    """
    N = len(decisions)

    for i in range(N):
        # 随机选择一个邻居进行决策学习
        neighbor = random.choice(list(G.neighbors(i)))
        utility_diff = utilities[i] - utilities[neighbor]
        # 考核内容所给概率
        p = 1 / (1 + np.exp(utility_diff / 0.5))

        # 设置一个随机数与p比较，满足条件则更新自己的决策行为
        if random.random() >= p:
            decisions[i] = decisions[neighbor]


def simulate_game(N, m, num_rounds):
    """
    仿真无标度网络上的博弈决策过程，并绘制选择A决策行为的比例随时间的变化曲线
    :param N: 节点数量
    :param m: 新增节点时与现有节点建立的边数
    :param num_rounds: 仿真的轮数
    :return:
    """
    # 创建一个BA无标度网络
    G = create_scale_free_network(N, m)

    # 初始化决策行为
    decisions = np.random.choice(['A', 'B'], size=N)
    # 存储选择A决策行为的比例随时间的变化
    proportions = []

    # 进行10000轮博弈决策
    for _ in range(num_rounds):
        # 计算选择A的概率
        count_A = np.count_nonzero(decisions == 'A')
        proportion_A = count_A / N
        proportions.append(proportion_A)

        # 博弈之后得到的效益,以及更新效益
        utilities = play_game(G, decisions)
        update_decisions(G, decisions, utilities)

    # 绘制个体选择A决策行为的比例随时间的变化曲线
    plt.plot(proportions)
    plt.xlabel('Time')
    plt.ylabel('Proportion of individuals choosing A')
    plt.title('Evolution of Decision Behavior in a Scale-Free Network')
    plt.show()


# 设置参数并执行
N = 1000
m = 2
num_rounds = 10000
simulate_game(N, m, num_rounds)
