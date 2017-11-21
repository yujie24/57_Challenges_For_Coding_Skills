# 挑战编程技能：57道程序员功力测试题

**Exercises for Programmers by Brian P.Hogan**

<div align=center>
  <img src="https://github.com/yujie24/ChallengeForProgramming57/blob/master/Exercises%20for%20Programmers.jpg" width=40% height=40% alt="Figure 1.English Cover"/>
  <img src="https://github.com/yujie24/57_Challenges_For_Coding_Skills/blob/master/%E6%8C%91%E6%88%98%E7%BC%96%E7%A8%8B%E6%8A%80%E8%83%BD-57%E9%81%93%E7%A8%8B%E5%BA%8F%E5%91%98%E5%8A%9F%E5%8A%9B%E6%B5%8B%E8%AF%95%E9%A2%98.jpg?raw=true" width=41.5% height=41.5% alt="Figure 2.中文封面"/>
</div>

> When you write software, you need to be at the top of your game. Great programmers practice to keep their skills sharp. Get sharp and stay sharp with more than fifty practice exercises rooted in real-world scenarios. If you’re a new programmer, these challenges will help you learn what you need to break into the field, and if you’re a seasoned pro, you can use these exercises to learn that hot new language for your next gig.


**这是一本通用于提高所有语言、所有程序员的编程技能的书，一共列举了九个章节共57个问题。对于提高编程能力，训练编程思维来说，我认为确实很有用处。**

**说明：书中并没有教读者具体的代码，也没有指定具体某一种编程语言，而是教会大家编程的思维与能力。所以不论是C还是java，或者是我所用的python，都阔以使用。欢迎补充！**


# 目录

|章   节|问   题|
|------|-------|
|第一章 将问题转变成代码|理解问题|
||发现输入、处理和输出|
||用测试驱动设计|
||用伪代码编写算法|
||挑战|
||前进|
|第二章 输入、处理和输出|题1 问好|
||题2 计算字符数|
||题3 打印引语|
||题4 疯狂填词|
||题5 简单的数学处理|
||题6 计算退休时间|
|第三章 计 算|题7 矩形房间的面积|
||题8 比萨聚会|
||题9 涂料计算程序|
||题10 自助结账|
||题11 货币兑换|
||题12 计算单利|
||题13 确定复利|
|第四章 做出决策|题14 税额计算程序|
||题15 密码验证|
||题16 法定驾驶年龄|
||题17 计算血液中的酒精含量|
||题18 温度转换程序|
||题19 计算身高体重指数|
||题20 多州税收计算程序|
||题21 从数字到名字|
||题22 比较数字|
||题23 定位汽车问题|
|第五章 函 数|题24 字母易位词检查程序|
||题25 检查密码强度|
||题26 计算还清信用卡欠款所需的时间|
||题27 验证输入|
|第六章 重 复|题28 数字相加|
||题29 处理错误的输入|
||题30 乘法表|
||题31 卡蒙内心律|
||题32 猜数字游戏|
|第七章 数据结构|题33 神器8号球|
||题34 从员工列表中删除元素|
||题35 选择优胜者|
||题36 计算统计信息|
||题37 密码生成器|
||题38 过滤值|
||题39 排序记录|
||题40 过滤记录|
|第八章 使用文件|题41 姓名排序程序|
||题42 解析数据文件|
||题43 网站生成器|
||题44 产品搜索|
||题45 单词查找|
||题46 词频统计|
|第九章 使用外部服务|题47 谁在太空中？|
||题48 抓取天气|
||题49 Flickr照片搜索|
||题50 电影推荐|
||题51 向Flickr提交笔记|
||题52 创建自己的时间服务|
|第十章 完整的程序|题53 待完成事项清单|
||题54 短网址服务|
||题55 文本分享|
||题56 记录财产|
||题57 多选琐事问答应用|
|最后 下一步干什么|练习+思考+解决+分享|

# 第一章   将问题转变成代码

### 理解问题

### 发现输入、处理和输出

### 用测试驱动设计

### 用伪代码编写算法

### 挑战

### 前进

重点：玩得开心、享受学习！

# 第二章   输入、处理和输出

### 题1 问好

创建一个提示输入名字并打印包含该名字的问候信息的程序。

示例输出：

> What is your name? Brian

> Hello, Brian, nice to meet you!

约束：

- 输入、字符串连接、输出，这几部分要分开。

代码：

```python

name = input("What is your name?")

print("Hello,",name+",","nice to meet you!")

```

挑战：

- 不使用任何变量，编写一个新版本的程序。

