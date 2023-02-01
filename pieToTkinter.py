import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = tk.Tk()
frameChartsLT = tk.Frame(root)
frameChartsLT.pack()

stockListExp = ['AMZN' , 'AAPL', 'JETS', 'CCL', 'NCLH']
stockSplitExp = [15,25,40,10,10]

fig = Figure() # create a figure object
ax = fig.add_subplot(111) # add an Axes to the figure

ax.pie(stockSplitExp, radius=1, labels=stockListExp,autopct='%0.2f%%', shadow=True,)

chart1 = FigureCanvasTkAgg(fig,frameChartsLT)
chart1.get_tk_widget().pack()

root.mainloop()