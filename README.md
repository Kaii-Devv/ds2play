● INSTALL MODULE
```
pip install ds2play==2.0
```


● USE MODULE
```
from ds2play import ds
sd = ds.ds()
result = sd.get("https://ds2play.com/e/ollbtbz0n0u7")
print(result.content()) # <Response [206]> #
print(result.url) # read url videos #
pd = ds.ds(proxy=True)
result2 = pd.get("https://ds2play.com/e/ollbtbz0n0u7")
print(result2.response) # <Response [206]> #
print(result2.content()) # error #
```

● EXC
```
<Response [206]>
https://no951gt.video-delivery.net/u5kj2fsxole3sdgge4dqcoi2iqbo7x47ekmhah66ejccqambe43ma442j7sq/3o9rdmipvq~ZQccwyvIYP?token=uhdhs9mq8u9e14qmt3xvg7fl&expiry=170461826899
<Response [206]>
Traceback (most recent call last):
  File "/data/data/com.termux/files/home/test.py", line 9, in <module>
    print(result2.content()) # error #
          ^^^^^^^^^^^^^^^^^
  File "/data/data/com.termux/files/usr/lib/python3.11/site-packages/ds2play/ds.py", line 39, in content
    if self.u_proxy:raise TypeError('[error] proxy True not suport .content()!! try .response')
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: [error] proxy True not suport .content()!! try .response
```
