# Endid Python and Command-line client

Command-line utility and Python client for calling the [Endid Slack app](https://endid.app/) to announce that a task has ended!

Endid.app is a simpler more flexible webhook - an informal Slack integration for developers and data scientists.

Find yourself constantly checking terminals, notebooks, or web apps waiting to see if your dev tasks have finished?

Endid supplies a single token for any Slack channel. You can use Endid's simple API or command-line utility to let you know when any process has completed.

You can mute notifications temporarily right within Slack.

## Installation

To install both Python and Command-line clients:

```
pip install endid
```

Endid will install no other dependencies at all.

## Usage

Both clients store last-used tokens and messages on your system, so subsequently calling the bare-bones client with no token will still reach Slack.

Once Endid is installed in Slack, go to any channel (or message history with Endid app bot) and type `/endid`. You will receive a token such as 7c710a188f874520be1f7ab7815c6cd1 which you would use in the examples below.

### Command Line

Supply the token as an argument so a simple message ('Your task has ended!') appears in the Slack channel:

```
endid -t 7c710a188f874520be1f7ab7815c6cd1
```

Next time, just call endid to reuse the same token and Slack channel:

```
endid
```

Supply a custom message (to the saved channel/token):

```
endid -t 7c710a188f874520be1f7ab7815c6cd1 -m 'Here is a message'
```

For more command-line options run `endid -h`

### From Python code

From your Python code, for example in a Jupyter notebook:

```
import endid
endid.call(token='7c710a188f874520be1f7ab7815c6cd1')
```

To use the same token as last time (whether from Python or Command-line):

```
import endid
endid.call()
```

Extra arguments:

`message` - a custom message to display in the Slack channel.

`writeprefs` - whether to write token/message to the preferences file so they can become defaults next time (default=True)

`readprefs` - whether to read token/message from the preferences file (default=True)

`printoutput` - whether to print any success or error messages to the screen (default=False)

The call function returns an `OK` response from the API if everything goes to plan, and error messages if not.


### GitHub Actions

We have a ready-made [GitHub Action](https://github.com/marketplace/actions/endid-action) to easily send a Slack message via Endid.

The great thing is being able to mute notifications right from the Slack channel if they get a bit much, or 
to avoid disturbing colleagues while you develop your workflows.

## Installation Troubleshooting

The installation instructions assume you have [pip](https://pip.pypa.io/en/stable/installing/) on your system. This is usually the case for modern Windows and Mac.
If not, you can [install pip](https://pip.pypa.io/en/stable/installing/) first.

Alternatively, download [this file](https://raw.githubusercontent.com/endid-app/endid-python/main/endid/endid.py), rename it to `endid` and place it somewhere in your path. Make it executable too.

If you are using virtualenvs for Python development, `pip install endid` may attempt to install it inside your active virtualenv - which will work fine as long as the virtualenv is active. To install 'globally' `deactivate` the virtualenv first. If you then get a complaint that pip 'could not find an activated virtualenv', first set the 
environment variable PIP_REQUIRE_VIRTUALENV=false.

Please do not hesitate to raise a [GitHub Issue](https://github.com/endid-app/endid-python/issues) on this repo, or contact [support@endid.app](support@endid.app) to 
resolve installation or usage issues on your system.
