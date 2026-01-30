# Mommy+
Lovense and Pishock integration with [mommy](https://github.com/fwdekker/mommy).

## Requirements
Requires https://github.com/fwdekker/mommy to be installed. See that project for specifics.

Requires python3 to be installed. See https://www.python.org/.

Requires bash.

## Installing
Set `mommy-plus.py`, `encourage-plus.sh`, and `encourage.sh` to executable (chmod +x FILE).

Place all \*.py and \*.sh files in your PATH.

## Setup

### Mommy
The encourage scripts allow for mommy config swapping. To set this up, create a `~/.config/mommy/` directory. This will include \*.config.sh files, along with the active `config.sh` file. See the mommy project for how a configuration file is done.

### Lovense
Using the lovense remote app, connect your toy and set the app to use gamemode. Edit the `love.py` script to include the IP for your gamemode server in the "ip" variable. Optionally set the "ssl" variable to true if you wish to use ssl instead of http.

### Pishock
Connect haptic modules to the controller hub. Follow the normal pairing instructions here.

Follow the instructions at https://pishock.com and https://apidocs.pishock.com to get an API key. Using the values as described in the API docs, set the following environment variables:
- SECRET_PISHOCK_USERNAME
- SECRET_PISHOCK_API_KEY
- SECRET_PISHOCK_SHARE_CODE
- SECRET_PISHOCK_NAME

### Mommy+
Editing the file `mommy-plus.py` allows you to change the punishment or rewards. Editing the "reward()" and "punish()" functions can tweak the vibrate/shock duration and power.

# Usage
```$ mommy-plus.py COMMAND```  
```$ mommy-plus.py -s EXIT-CODE```  
The `mommy-plus.py` script takes a command and either shocks or vibrates depending on the return value of the command. It then passes the return value to mommy to encourage or compliment. If the `-s` flag is used, the command line arguments will be interpretered as an exit code and not a command.

```$ encourage-plus.py LEVEL [CONF]```  
The encourage scripts configure the level of mommy(+) involvement. The following levels are available:
- 0     mommy(+) isn't enabled
- 1     mommy(+) is enabled on only specific commands; edit script to edit the commands included
- 2     mommy(+) only has encouragement enabled
- 3     mommy(+) enabled on all commands

The optional conf argument specifies which file ~/.config/mommy/CONF.config.sh should be set to the current mommy config.  
`encourage.py` only uses mommy, while `encourage-plus.py` uses `mommy-plus.py`.  

