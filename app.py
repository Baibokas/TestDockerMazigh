from flask import Flask
from redis import Redis, RedisError
import os
import socket

print("Hello World")
# connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2,socket_timeout=2)
app = Flask(__name__)
print(socket.gethostname())
@app.route("/")
  
def hello():
    try:
        visites = redis.incr("compteur1")
        print("Hello worldV",visites)
    except RedisError:
        print("Hello worldEXCEPT")
        visites = "<i>Erreur de connection Reids, compteur descative </i>"

    html = "<h3> Bonjour {nom}! </h3>" \
           "<b> Hostname : </b> {hostname} <br/>" \
           "<b> visites:</b> {visites} <br/>" \
           "<p> Abonne toi! </p>"
    return html.format(nom=os.getenv("NOM", "youtube2"),hostname=socket.gethostname(), visites=visites)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)