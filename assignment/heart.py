

import os
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel

import imageio.v2 as imageio
from matplotlib import colors
import wordcloud  # 导入词云图模块

def main_gui():
    app = QApplication(sys.argv)  # PyQt6应用程序框架
    window = QWidget()

    layout_h1 = QHBoxLayout(window)  # 界面布局

    layout_v = QVBoxLayout(window)
    layout_v.setSpacing(20)
    layout_v.addStretch(1)

    layout_h2 = QHBoxLayout(window)
    label1 = QLabel(window)  # 控件设置
    label1.setText("Your Name:")
    layout_h2.addWidget(label1)
    edit = QLineEdit("")
    edit.setMaximumWidth(100)
    layout_h2.addWidget(edit)
    layout_v.addLayout(layout_h2)

    layout_h3 = QHBoxLayout(window)
    button = QPushButton("Submit")
    button.setFixedSize(100, 30)

    def on_button_click():  # 按钮事件定义
        word = edit.text()

        pic = imageio.imread('heart.png')  # 背景图形，如果根据图片绘制，则需要设置

        color_list = ['deeppink', 'pink']
        colormap = colors.ListedColormap(color_list)  # matplotlib色图

        wc = wordcloud.WordCloud(
            mask=pic,
            colormap=colormap,
            font_path='simhei.ttf',  # 字体
            background_color='black',  # 背景颜色
            max_words=200,  # 最大单词数量
            max_font_size=70,  # 最大字体大小
            repeat=True,
            scale=1)  # 缩放比例
        wc.generate(word)  # 生成词云

        # 显示词云图
        wc.to_file('wordcloud.png')
        pixmap = QPixmap('wordcloud.png')
        label2.setStyleSheet("border-radius:20px;background-color:black;")  # 倒圆角
        label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label2.setPixmap(pixmap)
        layout_h1.addWidget(label2)
        os.remove('wordcloud.png')

    button.clicked.connect(on_button_click)  # 注册按钮事件
    layout_h3.addWidget(button)
    layout_v.addLayout(layout_h3)
    layout_v.addStretch(1)
    layout_v.addStretch(1)

    layout_h1.addStretch(1)
    layout_h1.addLayout(layout_v)
    layout_h1.addStretch(1)
    layout_h1.addStretch(1)
    layout_h1.addStretch(1)
    layout_h1.addStretch(1)
    label2 = QLabel(window)
    label2.setFixedWidth(440)  # 设置图片显示区域大小
    label2.setFixedHeight(440)
    layout_h1.addWidget(label2)

    window.showMaximized()
    window.setWindowTitle('爱心')
    window.show()
    sys.exit(app.exec())

main_gui()


