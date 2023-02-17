from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'containers-us-west-164.railway.app'
app.config['MYSQL_DATABASE_PORT'] = '6688'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'nLJcClD5TrTTz8JdH57p'
app.config['MYSQL_DATABASE_DB'] = 'railway'
#app.config['MYSQL_DATABASE_CHARSET'] = 'utf-8'

mysql.init_app(app)
