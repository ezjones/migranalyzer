#!/bin/sh
while true; do
    nohup python migranalyzer.py >> ez.out
    nohup python migranalyzer_Tim.py >> tim.out
done &
