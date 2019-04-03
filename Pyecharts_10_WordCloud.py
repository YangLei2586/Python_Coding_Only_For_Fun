Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Part 10 Create WordCloud wity Pyecharts
>>> from pyecharts import WordCloud
>>> name=['Volvo Cars','Hofstra University','Yang Lei','Ryln Lei','BeiBei','Data Scince','Data Analyst','New York','Long Island','Sillicon Valley','American Dream','Thankful','Hard Working','Data Scientist','Polestar','Xc90','Garden City','Houston,Texas','Zarb','Business Analytics Master']
>>> value=[1112,4380,6181,4055,5668,2366,1866,1366,1166,966,456,323,10100,355,306,266,399,199,216,202]
>>> wordcould=WordCloud(width=1300,height=620)
>>> wordcloud=WordCloud(width=1300,height=620)
>>> wordcloud.add("",name,value,word_size_range=[20,100])
<pyecharts.charts.wordcloud.WordCloud object at 0x033F8F50>
>>> wordcloud.render()
>>> 
