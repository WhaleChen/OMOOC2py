from bottle import Bottle, run
import sae
app=Bottle()
@app.route('/')
def mainpage():
        return template('write',diaryWritten='Hello')
apllication =sae.create_wsgi_app(app)