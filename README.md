# endid-python

Command-line utility and Python client for calling the Endid Slack app to announce that a task has endid!

## Installation

pip install endid

## Usage

### Command Line

```
endid -t 7c710a188f874520be1f7ab7815c6cd5
```

```
python3 endid.py -t 7c710a188f874520be1f7ab7815c6cd5
```

```
python2 endid.py -t 7c710a188f874520be1f7ab7815c6cd5 -m 'Here is a message'
```

```
python -m endid.cmd -t 7c710a188f874520be1f7ab7815c6cd5
```

### From Python code

```
import endid
endid.call(token='7c710a188f874520be1f7ab7815c6cd5')
```
