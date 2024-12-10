# This file must be used with "source bin/activate.csh" *from csh*.
# You cannot run it directly.
# Created by Davide Di Blasi <davidedb@gmail.com>.
# Ported to Python 3.3 venv by Andrew Svetlov <andrew.svetlov@gmail.com>

alias deactivate 'test $?_OLD_VIRTUAL_PATH != 0 && setenv PATH "$_OLD_VIRTUAL_PATH" && unset _OLD_VIRTUAL_PATH; rehash; test $?_OLD_VIRTUAL_PROMPT != 0 && set prompt="$_OLD_VIRTUAL_PROMPT" && unset _OLD_VIRTUAL_PROMPT; unsetenv VIRTUAL_ENV; unsetenv VIRTUAL_ENV_PROMPT; test "\!:*" != "nondestructive" && unalias deactivate'

# Unset irrelevant variables.
deactivate nondestructive

setenv VIRTUAL_ENV "/home/student/Desktop/dcbs/accessVirt"

set _OLD_VIRTUAL_PATH="$PATH"
setenv PATH "$VIRTUAL_ENV/bin:$PATH"


set _OLD_VIRTUAL_PROMPT="$prompt"

if (! "$?VIRTUAL_ENV_DISABLE_PROMPT") then
    set prompt = "(accessVirt) $prompt"
    setenv VIRTUAL_ENV_PROMPT "(accessVirt) "
endif

alias pydoc python -m pydoc

rehash

export AZURE_DB_NAME='development'
export AZURE_DB_HOST='c2084413.mysql.database.azure.com'
export AZURE_DB_PORT='3306'
export AZURE_DB_USER='c2084413'
export AZURE_DB_PASSWORD='your-password'
export AZURE_SA_NAME="dangobase2"
export AZURE_SA_KEY="z5fbEKbc3OAKjf1oBrDqEf0hsCEfWHMjBCCXwXkUmd/WK33Q+XRPzffCQ9+UQT9xwAsN/YvMEbfU+AStUIvjCA== " 

