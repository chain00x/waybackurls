# waybackurls
# 开vpn，http和https代理即可

使用方法：python3 waybackurls.py -f 输入txt文件 -o 输出txt文件 -u 单个域 -d 1(带入子域名)


# 1.通过根域名查询所有子域名（包括根域名）
```python3 waybackurls.py -d 1 -o output.txt -u example.com```

# 2.输出TXT文件
```python3 waybackurls.py -o output.txt -u example.com```

# 3.输入文件，循环url查询
```python3 waybackurls.py -f intput.txt```

正在写第二版，可以根据关键字过滤

欢迎各位师傅提建议和反馈
