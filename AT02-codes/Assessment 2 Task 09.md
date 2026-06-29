# Assessment 2 Task 9

## Overview
This task evaluates the students ability to debug script. 

### Before Debugging

```bash

#!/usr/bin/env bash

# Ping hosts and print whether they are up or down
ping_hosts() {
    for host in "$@"; do
        if ping -c 1 -W 1 "$host" &>/dev/null; then
            echo "Connection to $host failed"
        else
            echo "Connection to $host successful"
        fi
    done
}

# If no hosts are passed to the script, print usage message and exit
if [ $# -eq 0 ]; then
    echo "Usage: $0 <host1> <host2> ..."
    exit 1
else
    ping_hosts "$@"
fi```


### After Debugging

``` bash
#!/usr/bin/env bash

# Ping hosts and print whether they are up or down
ping_hosts() {
    for host in "$@"; do
        if ping -c 1 -W 1 "$host" &>/dev/null; then
            #Changed failed to successful 
            echo "Connection to $host successful"
        else
            #Changed successful to failed
            echo "Connection to $host failed"
        fi
    done
}

# If no hosts are passed to the script, print usage message and exit
if [ $# -eq 0 ]; then
    echo "Usage: $0 <host1> <host2> ..."
    exit 1
else
    ping_hosts "$@"
fi
```
