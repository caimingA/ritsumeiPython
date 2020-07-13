# グラフ描画に必要なモジュール（NetworkX，Matplotlib）をインポート
import networkx as nx
import matplotlib.pyplot as plt

# 新たなグラフの作成
G = nx.Graph()

# グラフにエッジを追加（ノードは必要に応じて自動生成される）
G.add_edge("あ", "い")
G.add_edge("い", "う")
G.add_edge("う", "え")
G.add_edge("え", "お")
G.add_edge("お", "あ")
G.add_edge("あ", "う")

# グラフ描画領域の生成
plt.figure()

# ばねレイアウトでノードの配置（pos）を作成
pos = nx.spring_layout(G)

# グラフにノードを描画
nx.draw_networkx_nodes(G, pos)

# グラフにエッジを描画
nx.draw_networkx_edges(G, pos)

# グラフのノードにラベルを描画
nx.draw_networkx_labels(G, pos, font_family="IPAexGothic")

# 描画領域の軸を描画しない設定
plt.axis("off")

# グラフのウィンドウを表示
plt.show()
