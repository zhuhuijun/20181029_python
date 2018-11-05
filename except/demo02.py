#coding=utf-8

"""

进阶 异常处理


1.异常的几点注意
	一个try就有一个except

	1.1 不要没事就乱用异常
    慎用异常：1.找到python的内置异常
            2.理解python的内置异常分别对应什么情况
            3.阅读你的代码，找到你的代码里可能会抛出内置异常的地方
            4.仅对这几行代码做异常处理

	假设你无法知道你的代码会抛出什么异常，那么，你的异常处理便是无效的。	-》 准确了解你的代码情况。
	1.2 不要一个代码块，大try完事。
	1.3 好吧，想try all exception？sys.exc_info()
	1.4 logging如何使用呢


2.断言，一种开发期时检定代码的方式
	只断言绝对不能出现的错误 twisted


	先断言绝对不能发生的错误
	然后，再去处理错误 （异常）
3.代码友好，自动处理垃圾,with.


4.自己定义异常？继承exception类。

    import logging   
 
    logger = logging.getLogger()

    logfile = 'test.log'
    hdlr = logging.FileHandler('sendlog.txt')

    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    hdlr.setFormatter(formatter)

    logger.addHandler(hdlr)

    logger.setLevel(logging.NOTSET)



"""





import sys
import logging
logger = logging.getLogger()
logfile = 'test.log'
hdlr = logging.FileHandler(logfile)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.NOTSET)
try:
    a+b
except:
    exc = sys.exc_info()
    logging.debug(exc[1])
    print exc
