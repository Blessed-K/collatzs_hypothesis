This is a code that helps solve the collats hypothesis for idividual values. It follows the rules below giving the number of steps and individual/intermediate values that came up before the final answer was achieved. The hypothesis states that when the rules are followed any number that meets the requirements will eventually evaluate to 1.
The rules are:
take any non-negative and non-zero integer number and name it c0;
if it's even, evaluate a new c0 as c0 ÷ 2;
otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
if c0 ≠ 1, go back to point 2.
