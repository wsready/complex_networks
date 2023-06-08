# @Time    : 2023/6/4 15:36
# @Author  : wang song
# @File    : final_task.py
# @Description : 解题思路如下
# 1. N=1000个节点组成的BA无标度网络可以用networkX库中的nx.barabasi_albert_graph(N, m)'函数来生成。
# 其中每个节点代表一个决策个体，并且具有连接的节点可以进行博弈决策。每个个体可以选择两种决策行为：A和B。
# 2. 在每一轮的博弈决策过程中，有两个阶段：博弈阶段和决策更新阶段。
#    1. 首先在博弈阶段，每个个体与其邻居进行博弈，根据与邻居的决策行为获得效益。
#       当A决策个体与A决策个体博弈时，效益为3。
#       当A决策个体与B决策个体博弈时，效益为0。
#       当B决策个体与A决策个体博弈时，效益为5。
#       当B决策个体与B决策个体博弈时，效益为1。
#    2. 在博弈阶段结束后，每个个体需要更新自己的决策行为。
#    3. 更新决策行为时，个体i会随机选择一个邻居j进行决策学习，同时个体i将自己的决策行为调整为个体j的决策行为为概率p。p=1/(1+exp[(𝑈𝑖−𝑈𝑗)/0.5])，其中𝑈𝑖和𝑈𝑗分别代表个体i和个体j的累加效益。
# 3. 最后再用matplotlib库画出来群体中选择A决策行为个体的比例在10000轮博弈决策过程中随时间的变化曲线。
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
        neighbor = random.choice(list(G.neighbors(i)))
        utility_diff = utilities[i] - utilities[neighbor]
        p = 1 / (1 + np.exp(utility_diff / 0.5))

        if random.random() < p:
            decisions[i] = decisions[neighbor]


def simulate_game(N, m, num_rounds):
    """
    仿真无标度网络上的博弈决策过程，并绘制选择A决策行为的比例随时间的变化曲线
    :param N: 节点数量
    :param m: 新增节点时与现有节点建立的边数
    :param num_rounds: 仿真的轮数
    :return:
    """
    G = create_scale_free_network(N, m)
    decisions = np.random.choice(['A', 'B'], size=N)
    proportions = []

    for _ in range(num_rounds):
        count_A = np.count_nonzero(decisions == 'A')
        proportion_A = count_A / N
        proportions.append(proportion_A)

        utilities = play_game(G, decisions)
        update_decisions(G, decisions, utilities)

    # 绘制个体选择A决策行为的比例随时间的变化曲线
    plt.plot(proportions)
    plt.xlabel('轮次')
    plt.ylabel('选择 A 决策行为个体的比例')
    # plt.title('Evolution of Decision Behavior in a Scale-Free Network')
    plt.show()


# 设置参数并执行
N = 1000
m = 2
num_rounds = 10000
simulate_game(N, m, num_rounds)
