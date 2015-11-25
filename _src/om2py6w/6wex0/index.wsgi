#-*- coding:utf-8 -*-
#author: WhaleChen

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from bottle import Bottle, run,template,request,debug
import sae
import sae.const  #这里储存了 sae中包括用户信息的值
import MySQLdb
import time 

app=Bottle()

@app.route('/')
def mainpage():
        # 主页显示欢迎界面，同时提供当下时间
        return template('welcome',diaryWritten1="当下时间是：" + time.strftime('%Y-%m-%d %H:%M:%S'),diaryWritten2 = 'Welcome All !',diaryWritten3 = '欢迎大家来到这里!', diaryWritten4 ='写完日记后按下写入!Enjoy the journey')
@app.route('/write',method='POST')
def write():
        db = MySQLdb.connect(host =sea.const.MYSQL_HOST, port =int(sae.const.MYSQL_PORT), user =sae.const.MYSQL_USER, passwd =sae.const.MYSQL_PASS, db=sae.const.MYSQL_DB) #对用户信息引用的方式
        cursor =db.cursor() #连接数据库后获取光标
        diaryInput =request.forms.get('diaryInput') #输入值获取
	if "<" in diaryInput:
	    diaryInput ='Thanks! this is forbidden!' #如果发现有输入< 阻挡，防止污染
	cursor.execute('USE app_whalechen') #使用数据库，名字是app_用户名
	cursor.execute('SELECT content, dt FROM dairy_db') #find out diary is misspelled, the unique tag 选择数据库中的表
	idtuple =cursor.fetchall() #获取所有符合选择条件信息
	idlist =list(idtuple) #获取的信息是tuple的格式，转换成为list
	the1print = time.strftime('%Y-%m-%d %H:%M:%S') #获取时间
	the2print = "欢迎！你输入了： " + diaryInput #获取输入内容
	the3print = idlist[len(idlist)-1][1].strftime('%Y-%m-%d %H:%M:%S') #获取最近一条信息的时间
	the4print = idlist[len(idlist)-1][0] #获取最近一条信息
	newid = len(idlist)+1 #获取最新id，之前id+1 
	#加入循环获得10条最近的信息
	list10 = []
	listInput10 =[]
	thelength = len(idlist)
	for i in range(10):
	    list10.append(time.strftime(idlist[thelength-1-i][1].strftime('%Y-%m-%d %H:%M:%S')))
	    listInput10.append(idlist[thelength-1-i][0])
	cursor.execute('INSERT INTO dairy_db (content,id,dt) VALUES("%s",%d,"%s")'%(diaryInput,newid,time.strftime('%Y-%m-%d %H:%M:%S')))
	db.commit() #提交数据给数据库
	db.close() #关闭数据库

	return template('write',diaryWritten1=the1print,diaryWritten2=the2print, diaryWritten3=the3print, diaryWritten4=the4print, diaryWritten =idlist, inputTime =list10,inputNotes =listInput10)

	# 来自小赖的方法
@app.get('/wechat')
def check_signature():
    token = "" #这里填你注册的token
    timestamp = request.GET.get('timestamp', None) 
    nonce = request.GET.get('nonce', None) 
    signature = request.GET.get('signature', None)  
    echostr = request.GET.get('echostr', None) 

    # 第1步：将token、timestamp、nonce三个参数进行字典序排序
    mylist = sorted([token, timestamp, nonce]) #将token, timestamp和nonce组成一个列表，然后进行排序

    # 第2步：将三个参数字符串拼接成一个字符串进行sha1加密
    mystr = "%s%s%s"%tuple(mylist) #将三个参数字符串拼接成一个字符串
    import hashlib
    mystr_encoded = hashlib.sha1(mystr).hexdigest() # 对拼接字符串进行sha1加密

    # 第3步：开发者获得加密后的字符串可与signature对比，标识该请求来源于微信
    if mystr_encoded == signature:
        return echostr
    else:
        return None	

