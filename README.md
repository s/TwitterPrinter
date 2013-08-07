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
  
   <h3>Output: (Public data)</h3><br/>
    <code>assets</code>          : Contains css and font files.<br/>
    <code>templates</code>        : Contains original templates.<br/>
    <code>views</code>           : Contains generated views. Generated views will be in the folder for e.g <code>views/#TwitterPrinter</code><br/>

##Configuration (config.yaml)  
  	<code>consumerKey      </code>   : Instagram api consumer key.<br/>
	<code>consumerSecret    </code>  : Instagram api consumer secret.<br/>
	<code>accessToken        </code> : Instagram api access token.<br/>
	<code>accessTokenSecret  </code> : Instagram api access token secret.<br/>
  	<code>delayTime        </code>   : Delay time between each api request. Default: <code>30</code>(seconds)<br/>	
  	<code>pageTitle        </code>   : Page title of generated html file. Default: <code>InstagramPrinter</code><br/>
  	<code>searchHashtag    </code>   : Hashtag to search. Default:<code>TwitterPrinter</code><br/>	
  	<code>templateFileName </code>   : Name of template file. Default: <code>main.html</code><br/>


##View Template Tags:


<code>{$title}</code>                    : Page Title<br/>
<code>{$photoUrl}</code>                 : Url of photo<br/>
<code>{$photoWidth}</code>               : Width of photo<br/>
<code>{$photoHeight}</code>              : Height of photo<br/>
<code>{$postOwnerAvatar}</code>          : Avatar of post owner<br/>
<code>{$postOwnerUsername}</code>        : Screen username of post owner<br/>
<code>{$postOwnerName}</code>      		 : Name of post owner<br/>
<code>{$postDate}</code>                 : Create date of post<br/>
<code>{$photo} .. {/$photo}</code> 		 : Media block<br/>


##Screen Shots

![View Screen Shot](https://github.com/s/TwitterPrinter/blob/master/screenshots/twitter.png?raw=true)

##TO-DO
->Log files.