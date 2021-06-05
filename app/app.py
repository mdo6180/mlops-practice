from flask import Flask
import matplotlib.pyplot as plt
import numpy as np


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!!!'


if __name__ == '__main__':

    mu = 0
    sigma = 0.1

    s = np.random.normal(mu, sigma, 1000)

    count, bins, ignored = plt.hist(s, 30, density=True)

    plt.plot(
        bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
        linewidth=2, color='r'
    )

    plt.savefig("./output/normal.png")

    app.run(host='0.0.0.0', port=8080)
