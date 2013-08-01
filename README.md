TwitterPrinter
==============

A Python application that searchs and prints Twitter tweets with the given hashtag.

Application first connects to Twitter Api and fetchs matched tweet datas.<br/>

Then clones the template <code>main.html</code> and replaces tags with returning data from Api.

##Installation and Run

```
$ git clone git://github.com/s/TwitterPrinter.git ~/TwitterPrinter
$ cd ~/TwitterPrinter
$ python app.py
```

##Skeletal
  <h3>Classes: (Core python files)</h3><br/>
    <code>Api.py</code> : Handles Twitter Api connection and generates html files.<br/>
    <code>Printer.py</code> : Prints generated html files with connected printer.<br/>
  
   <h3>Output: (Public data)</h3><br/>
    <code>assets</code>          : Contains css and font files.<br/>
    <code>templates</code>        : Contains original templates.<br/>
    <code>views</code>           : Contains generated views. Generated views will be in the folder for e.g <code>views/#TwitterPrinter</code><br/>
