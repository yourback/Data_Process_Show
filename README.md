# Data_Process_Show
数据编程显示系统

V1.0

内容要求：
1、数据源有35个数据
2、执行的算是包括：加、减、乘、除、求导、积分。
3、可以进行条件运算。
4、可以通过绘图显示某个变量的具体数值。

分析：
一、数据解析：
	导入TXT文档后，将数据进行提取，获取数据行数，以及35个数据源，A0~A34。

二、数据处理：
	1、自主编程：
		（1）变量声明：将用到的数据进行声明，例如：A0，A2，A3，D，G
		（2）处理逻辑：循环数据行数，当前循环标记为 i

	2、程序识别：
		（1）变量声明部分：每一个变量都是长度为数据行数的的列表，其中A0~A34为数据源，其余的全0列表；
		（2）处理逻辑部分：直接使用exec（xxxxx）,并捕捉异常，出现异常给用户对应提示。
三、折线显示部分：
	所有声明的变量形成列表，供用户选择，用户在选择的时候，是可以设置变量名称的，选择后，可以直接生成折线图。


