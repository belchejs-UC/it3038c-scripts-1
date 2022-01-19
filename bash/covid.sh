#!/bin/bash


#This is script to pull covid data

POSITIVE=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].positive')
NEGATIVE=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].negative')
TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive covid cases, there were $NEGATIVE negative cases"
