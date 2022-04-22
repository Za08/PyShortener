# PyShortener  
#### 1. 使用shortener.py将你的Python代码缩短至1行  
------------------------
__示例__:  
> 使用前:
```python
def func(something):
    print(something)


func("Hello world!")
```
    
> 使用后:
```python
exec("import base64\nb = b'ZGVmIGZ1bmMoc29tZXRoaW5nKToKICAgIHByaW50KHNvbWV0aGluZykKCgpmdW5jKCJIZWxsbyB3b3JsZCEiKQo='\nexec(base64.b64decode(b.decode('utf-8')).decode('utf-8'))")
```  
<br />
<br />

#### 2. 使用lengthener.py将使用shortener.py缩短的代码还原
------------------------
__示例__:  
> 使用前:
```python
exec("import base64\nb = b'ZGVmIGZ1bmMoc29tZXRoaW5nKToKICAgIHByaW50KHNvbWV0aGluZykKCgpmdW5jKCJIZWxsbyB3b3JsZCEiKQo='\nexec(base64.b64decode(b.decode('utf-8')).decode('utf-8'))")
```  
    
> 使用后:
```python
def func(something):
    print(something)


func("Hello world!")
```

<kbd>最后：这是写着玩的，不要用在你的项目中!</kbd>
