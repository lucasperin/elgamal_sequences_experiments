# elgamal_sequences_experiments

---

## Requirements
* numpy
* matplotlib
* tqdm

## Experiments

### Primes
* Lists primes starting at 1100000 where 'v divides p-1' for v in (2, ,3 , 4, 5, 6 ... )
* Passing 'use_v_is_g' as 'True' will force to list only primes where v is also a generator of the group of order p.
* Remark that v is never a generator when v in (4, 5, 8)

### Runs
* Generates csv files with run count of ElGamal Sequences
* Uses prime numbers from `primes` experiment
* For `normal` prime list, counts runs for Theorem 9 and Theorem 10
* For `v_is_g` prime list, counts runs for Theorem 9

The main difference is that generators for Theorem 10 are coprime to v.

### Tuples
* Generates csv files with tuple count of ElGamal Sequences

## Histograms

## Runs
* Generates a histogram of the `difference` of the upper/lower 
  bounds against the actual run count
    
* Generates a ratio plot of the number of runs of length t+1 divided 
  by the number of runs of length t (includes normalized plot, with 
  ratio multiplied by v). This plot shows Golomb's run length postulate
  for ElGamal Sequences (for normalized, we expect values to be distributed
  around 1).

## Tuples
* Generates a histogram of the `difference` of the upper/lower 
  bounds against the actual tuple count
* Generates an accuracy plot. Namely, the percentage of hits (when 
  difference is 0), for tuples of length t.
  
### Plots


### Report
* Automatically generate tex file that can be compiled into PDF with all 
  plots, for easier display of the experimentation.