- 编写一个新版本，对不同的人显示不同的问候语。在完成第4章和第7章的练习后，这是个值得一试的不错的挑战。

### 题2 计算字符数

创建一个程序，提示用户输入字符串，然后输出这个字符串，以及其中包含的字符数。

示例输出：

> What is the input string? Homer

> Homer has 5 characters.

代码Python：

```python

str = input("What is the input string?")
print(str,"has", len(str),"characters.")

```

约束：

- 确保输出中包含原始的字符串。

- 使用一个输出语句来构造输出。

- 使用所用编程语言中的一个内置函数来确定字符串的长度。

挑战：

- 如果用户什么都没输入，提示用户输入内容。

- 使用图形用户界面实现该程序，在每次键盘按下时，更新字符计数信息。如果所用语言没有特别友好的GUI库，尝试使用HTML和JavaScript来做这个练习。

### 题3 打印引语

创建一个程序，提示用户输入一条引语及其作者。按照示例输出那样显示引语和作者。

示例输出：

>What is the quote? These aren't the droids you're looking for.

>Who said it? Obi-Wan Kenobi

>Obi-Wan Kenobi says, "These aren't the droids you're looking for."

约束：

- 使用一条输出语句来生成该输出，使用适当的字符串转义技术来处理引语。

- 如果所用编程语言支持字符串插入或替换，在这个练习中不要使用。要使用字符串连接。

代码Python:

```python

quote = input("What is the quote?")
people = input("Who said it?")
print(people,"says,","\""+quote+"\"")

```

挑战：

- 在第7章中，你将练习使用数据的列表。修改这个程序，不再提示用户输入引语，而是自己创建一个保存引语及其作者的结构，然后使用例子中的格式显示所有的引语。由映射（map）组成的数组会是个不错的选择。

### 题4 疯狂填词

创建一个简单的疯狂填词程序，提示用户输入一个名词、一个动词、一个形容词和一个副词，然后将这些词插入到所创建的故事中。

示例输出：

> Enter a noun: dog

> Enter a verb: walk

> Enter an adjective: blue

> Enter an adverb: quickly

> Do you walk your blue dog quickly? That's hilarious!

约束：

- 在程序中使用一条输出语句。

- 如果所用语言支持字符串插入或替换，则使用它来构造输出。

代码Python：

```python
noun = input('Enter a noun:')
verb = input('Enter a verb:')
adj  = input('Enter a adjective:')
adv  = input('Enter a adverb:')
print('Do you',verb,'your',adj,noun,adv+'?','That\'s hilarious!')
```

挑战：

- 向程序中添加更多输入，扩展故事。

- 实现一个带有分支发展的故事，可以根据问题的答案来确定如何构造故事。在第4章的问题中，你将进一步探索这个概念。

### 题5 简单的数学处理

你将经常编写处理数值的程序。取决于所使用的编程语言，有时必须将获取的输入转换成数值数据类型。

编写一个程序，提示用户输入两个数。打印这两个数的和、差、积及商，如示例输出所示。

示例输出：

> What is the first number? 10

> What is the second number? 5

> 10 + 5 = 15
> 10 - 5 = 5
> 10 * 5 = 50
> 10 / 5 = 2

约束：

- 用户输入的值将会是字符串。确保在做数学运算之前将其转换成数值。

- 将输入和输出与数值转换及其他处理分开。

- 生成一条在适当的位置包含换行的输出语句。

代码Python：

```python
a = int(input('What is the first number?'))
b = int(input('What is the second number?'))
print(a,'+',b,'=',a+b)
print(a,'+',b,'=',a-b)
print(a,'*',b,'=',a*b)
print(a,'/',b,'=',a/b)
print(a,'/',b,'=',int(a/b)) #将最后结果显示为整数，而非浮点数
```

挑战：

- 修订这个程序，确保输入以数值形式提供。如否，不允许用户继续。

- 不允许用户输入负数。

- 将程序分解成处理计算的函数。你将在第5章中探索函数。

- 将该程序实现为图形用户界面程序，当任何值发生变化时，自动更新相关的值。

### 题6 计算退休时间

你的计算机知道今年的年份，这意味着可以将该信息加到你的程序中。你只需要知道所用编程语言如何提供该信息。

创建一个程序，确定用户还有多少年退休，并计算退休年份。它应该提示用户输入当前年龄，以及想要退休的年龄，最终按如下例子这样显示输出。

示例输出：

> What is your current age? 25

> At what age would you like to retire? 65

> You have 40 years left until you can retire.

> It's 2015, so you can retire in 2055.

