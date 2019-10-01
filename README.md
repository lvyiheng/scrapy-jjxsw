# scrapy-jjxsw
scrapy 集成 selenium 的久久小说网下载器

## 环境配置
python 3.6

selenium

chromedriver

## 修改配置

```GENRE = "Young" # Chuanyue, Young, chongshengxiaoshuo, Lsjs```

修改成喜欢的小说类型，其中Young为现在言情，Chuanyue为穿越小说，chongshengxiaoshuo为重生小说，Lsjs为历史架空

```EXECUTABLE_PATH = "/usr/local/share/"```

！！！重要！！！修改成自己的chromedriver程序路径

```HEADLESS = True # 浏览器不提供可视化页面```

False为不可视化


## 运行

```python3 run.py```
