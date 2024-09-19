from io import StringIO
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import matplotlib.pyplot as plt

url="https://dmuller.net/earthquakes-daily-monitor/"
response = requests.get(url)





if response.ok:
    print("Data is ready")
    
    # 使用 BeautifulSoup 解析 HTML
    soup = bs(response.text, 'html.parser')
    # 找到包含数据的表格（假设数据在第一个表格中）
    table = soup.find('table')  # 根据实际情况选择合适的选择器



type(table)

table_str = str(table)
    
    # 使用 StringIO 包装字符串
table_io = StringIO(table_str)
    
    # 使用 pandas 读取 HTML 表格
df = pd.read_html(table_io, header=1)[0]
    
    # 打印数据框

print(df)




df.shape[1]



df=df.values


df = pd.DataFrame(df, columns=['Date', 'Value1', 'Value2', 'Value3'])

# 打印原始 DataFrame
print("Original DataFrame:")
print(df)

# 将第一列转换为 datetime 格式
df['Date'] = pd.to_datetime(df['Date'])

# 将其他列转换为浮点数
df['Value1'] = df['Value1'].astype(float)
df['Value2'] = df['Value2'].astype(float)
df['Value3'] = df['Value3'].astype(float)




plt.style.use('ggplot')

# 创建一个新的图形
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制 Value1 的折线图，并设置图例标签为 'events'
ax.plot(df['Date'], df['Value1'], marker='o', label='events')

# 绘制 Value2 的折线图，并设置图例标签为 'strongest'
ax.plot(df['Date'], df['Value2'], marker='s', label='strongest')

# 绘制 Value3 的折线图，并设置图例标签为 'single event equivalent'
ax.plot(df['Date'], df['Value3'], marker='^', label='single event equivalent')

# 设置标题和标签
ax.set_title('Values over Time')
ax.set_xlabel('Date')
ax.set_ylabel('Values')

# 显示图例
ax.legend()

# 自动旋转日期标签
plt.xticks(rotation=45)

