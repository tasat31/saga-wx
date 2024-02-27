#!/bin/bash

R --slave -e 'renv::init(force = TRUE)'
# R --slave -e 'renv::use_python('/usr/local/bin/python3')'
R --slave -e 'renv::restore()'
