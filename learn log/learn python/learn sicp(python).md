  # *我接触的第一个编程语言————python*
  python是一种面向对象的语言，在python之中一切都可以被视作对象，当我在操作对象时，实则也是对象在调用自己的方法或者调用自己的属性，这在学习完*类*以后尤其明显。

  - 类型
   - 方法
     * 函数
   - 数值

-最底层：values 和 exprssions，他们组建起了python中的复杂语句

  - 首先，是缩进，代码块的表示有很多种方法，而缩进则是python所选择的方法，这种方法很方便（如果不需要缩进太多次的话）一个TAB或者四个空格。

  - 其次，python中的运算符
  
    - \+ \- * / %（取余数） //（取整数）**（指数) 这些用于数学运算

  - 简单数据类型

    - string(字符串 通常有''或"") inter(整数) float(浮点数) list(列表) dictionary(字典) tuple(元组)

     - "hello world!"       ；   114514   ；    3.14159  ；    [2,3,3]  ；  {"key":"name"} ； (1,2,3)

      -- 字符串也可以进行对列表的操作，例如遍历，每一个字符都有索引，索引顺序与列表和元组都相同由0开始一直到最后一个。不同的是元组中的元素不可更改。字典{key:name}以key作为索引，而name则是索引值（value）
    - bool值
     - 布尔值（bool）在python中是 True 与 False,但又不仅仅是True与False。在python中False, None, 0, 0.0, 0j, '', (), [], {}, set(), range(0)都被视为False,而除此之外的则被视为True。这将在后续语法发挥作用。
      -
 - 简单语法
  - if判断语句
  - ```python
    if <expression1>:
        <expression2>
    #如果expression1的值是True,那么解释器会运行下面的语句，如果是False，就不会运行任何东西。
    #但是
    if <expression1>:
      <expression2>
    elif <exprssion3>:
      <expression4>
    else:
      <expression5>
    #（下面用数字指代表达式）如果（1）是对的，则运行（2），否则就会检查（3），如果（3）是对的，就会运行（4），否则如果if与elif都检查完毕，都是False,则运行else后面的语句，这里是（5）。
    ```
  - while循环
  - for遍历
    

  ## 类
  ```python
      class <name>(parent class):
            class attribute1 = ""
            class attrubute2 = ""
            ...
            def __init__(self,a,b)：
                self.<instance attribute> = a
                ...
```
- 类，即类型。
  - 当创建一个*类*时，即是创建了一个*类型*，这个类型之下可以有多个实例，他们隶属于该类型，实例相当于类型之下的个体，而类型是实例的抽象。
  - 但类型之下，实例之上还存在子类，子类相当于类型的特殊。

好比有理数类型，有理数类型之下有浮点数与整数浮点数与整数就是有理数的子类，而1.1与1则是浮点数与整数的实例。

如果说类是一个集合，那么子类便是他的子集（也可能只继承了一部分），而实例则是集合中的元素。


 
                
  

