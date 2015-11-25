# 微信版的情绪日记——寻找心流状态

## 缘起：
- 编程让我感觉到情绪对于心流状态的影响异常大，尤其是面对自己并不熟悉的领域，那个comfort zone之外的世界原来把手者有很多是自己的卫兵。
- 因此，内心萌生了一个小小的愿望，希望记录情绪中的细节，观察自己的情绪波动特征，以及对行为的影响，让自己更多的属于心流状态中。
- 在Cnfeat 教练 的提点下，我发现自己可以开发情绪日记——通过实时记录来发觉自己情绪的梗，帮助自己和别人更好的进入心流状态。
- 而手机是最佳的随手记的载体 微信手机应用是最佳的平台，因此，就有了希望实践情绪日记的雏形。
 
##拆解目标：
- 微信的创建到token认证
- 本地化测试
- 数据库备份和数据处理
- 情绪日记的构想
 
## 他山之石，可以攻玉
- 首先感谢小赖，他的日记非常充分而且周到的将微信的创建到token认证的方式彻彻底底讲清楚了
- 小赖的笔记 [小赖的Python学习笔记](https://wp-lai.gitbooks.io/learn-python/content/1sTry/wechat.html)
- 梗点：我发现，我在写 token 密码后多加了一个‘,’ 实在让我用了2个天 郁闷找不出错误的原因。
- [使用python一步一步搭建微信公众平台](http://my.oschina.net/yangyanxing/blog/159215)
- 这篇博文非常细致的描述了如何一步一步搭建微信公共平台，真的一步一步，和小赖的笔记一起读，非常有帮助。

## 完成echo，偷懒的本地化测试
- 由于希望模仿 微信的输出，我用了一个本地化的偷懒的办法，小赖的方法太高深了对我。我先用一个简单的。

Server:
```
@app.post('/')
def get_data():
        import xml.etree.ElementTree as ET
	str_xml =request.body.read()
	xml = ET.fromstring(str_xml)
	content =xml.find("Content").text
	msgType =xml.find("MsgType").text
	fromUser =xml.find("FromUserName").text
	toUser=xml.find("ToUserName").text
	createtime = int(time.time())
		return '''
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%s]]></Content>
</xml>
	'''%(fromUser, toUser, createtime, content)
    
debug(True)
run(app, host='localhost', port =8080,reloader=True)
```


- 如何仿造 微信端呢？ 用 requests

```
import requests
from bs4 import BeautifulSoup

content =raw_input('>>>')
value = '''
<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName>
<CreateTime>1348831860</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%s]]></Content>

</xml>
'''%(content)


url = "http://localhost:8080"
r = requests.post(url,data = value)
print str(r)
print r.url
print r.text
```


## 数据库： 继续使用 MySQL：
- 用MySQL 是源于自己希望在之后能够做一个心流的统计。这样方便我的数据管理。
- 由于 tag 在MySQL也方便，MySQL的数据结构也清晰，就继续用吧！

## 情绪日记的初步构想：寻找那份属于自己的独一无二的心流状态
- 每个人都不一样。
- 人并不清楚自己的样式：持续不断的记录和统计有助于帮助人认识到自己。
- 情绪日记：着重于通过简单记录来寻找出情绪、行为和心流状态的关联

## 实践：
- 实现第一个功能：心流状态的持续记录
- [Google Py Styl](http://zh-google-styleguide.readthedocs.org/en/latest/google-python-styleguide/) 发现当编码量上去了，非多看不可
- 发现自己忠于自己的本性的结果就是代码累赘有不靠谱 
- 类似错误和出现很多，这个代码权当改错的原件
``` 
if len(users) == 0
```
- 自以为终于在一个py中就到了200行，发现原来自己是那么累赘~多读 GPS！！！

