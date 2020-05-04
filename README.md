# ProxyList
This python code checks the latest proxy list from 'https://www.free-proxy-list.net/' with 'https://baidu.com/'.

All possible proxies are saved to `./hosts.txt`.

All working proxies are saved to `./working.txt`.

Note: `working.txt` is saved using `pickle.dump()`, so that it could be retrieved by other programs using `pickle.load()`.

```python
with open('working.txt', 'rb') as filehandle:
    working = pickle.load(filehandle)
proxy = random.choice(working)
```

