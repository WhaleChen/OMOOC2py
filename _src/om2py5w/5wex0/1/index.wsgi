
from bottle import Bottle, run,template,request,debug
import sae
#import bottle_mysql
#do not use bottle_mysql
import sae.const
import MySQLdb

app=Bottle()
# plugin =bottle_mysql.Plugin(dbuser='SAE_MYSQL_USER',dbpass='SAE_MYSQL_PASS',dbname='SAE_MYSQL_DB',dbhost='SAE_MYSQL_HOST_M', dbport='SAE_MYSQL_PORT')
# app.install(plugin)

@app.route('/')
def mainpage():
        # cursor.excute('USE app_whalechen')
        return template('write',diaryWritten='Hello')
@app.route('/write',method='POST')
def write():
        db = MySQLdb.connect(host ="w.rdc.sae.sina.com.cn", port =3307, user ="", passwd ="", db="app_whalechen") #should be your key
        cursor =db.cursor()
        diaryInput =request.forms.get('diaryInput')
	cursor.execute('USE app_whalechen')
	# contentlist =cursor.execute('SELECT content FROM dairy_db') wrong should use fetchall()
	cursor.execute('SELECT content, id FROM dairy_db') #find out diary is misspelled, the unique tag
	idlist =cursor.fetchall()
	newid = len(idlist)+1
	cursor.execute('INSERT INTO dairy_db (content,id) VALUES("%s",%d)'%(diaryInput,newid))
	db.commit()
	db.close()
	return template('write',diaryWritten=idlist)

debug(True)	
application =sae.create_wsgi_app(app)
