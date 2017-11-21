### 题4 疯狂填词

疯狂填词是一个简单的游戏，我们创建一个空出一些单词的故事模板。你或另一个玩家提供一系列单词，将其放到故事中，得到一个通常或愚蠢或搞笑的故事

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

