#!/usr/bin/env python3
"""
  Setup a basic Flask app
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=["GET"], strict_slashes=False)
def hello() -> str:
    """
      Printing out Hello World from the Html file
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
