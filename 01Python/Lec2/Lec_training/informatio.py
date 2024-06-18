import platform
import os
import importlib
import requests
print(platform.system())
print(platform.release())
print(platform.version())
print(platform.machine())
print(platform.processor())
print(platform.architecture())
print(platform.node())
print("*************************************************")
print(os.getcwd())
print(os.listdir())
print("*************************************************")
print(importlib.import_module("os"))
print(importlib.import_module("platform"))
print(importlib.import_module("requests"))