@app.post('/wechat')
def get_data():
        import xml.etree.ElementTree as ET
	str_xml =request.body.read() #request获取post方法body中内容的方式
	xml = ET.fromstring(str_xml) #转变为可处理了xml
	content =xml.find("Content").text #提取Content的内容，返回为str
	msgType =xml.find("MsgType").text #同理
	fromUser =xml.find("FromUserName").text
	toUser=xml.find("ToUserName").text
	createtime = int(time.time())
	len_cotent =len(content)	
	
	db = MySQLdb.connect(host =sea.const.MYSQL_HOST, port =int(sae.const.MYSQL_PORT), user =sae.const.MYSQL_USER, passwd =sae.const.MYSQL_PASS, db=sae.const.MYSQL_DB)
        cursor =db.cursor()
        cursor.execute('USE app_whalechen')
	if msgType == "event":
	    mscontent =xml.find("Event").text  #希望能够在被关注的时候发送 欢迎信息，并记录下用户数据，失败
	    if mscontent =='subscribe':
	        #cursor.execute('INSERT INTO emotion_diary (fromUser, ct, flowStatement,content) VALUES("%s","%s",%d,"%s")'%(fromUser,time.strftime('%Y-%m-%d %H:%M:%S'), 5,"begin"))
		contentEcho = '''欢迎关注本微信，期待和你一起寻找最棒的你！心流状态初始值为5。'''
        else:
	    if len_cotent > 100:
	        contentEcho = "对不起，内容太多，消化不良，试试短一些的句子"  #防止过度输入
            else:
                if content[0] == 'w':
	            cursor.execute('SELECT content, dt FROM dairy_db') #这里是完全兼容简易日记
	            idtuple =cursor.fetchall()
	            idlist =list(idtuple)
		    the1print = time.strftime('%Y-%m-%d %H:%M:%S')
	            the2print = "欢迎！你输入了： " + content[1:]
	            the3print = idlist[len(idlist)-1][1].strftime('%Y-%m-%d %H:%M:%S')
	            the4print = idlist[len(idlist)-1][0]
		    newid = len(idlist)+1
		    contentEcho = (the1print +the2print +"  上一条信息为"+the3print+the4print) #回复一并将前一条记录的信息也给出
		    cursor.execute('INSERT INTO dairy_db (content,id,dt) VALUES("%s",%d,"%s")'%(content[1:].encode('utf-8'),newid,time.strftime('%Y-%m-%d %H:%M:%S')))
	        elif content[0] == 'h':
	            contentEcho ='''
			心流日记记录说明：心流状态采用主观评估，我们相信你的感觉。
			希望你当下评估你的心流状态，从0-9 给自己打个分数。
			按 x后直接加数字后直接加内容 来建立第一个心流档案。 
			在心流状态转变的时候，请再次评估，按 x后直接加数字后直接加内容 内容为你对情绪梗点说明。
			我们获得在数字之后的文字内容作为你个人对于心流状态的记录。
			如果希望查看你的心流日记内容，请按c
			'''
			
	        elif content[0]== 'x':
		    #cursor.execute('SELECT fromUser, ct, flowStatement, content FROM emotion_diary WHERE fromUser =%s'%(fromUser))  #WHERE 不能用
		    cursor.execute('SELECT fromUser, ct, flowStatement, content FROM emotion_diary')
		    idtuple =cursor.fetchall()
		    idlist =list(idtuple)
		    listlen =len(idlist)
		    #timegap 希望用来输入所用时间，待完善
		    i = listlen
		    time1 = '' #作为判断是第一次赋值的条件
		    while i > 0:
		        if idlist[i-1][0] == fromUser:
		            time1 =idlist[i-1][1].strftime('%Y-%m-%d %H:%M:%S')
			    flowState1 = idlist[i-1][2] # flowState is an int
		            break
			else:
		            i = i-1
		    time0 =time.strftime('%Y-%m-%d %H:%M:%S')
		    flowState0 = content[1]	
			
		    cursor.execute('INSERT INTO emotion_diary (fromUser, ct, flowStatement,content) VALUES("%s","%s",%d,"%s")'%(fromUser,time.strftime('%Y-%m-%d %H:%M:%S'), int(content[1]),content[2:].encode('utf-8')))
		    if time1 =='':
			contentEcho = ("真棒！恭喜你踏上记录心流日记的历程！你记录心流状态的时间是" +'%s'+"，你的心流状态是"+'%s'+"  你现在的感觉是："+"%s"+"，期待更棒的你！")%(time0,flowState0,content[2:])
		    else:
			contentEcho = ("你上一次记录心流状态的时间是" +'%s'+"，这段时间你的心流状态从"+"%d"+"转变到了"+'%s'+"\n"+"你现在的感觉是："+"%s")%(time1,flowState1,flowState0,content[2:]) 
			
		elif content[0] =='c':

		    cursor.execute('SELECT fromUser, ct, flowStatement, content FROM emotion_diary') #反馈信息，编得非常累赘
		    idtuple =cursor.fetchall()
		    idlist =list(idtuple)
		    listlen = len(idlist)
		    timelist =[]
	            flowlist =[]
		    contentlist =[]
		    i =listlen
		    while i > 0:
		        if idlist[i-1][0] == fromUser:
			    timelist.append(idlist[i-1][1].strftime('%Y-%m-%d %H:%M:%S'))
			    flowlist.append(idlist[i-1][2])
			    contentlist.append(idlist[i-1][3])
		            i = i-1
			    if len(timelist) >5:
			        break
			if timelist == []:
			    contentEcho =("请先开始记录心情日记喔！")
			else:
			    number = len(timelist)
			    contentEcho = "你之前的五条心流日记为 "
			    for j in range(number):
			        contentEcho +=("\n"+"%s"+" 心流值为"+ "%d"+" 梗点为"+"%s")%(timelist[j], flowlist[j],contentlist[j])
						
			
				
				
		
                else:
                    contentEcho = '''
			心流记录，请按 x后直接加数字后直接加内容 从0-9,一位 ；
			心流记录具体帮助 按h 获得具体指导和说明；
			如果希望查看你的心流日记内容，请按c
			吐槽日记，请按w后直接加输入内容；
			请输入少于50个的汉字。
			例子，w唱歌 表示吐槽 唱歌 
			x7听了轻音乐后心情舒畅 表示 记录心流值 为 7，
			此时听了轻音乐后心情舒畅。
			'''
	db.commit()
	db.close()
	return '''
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%s]]></Content>
</xml>
	'''%(fromUser, toUser, createtime, contentEcho)
	
		
debug(True)	
application =sae.create_wsgi_app(app)
