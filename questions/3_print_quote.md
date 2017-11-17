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

