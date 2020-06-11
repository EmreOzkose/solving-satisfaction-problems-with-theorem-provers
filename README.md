# solving-satisfaction-problems-with-theorem-provers

3-sat an n-queens problems are solved with [Z3 theorem provider](https://github.com/Z3Prover/z3/wiki). [SMT-LIB2](http://smtlib.cs.uiowa.edu) files are given in this repository.

- 5 propositional formulas are given in CNF form in 3SAT_\<id=1..5\>.txt
- 5 ... are given in USAT_\<id=1..5\>-org.txt
- 5 ... are given in USAT_\<id=1..5\>-converted.txt
- 4 queens problem solution is given in  4-Queens.txt
- 8 queens problem solution is given in  8-Queens.txt
- A trick for finding all solutions in n-queens problem is given in N-Queens-all.txt

# Usage
### Build Z3
```
git clone https://github.com/Z3Prover/z3.git
cd z3
python scripts/mk_make.py
cd build
make
sudo make install
```

### Inference
example:
```
cd path/to/z3/build/
$ z3 -smt2 path/to/4-Queens.txt
```
