#! /bin/bash

rm -f PES* *log *out *err *pdb *c

if [ "$1" = "s" ];
then
    rm -f structures/*
fi

