class Car:
    # コンストラクタ（オブジェクト作成時に自動的に実行される特別なメソッド）
    def __init__ (self, n):
        self.num = n;	# 車のナンバー
        self.gas = 0.0;	# ガソリン量
        print("ナンバー" + str(self.num) + "の車を作成しました")

    # ガソリンを補充するメソッド
    def put_gas(self, g):
        self.gas += g
        print("ナンバー" + str(self.num) + "にガソリンを" + str(g) + "l補充しました");

    # 現在のガソリン量を返すメソッド
    def get_gas(self):
        return self.gas

# ここから実行が始まる
car1 = Car(1234)	# ナンバー1234の自動車car1を作成

# 自動車car1に対する操作（メソッドの呼び出し）
print("car1のガソリン量は" + str(car1.get_gas()) + "lです")
car1.put_gas(10.0)	# car1のput_gas()メソッドを呼び出す
car1.put_gas(20.0)	# car1のput_gas()メソッドを呼び出す
print("car1のガソリン量は" + str(car1.get_gas()) + "lです")
