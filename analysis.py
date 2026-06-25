# ==========================
# 导入库
# ==========================

import pandas as pd
import matplotlib.pyplot as plt


# ==========================
# 解决中文显示问题
# ==========================

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


# ==========================
# 读取数据
# ==========================

df = pd.read_csv(
    "data/books.csv"
)

print(df.head())


# ==========================
# 数据清洗
# ==========================

# 删除英镑符号
df["价格"] = (
    df["价格"]
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
)

# 转换数字类型
df["价格"] = df["价格"].astype(float)

print("\n价格统计：")
print(df["价格"].describe())

# ==========================
# 价格分布图
# ==========================

plt.figure(figsize=(10, 6))

# bins=20
# 将价格划分为20个区间
plt.hist(
    df["价格"],
    bins=20
)

plt.title("图书价格分布")
plt.xlabel("价格")
plt.ylabel("数量")

plt.savefig(
    "price_distribution.png"
)

plt.show()

# ==========================
# 最贵10本书
# ==========================

top10 = (
    df.sort_values(
        by="价格",
        ascending=False
    )
    .head(10)
)

print("\n最贵10本书：")
print(top10)


plt.figure(figsize=(12, 6))

plt.bar(
    top10["书名"],
    top10["价格"]
)

plt.title("最贵10本书")
plt.xlabel("书名")
plt.ylabel("价格")

plt.xticks(
    rotation=45,
    ha="right"
)

plt.tight_layout()

plt.savefig(
    "top10_expensive_books.png"
)

plt.show()

# ==========================
# 评分统计
# ==========================

rating_count = (
    df["评分"]
    .value_counts()
    .sort_index()
)

print("\n评分统计：")
print(rating_count)


plt.figure(figsize=(8, 5))

plt.bar(
    rating_count.index,
    rating_count.values
)

plt.title("图书评分分布")
plt.xlabel("评分")
plt.ylabel("数量")

plt.savefig(
    "star_rating_distribution.png"
)

plt.show()