from flask import Flask
import pymysql

db = pymysql.connect("db", "root", "mypasswd", "flask")


app = Flask(__name__)


@app.route("/")
def hello():
    return """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
          <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
          </head>
          <div class="container-fluid">
            <h2>
              <a id="Its_a_Dockerized_Flask_ADVANCED_0"></a>It’s a Dockerized Flask 
              <code>[ADVANCED]</code>
            </h2>
            <a href="http://flask.pocoo.org/">
              <img src="/static/images/docker_flask.png" alt="Flask">
              </a>
              <p class="lead">
                <lead>It’s a Python3 
                  <strong>Flask</strong> app deployed via 
                  <strong>uWSGI</strong>, served by 
                  <strong>Nginx</strong> and...
                  <br> managed by 
                    <strong>supervisord</strong> all in an 
                    <strong>Alpine</strong> Docker alpine container
                  </p>
                </div>
"""

@app.route("/healthz")
def healthz():
    return "OK"

@app.route('/db')
def list_db():
   cursor = db.cursor()
   sql = "SELECT * FROM table"
   cursor.execute(sql)
   results = cursor.fetchall()
   return render_template('static/db.html', results=results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
