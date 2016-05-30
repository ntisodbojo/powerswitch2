from flask import Flask, jsonify, make_response, render_template

import powerswitch

app = Flask(__name__)


@app.route('/api/v1/powerswitch')
@app.route('/api/v1/powerswitch/<device>')
@app.route('/api/v1/powerswitch/<device>/<int:set_status>')
def powerswitch_api(device=None,set_status=None):

    response=powerswitch.status(device,set_status)

    return make_response(jsonify(response))


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
