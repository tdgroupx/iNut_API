from flask import Flask, render_template, request
import requests

app = Flask(__name__)


def iNut_API(values):
    url = 'https://connect.mysmarthome.vn/api/1.0/request/Cff1m9axIaT59lvrQS13Ta7jsWk1/oJnpW9Op7/35c6eac4a73d83389756b215bd8a2683305225137149/req_device_sensor'
    headers = {
        'Content-Type': 'application/json'
    }
    json_data = requests.post(url, data=values, headers=headers).json()

    print(json_data)


@app.route('/', methods=['GET', 'POST'])
# Home
def index():
    if request.method == 'POST':
        if request.form.get("button1"):
            values = request.form.get("button1")
            iNut_API(values)
        elif request.form.get("button2"):
            values = request.form.get("button2")
            iNut_API(values)
        elif request.form.get("button3"):
            values = request.form.get("button3")
            iNut_API(values)
        elif request.form.get("button4"):
            values = request.form.get("button4")
            iNut_API(values)
        elif request.form.get("button5"):
            values = request.form.get("button5")
            iNut_API(values)
        elif request.form.get("button6"):
            values = request.form.get("button6")
            iNut_API(values)
        elif request.form.get("button7"):
            values = request.form.get("button7")
            iNut_API(values)
        elif request.form.get("button8"):
            values = request.form.get("button8")
            iNut_API(values)
        elif request.form.get("button9"):
            values = request.form.get("button9")
            iNut_API(values)
        elif request.form.get("button10"):
            values = request.form.get("button10")
            iNut_API(values)
        elif request.form.get("button11"):
            values = request.form.get("button11")
            iNut_API(values)
        elif request.form.get("button12"):
            values = request.form.get("button12")
            iNut_API(values)
        elif request.form.get("button13"):
            values = request.form.get("button13")
            iNut_API(values)
        elif request.form.get("button14"):
            values = request.form.get("button14")
            iNut_API(values)
        elif request.form.get("button15"):
            values = request.form.get("button15")
            iNut_API(values)
        elif request.form.get("button16"):
            values = request.form.get("button16")
            iNut_API(values)
        elif request.form.get("button17"):
            values = request.form.get("button17")
            iNut_API(values)
        elif request.form.get("button18"):
            values = request.form.get("button18")
            iNut_API(values)
        elif request.form.get("button19"):
            values = request.form.get("button19")
            iNut_API(values)
        elif request.form.get("button20"):
            values = request.form.get("button20")
            iNut_API(values)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
