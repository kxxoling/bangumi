Bangumi 新番表计划
---------

本项目旨在建设一个简单易用的 Bangumi 网站供个人使用，并提供极影字幕组的相关链接。


如何部署
---------

Ubuntu 系统上需安装相应工具

```
apt-get install python-dev build-essentials python-pip python-lxml
```

使用 pip 安装相关依赖：

```
pip install -r requirements.txt
```

建议使用 virtualenv 部署环境，建议使用 Gunicorn 部署应用：

```
gunicorn -D -w 4 wsgi:app
```

为 ktxprsspider.py 添加可执行权限：

```
chmod +x ktxprsspider.py
```

使用 crond 部署自动脚本任务:

```
crontab -e
```

选择编辑器后添加下面一行：

```
0 */2 * * * /YOUR/PATH/TO/BANGUMI/ktxprssspider.py
```