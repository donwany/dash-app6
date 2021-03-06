import plotly.offline as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np


def main():


	N = 100
	random_x = np.random.randn(N)
	random_y = np.random.randn(N)

	# Create a trace
	trace = go.Scatter(
    	x = random_x,
    	y = random_y,
    	mode = 'markers'
	)

	data = [trace]

	# Plot and embed in ipython notebook!
	py.plot(data, filename='basic-scatter.html')


if __name__ == '__main__':
	main()




