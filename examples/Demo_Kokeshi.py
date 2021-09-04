import time
import pandas as pd
from Pyfhel import Pyfhel, PyPtxt, PyCtxt

he = Pyfhel()           # 空のPyfhelオブジェクトを生成
he.contextGen(p=65537, m=2**13, flagBatching=True)  #コンテキストを初期化 m=8192
he.keyGen()             # 鍵を生成

enc1, enc2 = he.encryptInt(1), he.encryptInt(2)
enc3, enc4 = he.encryptInt(1), he.encryptInt(2)
plain1, plain2 = 1, 2
plain3, plain4 = 1, 2

df_add = pd.DataFrame(index=[],columns=['noiseLevel(add_Int)', 'result(add_Int)', 'grand truth(add_Int)'])
df_mul = pd.DataFrame(index=[],columns=['noiseLevel(mul_Int)', 'result(mul_Int)', 'grand truth(mul_Int)'])

for i in range(10):
    he.add(enc1, enc2) # 加算
    he.multiply(enc3, enc4) # 乗算
    plain1 = plain1 + plain2
    plain3 = plain3 * plain4
    s1 = pd.Series([he.noiseLevel(enc1),  he.decryptInt(enc1), plain1], index=df_add.columns)
    s2 = pd.Series([he.noiseLevel(enc3),  he.decryptInt(enc3), plain3], index=df_mul.columns)
    df_add = df_add.append(s1, ignore_index=True )
    df_mul = df_mul.append(s2, ignore_index=True )

df_add.to_csv("df_add.csv", sep=",")
df_mul.to_csv("df_mul.csv", sep=",")
