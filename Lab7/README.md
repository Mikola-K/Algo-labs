# Algo labs 7

## Task:
    Implement Knuth–Morris–Pratt Algorithm
## Complexity
- Space complexity: Θ(line_to_find_length + basic_line_length)

## Algorithm
The Knuth–Morris–Pratt string searching algorithm (or KMP algorithm) searches for occurrences of a "word" within a main "text string" by employing the observation that when a mismatch occurs, the word itself embodies sufficient information to determine where the next match could begin, thus bypassing re-examination of previously matched characters.

## How to run:
- cd into folder where you want to store this repository
- Clone this repository with command git clone https://github.com/Mikola-K/Algo-labs.git
- Choose branch lab5 with command git checkout lab7
- Go into folder with files with command cd Algo-labs/lab7
- run command python3 -m unittest test.py on Mac/Linux or py -m unittest test.py on Windows