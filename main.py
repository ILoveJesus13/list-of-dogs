"""
Module Docstring: main.py
======================

This is the main module of the read/write to file project.
"""

__author__="Beau Bramlett"
__version__="0.1"
__license__= "None"
__date__= "October 7, 2024"


def read_file(file_name) -> None:
    with open(file_name, "r")as f:
        for line in f:
            print(line, end+"")


def write_file(file_name) -> None:
    with open(file_name, "w")as f:
        f.write("Pit Bull")

def main():
   
   append_file("cats.txt", "siamese")

def append_file(file_name, data) -> None:

        with open(file_name, "a") as f:

            f.write(data)


        