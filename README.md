# Udacity_subtitle_work

因为经常要手动找和打开与字幕相应的文件，于是就写了这么一个小小的脚本，将步骤做做减法。省下的时间就可以多看部电影了～

利用 Google 文档导出的 csv：
- 自动打开与课程名字相对应的文件
- 显示还没有完成的字幕

## 环境需求
- Mac
- Python 3
- [rows](https://github.com/turicas/rows) 库的安装

## 使用

### 自动打开程序
```
python auto_open.py
```
复制文字就会打开与标题相应的字幕文件, 下面的视频是个例子：

[![youtube example](https://i.ytimg.com/vi/sU2HHUAgZGA/2.jpg?time=1497189926980)](https://www.youtube.com/watch?v=sU2HHUAgZGA)

### 找出未完成的
找出未完成的校对，按校对截止日期排列
```
find_unfinished.py
```
