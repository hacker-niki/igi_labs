import os

from flask import Flask

import geometric_lib.circle

app = Flask(__name__)

radius = os.getenv('Radius')


@app.route('/')
def hello():
    html_string = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Python</title>
    </head>
    <body>
        <h1>Area of circle</h1>
        """
    if radius is not None:
        html_string += f"""
        <p>{radius} - <b>{geometric_lib.circle.area(float(radius))}</b></p>
        """
    else:
        html_string += f"""
                <p><b>Radius didn't set</b></p>
                """
    html_string += f"""
    </body>
    </html>
    """
    return html_string


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
