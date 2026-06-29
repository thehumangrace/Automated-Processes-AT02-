# Assessment 2 Task 8

## Overview
This task evaluates the students ability to debug script. 

### Before Debugging

```bash

#!/usr/bin/env bash

# This script reads a list of URLs from the command line, checks them for
# connectivity, and logs the results to a file.

log_file="connectivity.log"

# Check connectivity for a given URL
check_connectivity() {
    local url=$1
    if wget --spider --timeout=5 -q "$url"; then
        echo "$url: Accessible" >>"$log_file"
    else
        echo "$url: Inaccessible" >>"$log_file"
    fi
}

# If no URLs are passed to the script, print usage message and exit
if [ $# -lt 0 ]; then
    echo "Usage: $0 <url1> <url2> ..."
    exit 1
fi

# Otherwise, check connectivity for each URL passed to the script
for url in "$@"; do
    check_connectivity "$url"
done
```


### After Debugging

``` bash
#!/usr/bin/env bash

# This script reads a list of URLs from the command line, checks them for
# connectivity, and logs the results to a file.

log_file="connectivity.log"

# Check connectivity for a given URL
check_connectivity() {
    local url=$1
    if wget --spider --timeout=5 -q "$url"; then
        echo "$url: Accessible" >>"$log_file"
    else
        echo "$url: Inaccessible" >>"$log_file"
    fi
}

# If no URLs are passed to the script, print usage message and exit

#changed -lt to -eq
if [ $# -eq 0 ]; then
    echo "Usage: $0 <url1> <url2> ..."
    exit 1
fi

# Otherwise, check connectivity for each URL passed to the script
for url in "$@"; do
    check_connectivity "$url"
done
```
