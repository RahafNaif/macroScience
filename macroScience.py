from flask import Flask, url_for
from views.home import home
from views.ccis import ccis
from views.science import science
from views.arc import arc
from views.ccisLevels import ccisLevels
from views.sc import sc

app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(ccis)
app.register_blueprint(science)
app.register_blueprint(arc)
app.register_blueprint(ccisLevels)
app.register_blueprint(sc)



if __name__ == "__main__":
    app.run(debug=True)
