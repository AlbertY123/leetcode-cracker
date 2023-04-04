I like data visualization that are both pretty and easy to understand. 

This package will include my favourite dataviz. 


## Installation

You can install this package by running

`pip install fav-plots`


## Development

Currently the package only has one simple function `add_one`, which can be called with code below

```
from fav_plots.utils import add_one
add_one(5) # this should return 6
```


## Unit test

* Create a virtual environment 
* Install unit requirements for local development and the project package in a developer mode:
    * `pip install -r unit-requirements.txt`
    * `pip install -e .`
* Run unit test
    * `pytest tests/unit --cov` 
