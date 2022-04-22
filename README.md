# PyShortener  
#### 将你的Python代码缩短至1行  
------------------------
__实例__:  
使用前:
```python
def func(something):
    print(something)


func("Hello world!")
```
    
使用后:
```python
exec("import base64\nb = b'ZGVmIGZ1bmMoc29tZXRoaW5nKToKICAgIHByaW50KHNvbWV0aGluZykKCgpmdW5jKCJIZWxsbyB3b3JsZCEiKQo='\nexec(base64.b64decode(b.decode('utf-8')).decode('utf-8'))")
```

