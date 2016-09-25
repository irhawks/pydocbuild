# 说明文档

article:期刊与会议文章
calendar: 与时间有关的各种计划表、日历等
letter:信件格式，包括cover-letter，推荐信，个人陈述信等。也包括一些类似于信但是不像信的格式，比如公文。

从overleaf等来源当中克隆有关的幻灯片与演示的模板，以供参考使用。此外也复制了springer等论文的模板。主要保存latex格式。有时候也包括cv一类的东西。

资源：http://www.latextemplates.com/template/jacobs-landscape-poster

<http://www.thelinuxdaily.com/2008/10/latex-resume-examples/>上面有一个CV的模块与教程介绍。

<https://services.math.duke.edu/computing/tex/templates.html>是一个博士研究生所用的latex的模板。

<https://www.thebalance.com/recommendation-letter-template-2062919>上面介绍了英文的Reference Letter的写法。

<https://www.thebalance.com/how-to-request-a-transcript-for-a-job-application-2062973>介绍了Official Transcripts，也就是标准的成绩单。


<http://www.wikihow.com/Write-a-Letter-of-Recommendation>上面介绍了推荐信的各种写法。比如使用热情的术语。<http://www.theatlantic.com/education/archive/2014/02/the-art-of-the-college-recommendation-letter/284019/>还介绍了The Art of Recommendation Letter.



calendar目录--一天以内的时间[09-25-2016 10:51:39 CST]
----------------------------------------------------------------------

Part          Begin End   Meal             Greeting
------------- ----- ----- ---------------- ---------------------
morning/dawn   0:00  5:00                  
early morning  5:00  6:00                  Good morning
morning        6:00  9:00 breakfast        Good morning
mid-morning    9:00 11:59 elevenses/       Good morning
                          morning tea/
                          brunch
noon          12:00 12:00 -
afternoon     12:00 17:00 lunch/           Good afternoon
                          afternoon tea
evening       17:00 21:00 supper           Good evening
night         21:00 23:00 night-time snack Good evening
midnight      23:00  1:00 midnight snack   Good night

或者：

Part         Begin End   Meal             Greeting
-----------  ----- ----- ---------------- ---------------------
Early morning/
 wee hours    1:00  4:00                  Good morning
dawn          4:00  6:00                  Good morning
morning       6:00  9:00 breakfast        Good morning
Mid-morning   9:00 11:59 elevenses/
                         morning tea/
                         brunch           Good morning
noon         12:00 13:00 lunch            Good afternoon
afternoon    14:00 16:00 afternoon tea    Good afternoon
evening      16:00 21:00 tea/dinner       Good evening
night        21:00 23:59 supper           Good evening
mid-night    24:00  1:00                  Good evening

<http://stackoverflow.com/questions/217834/how-to-create-a-timeline-with-latex>上面有一篇介绍如何在LaTeX当中画时间线的说明。



模板改进说明[09-25-2016 17:39:24 CST]
----------------------------------------------------------------------

其实许多模板的设计并不合理。比如Roboto字体，经常是直接调用字体文件，这样的依赖关系使得模板非常缺乏共用性。我们还是必须得尽量让材料文件与模板文件脱离。不然的话，很容易使模板仅仅只能适用于某个文档。
