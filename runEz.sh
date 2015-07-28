#!/bin/bash
while true; do
    nohup python migranalyzer.py &> ez.out
done &
