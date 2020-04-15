from flask import Flask, make_response, render_template
import pandas as pd
app = Flask(__name__)

from views import * 
if __name__ == '__main__':
    app.run(debug=True)
    # ,host="10.0.1.53",port="5000"
