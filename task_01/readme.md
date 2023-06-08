`本文档主要介绍完成第一个作业的思路`
1. 根据给定的顶点个数n和边连接概率p，使用networkx中的erdos_renyi_graph()函数生成ER随机图。
2. 利用networkx中的degree_histogram(ER)计算图中节点的度分布，得到度分布列表。
3. 将书上p85、p86度分布及期望度分布相关计算公式使用python代码实现。
4. 使用matplotlib画出ER模型的度分布图(可以运行代码看，也可以看同级目录下的.png文件)
5. 通过观察画出来的图，可以看到，实际度分布(离散点)和理论的度分布的偏离很少。
6. 将以上代码封装成函数plot_degree_distribution(n, p)，可以根据需要更改参数，提高代码的复用性。