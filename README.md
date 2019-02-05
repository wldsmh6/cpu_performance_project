# cpu_performance_project
Implemented a Python client-server socket able to compare CPU performances of different computers. The client has to connect to the server in order to transmit its CPU performance and finally displays its ranking and result reference to the PCs or Servers registered in a MySQL database.

Implemented a Python client-server socket able to compare CPU
performances of different computers. The client has to connect to the server in order
to transmit its CPU performance and finally displays its ranking and result reference
to the PCs or Servers registered in a MySQL database.

First, the script identifies if it’s a server’s CPU or a PC’s CPU to compare
differently each category of CPUs.
In order to calculate the CPU performance, the client’s computer tests 20
benchmarks:
 Chaos: Create chaosgame-like fractals
 Delta Blue: Ported for the PyPy project
 Django Template: Build a 150x150-cell HTML table
 Float: Artificial, floating point-heavy benchmark originally used by Factor
 Go: Artificial intelligence playing the Go board game
 Hexiom: Solver of Hexiom board game (level 25 by default)
 Json Dumps: Benchmark dumps() functions of the json module
 Json Loads: Benchmark loads() function of the json module
 Mdp: Battle with damages and topological sorting of nodes in a graph
 Meteor Contest: Solver for Meteor Puzzle board.
 Nbody: N-body benchmark from the Computer Language Benchmarks Game
 Nqueens: Simple, brute-force N-Queens solver
 Pidigits: Calculating 2,000 digits of π. This benchmark stresses big integer
arithmetic
 Pyflate: Benchmark of a pure-Python bzip2 decompressor
 Raytace: Simple raytracer
 Regex DNA: regex DNA benchmark using “fasta” to generate the test case
 Richards: The classic Python Richards benchmark
 Scimark:
o Scimark_sor: Successive over-relaxation (SOR) benchmark
o Scimark_sparse_mat_mult: sparse matrix multiplication benchmark
o Scimark_monte_carlo: benchmark on the Monte Carlo algorithm to
compute the area of a disc
CPU Benchmarking
Page 4 of 7
o Scimark_lu: LU decomposition benchmark
o Scimark_fft: Fast Fourier transform (FFT) benchmark
 Spectral Norm: The Computer Language Benchmarks Game
 Sqlite Synth: Benchmark Python aggregate for SQLite
Their execution time is computed using python’s timeit( ) function and sent via
socket to the server.
After all the calculations in the server side the client will receive the CPU’s Final
Score and Ranking and will display it in the Graphical User Interface.

The Server receives all the execution times already obtained from the client
and send it to the database.
Via a Select query, the server selects all the execution times of a reference PC /
Server.
Then, it computes the SPEC Ratio for each Benchmark.
Then, it calculates the score which is the geometric mean of all the SPEC Ratios.
The final score is sent to the database and its ranking among other PCs already
stored in the database is calculated. The Final Score and the ranking are finally sent
to the client.

The database is divided in two parts Server and
PC and each part has 2 tables:
1. PC/ Server Execution Time (execTime): It stores the execution times of all the
benchmarks
2. PC/ Server: It stores the model of the CPU and the final scores.

How to use Code
Steps:
1. Import database.sql to MySQL
2. Open the command line on the Server folder
3. Write: “pip install –r requirements.txt”
4. Run Server.py
5. Open the command line on the Client folder
6. Write: “pip install –r requirements.txt”
7. Run Client.py
8. Press CPU Benchmarks then Start buttons
9. Wait until the Score and Rank appear
Database:
 Username: root
 Password: password

