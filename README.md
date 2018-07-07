# Utils

## Install

From the root directory of this repo, run:

```
pip install -e lib
```

This will install the lib `utils`.

# Python Simple Progress Bar

A simple, easy-to-use progress bar for your time-consuming operations in Python.

## Usage

````
bar = ProgressBar(100)
bar.start()
for i in range(0, 100):
    time.sleep(1)
    bar.update(i)
````

Output:


````
Progress: [##############      ] 70%
````

## Documentation

### Basics

You set the end value and update it at each iteration with the new value. Note that it assumes values from 0 to `end_value-1`.

````
end_value = 42
bar = ProgressBar(end_value)
bar.start()
for i in range(0, end_value):
    # Do something cool but long
    bar.update(i)
````

### Options

#### Counts

You can display the current state of count if you want to see more than just the percentage by enabling `count`. **Default:** `False`.

````
bar = ProgressBar(74, count=True)
bar.start()
for i in range(0, 74):
    time.sleep(1)
    bar.update(i)
````

````
Progress (52/74): [##############      ] 70%
````

#### Info text

You can set the informative text before the bar by setting `text`. **Default:** `"Progress"`.

````
bar = ProgressBar(100, text="Iterations")
bar.start()
for i in range(0, 100):
    time.sleep(1)
    bar.update(i)
````

````
Iterations: [##############      ] 70%
````

#### Status text

You can set an informative text after the bar by passing `status_text` to `start()` and using `current_status()`.

````
bar = ProgressBar(100, text="Iterations")
bar.start(status_text="Initializing...")
time.sleep(2)
for i in range(0, 100):
    bar.current_status("Iteration %s" % i)
    time.sleep(1)
    bar.update(i)
````

````
Iterations: [##############      ] 70% Iteration 1
````

#### Bar length

You can set the length of the bar (hashes) by setting `bar_length`. **Default:** 20.

````
bar = ProgressBar(100, bar_length=10)
bar.start()
for i in range(0, 100):
    time.sleep(1)
    bar.update(i)
````
````
Progress: [#######   ] 70%
````

## Compatibility

Compatible with Python 2 and 3.
