import flask
from app import app
from app import main


@app.route('/')
@app.route('/index')
def index():
    testout = main.main()
    curr_date = main.get_date()
    curr_time = main.get_time()
    return flask.render_template('index.html',
                           output=testout,
                           DATE = curr_date,
                           TIME = curr_time
                           )

@app.route('/webapi')
def webapi():
    dictout = main.getapi()
    curr_date = main.get_date()
    curr_time = main.get_time()
    sampledict = dictout[0]
    return flask.jsonify(*dictout)
