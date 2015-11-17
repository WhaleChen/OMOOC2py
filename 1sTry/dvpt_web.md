# Paas 版本 极简交互式笔记

## 要求：
- 通过固定域名访问系统；
- 一次接受输入一次笔记
- 服务端保存为文件
- 兼容3w Net 版本的命令行界面进行交互
- 获得当前笔记数量/访问数量等基础数据
- 可以获得所有笔记备份并归档

## 20151115
终于基本实现基于bottle的交互功能。

## 20151116开始尝试
- 工具：新浪云SAE  理解
- 部署：
    -svn： subversion 为了版本控制 [svn for windows](http://sourceforge.net/projects/win32svn/)
    -config.yaml
    -index.wsgi: 
- 基本配置参考：
    + [新浪云SAE](http://www.sinacloud.com/doc/sae/python/index.html)
	+ [小赖的Python学习笔记](https://wp-lai.gitbooks.io/learn-python/content/1sTry/sae.html)
	+ 说明：不得不看小赖，wp-lai 的速度也是我们的标杆！借助peer 真的发现wp-lai 理解问题的能力很强，不单学习，更要认真学习！
	+ [bottle todo list](http://bottlepy.org/docs/dev/tutorial_app.html)
	
### 坚固bottle
- bottle 的外部接口
- bottle 是必须的

### peer study~ 
- wp-lai 的速度也是我们的标杆！

### 本地开发
- 环境配置有些问题，一直思考最小代价，决定先放弃本地，等回过来再搞！

## 20151117 专注服务器保存文件
- 1116 用kvdb一直觉得需要改进，同时没有实名也让我有些不舒服，但是要实现功能必须有数据库
- 一直思考 数据库，有些郁闷，是否可以使用MySQL？总觉得 关系型数据库在处理 输入信息的时候更有利。
- 决定 使用 MySQL ，个人觉得kvdb 非常适合获得访问信息，不过关系性数据更适合我现在，也可以先学习一下网络关系数据库

### MySQL 分解任务
- 获得接口资料：
- bottle 配置接口
- 学习SQL语言基本操作
- 加入信息获取并保存信息

### 获得接口资料
- [新浪共享型数据库](http://www.sinacloud.com/doc/sae/python/mysql.html)
- [bottle-mysql](https://pypi.python.org/pypi/bottle-mysql/0.1.4)
- [The Python standard for database interfaces](http://www.tutorialspoint.com/python/python_database_access.htm)
- 资料显示 MySQLdb 是唯一的python db-api, sae 对于 MySQL 还是很好支持的。更惊喜的发现bottle-mysql是 MIT编写的！用plugin的方式放入bottle。我就如同放bottle.py, 放入bottle-mysql.py OK!

### bottle 配置接口
- 申请数据库：直接在新浪SAE 上申请共享型数据库，过程不复杂。记住app_<name>就是数据库名字，不用被PhpMyAdmin欺哄，认为是什么php 语言，我在这里愣了半天。
发现不用管这个名字，直接在网页操作，而deferredjob 和storage略过
- 建立第一张表：用来记录数据用的，这里直接可以在网上增加，有很多选项，不过不用担心，直接建立，之后可以更改，我建立了2 个字段。
- 用bottle 连接数据库：
    + 这里绕了很多圈子：
	"用户名　 : SAE_MYSQL_USER  密码 : SAE_MYSQL_PASS  主库域名:SAE_MYSQL_HOST_M 端口 : SAE_MYSQL_PORT 数据库名 : SAE_MYSQL_DB""
    + 看这个让我想到Socket 的结构，然后直接阅读bottle-mysql示意代码：
``` 
app =Bottle()
plugin =bottle_mysql.Plugin(dbuser='user',dbpass='pass',dbname='db')
app.install(plugin)
```
    用 这种形式来调用，那么 自然 想到 dbuser = SAE_MYSQL_USER ...

- 梗点：
    + bottle-mysql 在连接上有问题，后来发现 bottle-mysql 的源码非常小，小到让人惊叹！因此，第一次直接读源码，然后发现我其实不用bottle-mysql,更简单的方式是直接 import MySQLdb
	+ 用 db = MySQLdb.connect(host ="", port =, user ="", passwd ="", db="") 的形式,如果 user =SAE_MYSQL_USER .. 无法连接上，我突然感觉到一定有一些绝对常数，仔细搜索：
	+ [sae 数据库连接配置](http://shellbye.com/blog/tech_world/sae-mysql-config/) 终于被挖到了。才发现 可以直接用 w.rdc.sae.sina.com.cn 来放在host 里面
	+ [sae MySQL 连接实例](http://blog.csdn.net/querdaizhi/article/details/7337629) 也值得参考，提示梗点：只有一个数据库可以操作

### 学习SQL语言基本操作：
- [SQL 基本语法](http://www.w3school.com.cn/sql/sql_syntax.asp)
- [MySQL manual](http://dev.mysql.com/doc/)
- SQL语言比较规范，都用大写，比较容易区别

### 加入信息获取并保存信息
- 主要不会使用SQL，语句学得有些慢。先上了，赶上可以让大妈批评。

### 继续需要做的
- 输出是 一个很奇怪的 原是格式数据，需要去括号
- 时间加入，date格式数据
- 迭代