约束：

- 再次强调，在做任何数学运算之前，务必将输入转换成数值数据。

- 不要将当前的年份硬编码到程序中。通过所用编程语言从系统时间中获取。

代码Python：

```python

```

挑战：

- 处理程序返回负数的情况，提示用户已经可以退休了。

### 本章回顾

重点：保持输入、处理和输出分开。

当程序很简单时，在输出语句中做点数学运算或字符串连接，可能很有诱惑力，但随着程序愈加复杂，会发现需要将其分解为可以复用的组件。你会为一开始的这种训练感到开心的。

下一章是更严肃的数学问题。

# 第三章   计算

本章开始研究复杂点的运算。数值转换公式，以及一些金融相关的程序。

运算优先级：括号>幂>乘>除>加>减

浮点数的精度问题在很多语言中都存在。常用的一种方案是用整数表示钱。如1.25元换成125分。

### 题7 矩形房间的面积

如果你在一个全球化的环境中工作，则必须同时提供公制和英制单位的信息，而且需要知道何时进行转换，以保证结果最为精确。

编写一个计算房间面积的程序。提示用户输入以英尺为单位的房间的长和宽。然后显示以平方英尺和平方米为单位的面积。

示例输出：

> What is the length of the room in feet? 15

> What is the width of the room in feet? 20

> You entered dimensions of 15 feet by 20 feet.

> The area is

> 300 square feet

> 27.871 square meters

转换公式为：

m^2 = f^2 * 0.0920304

约束：

- 让计算与输出分离。

- 使用一个常量来保存转换因子。

代码Python：

```python

```

挑战：

- 修改程序，确保输入的是数值。如果不是，不允许继续。

- 开发一个新版本，支持用户选择输入的单位是英尺还是米。

- 以GUI方式实现该程序，当任何一个值有修改时，自动更新结果。

### 题8 比萨聚会

除法并不总是精确，有时候需要写程序来处理余数，而不是用小数。

编写一个平均分配比萨的程序。提示用户输入就餐人数、比萨数，以及每个比萨分几块。确保平均分配。显示每个人能得到几块。如果有剩余，显示剩下几块。

示例输出：

> How many people? 8

> How many pizzas do you have? 2

> 8 people with 2 pizzas

> Each person gets 2 pieces of pizza.

> There are 0 leftover pieces.

约束：

- （无）

代码Python：

```python

```

挑战：

- 修改程序，确保输入的是数值。如果不是，不允许继续。

- 修改输出，使其可以正确处理复数，比如：

> Each person gets 2 pieces of pizza.

或

> Each person gets 1 piece of pizza.

对于剩下的块数，也这样处理。

- 开发一个该程序的变种，提示用户输入就餐人数和每个人想要的比萨块数，计算需要购买多少个比萨。

### 题9 涂料计算程序

### 题10 自助结账

### 题11 货币兑换

### 题12 计算单利

### 题13 确定复利

# 第四章   做出决策

### 题14 税额计算程序

### 题15 密码验证

### 题16 法定驾驶年龄

### 题17 计算血液中的酒精含量

### 题18 温度转换程序

### 题19 计算身高体重指数

### 题20 多州税收计算程序

### 题21 从数字到名字

### 题22 比较数字

### 题23 定位汽车问题

# 第五章 函 数

### 题24 字母易位词检查程序

### 题25 检查密码强度

### 题26 计算还清信用卡欠款所需的时间

### 题27 验证输入

# 第六章 重 复

### 题28 数字相加|

### 题29 处理错误的输入

### 题30 乘法表

### 题31 卡蒙内心律

### 题32 猜数字游戏

# 第七章 数据结构

### 题33 神器8号球

### 题34 从员工列表中删除元素

### 题35 选择优胜者

### 题36 计算统计信息

### 题37 密码生成器

### 题38 过滤值

### 题39 排序记录

### 题40 过滤记录

# 第八章 使用文件

### 题41 姓名排序程序

### 题42 解析数据文件

### 题43 网站生成器

### 题44 产品搜索

### 题45 单词查找

### 题46 词频统计

# 第九章 使用外部服务

### 题47 谁在太空中？

### 题48 抓取天气

### 题49 Flickr照片搜索

### 题50 电影推荐

### 题51 向Flickr提交笔记

### 题52 创建自己的时间服务

# 第十章 完整的程序

### 题53 待完成事项清单

### 题54 短网址服务

### 题55 文本分享

### 题56 记录财产

### 题57 多选琐事问答应用

# 最后 下一步干什么

### 练习+思考+解决+分享