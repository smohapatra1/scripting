from ipywidgets import interact, interactive,fixed
import ipywidgets as widgets

w = widgets.IntSlider()
from IPython.display import display
display(w)
w.close()
print(w.keys)
'''
def func(x):
    return (x)
interact(func,x=3);
'''