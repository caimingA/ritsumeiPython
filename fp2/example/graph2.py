# グラフ描画に必要なモジュール（NetworkX，Matplotlib）をインポート
import networkx as nx
import matplotlib.pyplot as plt

# 新たなグラフの作成
G = nx.Graph()

# グラフにエッジを追加（各エッジの重みを指定）
G.add_edge("あ", "い", weight=16.0)
G.add_edge("い", "う", weight=8.0)
G.add_edge("う", "え", weight=4.0)
G.add_edge("え", "お", weight=2.0)
G.add_edge("お", "あ", weight=1.0)

# グラフ描画領域の生成（9.5インチ×9.5インチ）
plt.figure(figsize=(9.5, 9.5))

# 余白の調整（デフォルトより余白を狭くする）
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)

# ばねレイアウトでノードの配置（pos）を作成
# ノード間の反発力kを0.5に設定（kが大きいほどノード間の距離が離れる）
pos = nx.spring_layout(G, k=0.5)

# 各ノードの大きさをリストn_sizeに格納
n_size = [ 5000, 4000, 3000, 2000, 1000 ]

# 各ノードの色をリストn_colorに格納
n_color = [ "red", "blue", "green", "violet", "yellow" ]

# グラフにノードを描画
# （各ノードのサイズをn_sizeで指定，色をn_colorで指定，透明度を0.8に指定）
nx.draw_networkx_nodes(G, pos, node_size=n_size, node_color=n_color, alpha=0.8)

# 各エッジの太さをリストe_widthに格納
# （エッジの重みの値を太さに指定）
e_width = [G[u][v]["weight"] for u, v in G.edges]

# グラフにエッジを描画
# （色をオレンジに指定，各エッジの太さをe_widthで指定，透明度を0.5に指定）
nx.draw_networkx_edges(G, pos, edge_color="orange", width=e_width, alpha=0.5)

# グラフのノードにラベルを描画
# （フォントサイズを20ポイントに指定）
nx.draw_networkx_labels(G, pos, font_family="IPAexGothic", font_size=20)

# 描画領域の軸を描画しない設定
plt.axis("off")

# グラフのウィンドウを表示
plt.show()
