# ==========================
# 导入第三方库
# ==========================
#发送http请求
import requests
#解析HTML网页结构
from bs4 import BeautifulSoup

import pandas as pd


# ==========================
# 创建空列表
# ==========================

books = []


# ==========================
# 循环爬取50页
# ==========================

for page in range(1, 51):

    # 第一页地址特殊处理
    if page == 1:

        url = "https://books.toscrape.com/"

    else:

        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    print(f"正在爬取第 {page} 页...")

    # 发送请求
    response = requests.get(url)

    # 解析网页
    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    # 获取当前页所有书籍
    for book in soup.find_all(
        "article",
        class_="product_pod"
    ):

        # 获取书名
        title = book.h3.a["title"]

        # 获取价格
        price = book.find(
            "p",
            class_="price_color"
        ).text

        # ==========================
        # 获取评分
        # ==========================

        rating_class = book.find("p")["class"][1]

        rating_dict = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5
        }

        rating = rating_dict[rating_class]

        # ==========================
        # 保存数据
        # ==========================

        books.append(
            [
                title,
                price,
                rating
            ]
        )


# ==========================
# 转DataFrame
# ==========================

df = pd.DataFrame(
    books,
    columns=[
        "书名",
        "价格",
        "评分"
    ]
)

print(df.head())

print(f"\n共获取 {len(df)} 条数据")

# ==========================
# 保存CSV
# ==========================

df.to_csv(
    "data/books.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\n保存成功！")