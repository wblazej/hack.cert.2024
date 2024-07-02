# [re - CPU goes brrr](https://hack.cert.pl/challenge/brrr)

You need to decompile the given binary file e.g. using Ghidra. After that, you can recognize two highly unoptimized functions: the tribonacci sequence and the isPrime check. All you need to do is rewrite the decompiled code back to C++ (Python is too slow for this one) and replace the two mentioned functions with faster solutions.

Whole solution is in `sol.cpp`:
```bash
g++ -std=c++11 -o sol sol.cpp && ./sol 
```

### Flag
```
ecsc24{sl0w_4nd_5t3ady_w1ns_th3_r4ce}
```
