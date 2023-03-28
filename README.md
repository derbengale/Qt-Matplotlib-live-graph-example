# Minimal Example how to Embed a Live MPL Graph in a QT-Application

This example shows how to embed interactive Graphs in a QT Application created with UI Designer.

## How to create a GUI

To create a GUI Design
```bash
pyside6-designer
```
To create the .py File that needs to be embedded
```bash
pyside6-uic design.ui -o designfile.py
```

## Why this Repo has been created
A lot of the examples on the Internet show how to embed a graph in QT but most of them did not show how to embed it in such a way that it can be updated. 

The examples I could find often used a clear() statement and plot the whole graph afterwards again. This lead to growing objects in the RAM since someobject I couldn't find grew continuously.

This example shows how I solved this problem. I updated mplwidget.py and replaced the axis.clear() statements by set_data and set_xlim set_ylim and canvas.draw() like it is done in the official MPL example. 

That example did not use the mplwidget.py file I previously took from an example in the internet and was not easily embeddable with UI Designer so this fixes that.