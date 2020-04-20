import app
import json, plotly
from flask import render_template
from prep_script import return_figures

@app.route("/")
@app.route("/index")
def index():

    figures = return_figures()

    # plot ids for the html id tag in index.html
    ids = ["figure-{}".format(i) for i, _ in enumerate(figures)]

    # convert plotly figures to JSON for javascript in index.html
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("index.html",
                           ids=ids,
                           figuresJSON=figuresJSON)       