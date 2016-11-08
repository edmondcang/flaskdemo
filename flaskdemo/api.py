from flaskdemo import app
from datetime import datetime

@app.route('/api/srvtime')
def srvtime():
    d = datetime.now()
    return 'The time of the server is now %s' % d.strftime('%H:%M:%S')
