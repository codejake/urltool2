# urltool2

A small Python script that helps with repetitive cybersecurity work by parsing 
and decoding URL elements in useful ways. It contains no external dependencies 
and should run on any platform that supports Python 3, including macOS, Linux, 
Windows, and WSL.

I plan on adding more functionality to it during future lunches. See 
[TODO.md](TODO.md).

Feedback appreciated.

## Installation

1. Have a recent version of Python 3 installed on your system.

2. Download `urltool2.py` and run it.


## Usage

```bash
% ./urltool2.py
Enter a URL: https://url2.mailanyone.net/scanner?m=1s7vXH-087vxcm-3J&d=4%7Cmail%2F90%2F1719544200%2F1s7vXH-007xcm-3J%7Cin2c%7C57e55b682%7C17902772%7C12174482%7C6647356560D7825FF92FF08A4B666BA9C&o=%2Fphtm%3A%2Fatsmoc.rapbi&s=7yueudfref77wTq83xHw_rBolyj8

Proto: https
Netloc: url2.mailanyone.net
Path: /scanner
Params: 
Query: m=1s7vXH-087vxcm-3J&d=4%7Cmail%2F90%2F1719544200%2F1s7vXH-007xcm-3J%7Cin2c%7C57e55b682%7C17902772%7C12174482%7C6647356560D7825FF92FF08A4B666BA9C&o=%2Fphtm%3A%2Fatsmoc.rapbi&s=7yueudfref77wTq83xHw_rBolyj8
        Decoded query details:
                 m : 1s7vXH-087vxcm-3J
                 d : 4|mail/90/1719544200/1s7vXH-007xcm-3J|in2c|57e55b682|17902772|12174482|6647356560D7825FF92FF08A4B666BA9C
                 o : /phtm:/atsmoc.rapbi
                 s : 7yueudfref77wTq83xHw_rBolyj8
Fragment: 
Username: None
Password: None
Hostname: url2.mailanyone.net
Port: None

Defanged: hxxps://url2[.]mailanyone[.]net/scanner?m=1s7vXH-087vxcm-3J&d=4%7Cmail%2F90%2F1719544200%2F1s7vXH-007xcm-3J%7Cin2c%7C57e55b682%7C17902772%7C12174482%7C6647356560D7825FF92FF08A4B666BA9C&o=%2Fphtm%3A%2Fatsmoc.rapbi&s=7yueudfref77wTq83xHw_rBolyj8
```
