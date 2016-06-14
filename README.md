# Exemplary Functions and Functional Examples

[![Build Status](https://travis-ci.org/jwg4/decorating_and_overruling.svg?branch=master)](https://travis-ci.org/jwg4/decorating_and_overruling)

This is a collection of examples and experiments about functions, decorators and related topics in Python.
The original motivation for this example code was a series of experiments done to try and find a way of calling code from an external library, changing exactly how it worked, but without modifying that external library directly.
This is explained in the file 50_motivation.md and the immediately following files give some examples of things that I tried.

The examples are presented as doctests in MarkDown files.
The Python code is given in a format similar to an interactive Python session, with some explanations in plain text in between.
Running doctest against all the MarkDown files in the repository should result in all tests passing.

Reading all the files from the start, in numerical order, takes you through the whole topic of functions, closures and decorators in Python from the very start to quite complex examples.
All you need as a prerequisite is some knowledge of Python syntax including how to call and define functions, or a willingness to pick it up as you go along.
