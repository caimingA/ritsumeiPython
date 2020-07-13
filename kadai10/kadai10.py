import networkx as nx
import matplotlib.pyplot as plt


def read_doc_sim():
    flag = 0
    names = dict()
    matrix = list()
    f = open("doc_sim.txt", encoding="UTF-8")
    for line in f:
        line = line.replace('\n', "")
        if flag == 0:
            nameList = line.split(',')
            for name in nameList:
                names[name] = 0
            flag = 1
        else:
            valueList = line.split(',')
            values = [float(i) for i in valueList]
            matrix.append(values)
    f.close()
    return names, matrix


def read_sports(names):
    colors = {'b': 'red', 'f': 'blue', 't': 'yellow', 'v': 'violet'}
    f = open("sports.txt", encoding="utf-8")
    idAndNames = dict()
    for line in f:
        # print(line)
        line = line.replace('\n', '').split('\t')
        # print(line[0])
        if line[0] in names:
            names[line[0]] = colors[line[1]]
    f.close()
    index = 0

    for key, value in names.items():
        idAndNames[index] = [key, value]
        index += 1
    # print(names)
    # print(idAndNames)
    return idAndNames


def draw(matrix, names, idAndNames):
    G = nx.Graph()
    n_color = list()
    for row, values in enumerate(matrix):
        for col, value in enumerate(values):
            # print(value)
            if value > 0.65:
                # print(value)
                G.add_edge(idAndNames[row][0], idAndNames[col][0])
                G.edges[idAndNames[row][0], idAndNames[col][0]]["weight"] = value

    for node in nx.nodes(G):
        # print(type(node))
        n_color.append(names[node])
    print(len(n_color), n_color)

    # # グラフ描画領域の生成（9.5インチ×9.5インチ）
    plt.figure(figsize=(9.5, 9.5))

    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    pos = nx.spring_layout(G, k=0.5)

    nx.draw_networkx_nodes(G, pos, node_color=n_color, alpha=0.8)
    nx.draw_networkx_edges(G, pos, edge_color="orange", alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_family="IPAexGothic", font_size=12)

    plt.axis("off")
    plt.savefig("result_k=0.5_value=0.65.png")
    plt.show()


if __name__ == "__main__":
    names, matrix = read_doc_sim()
    idAndNames = read_sports(names)
    draw(matrix, names, idAndNames)
