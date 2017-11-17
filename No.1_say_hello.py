'''
在很多编程语言中，“Hello, World”程序都是你要学习编写的第一个程序，但是它没有涉及任何输入。
所以先来创建一个提示输入名字并打印包含该名字的问候信息的程序。

题1：问好
创建一个输入名字并打印包含该文字的问候信息的程序

示例输出：
What is your name? Brian
Hello, Brian, nice to meet you!

约束：
输入、字符串连接、输出，这几部分要分开

挑战：
1、不适用任何变量，编写一个新版本的程序
2、对不同的人显示不同的问候语。在完成第4章、第7章练习后，可以尝试此挑战。
'''

name = input("What is your name?")
print("Hello,",name+",","nice to meet you!")

#【问】如何在“name”和“nice to meet you!”之间添加一个逗号,且逗号紧挨着“name”？
#【答】直接在后面用“+”连接
