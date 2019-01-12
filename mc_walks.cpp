#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <string>

#include "mpi.h"

using namespace std;

double frand(double a, double b)
{
    return a+(b-a)*(rand()/double(RAND_MAX));
}

int do_walk(int a, int b, int x, double p, double& t)
{
    int step = 0;
    while( x>a && x<b )
    {
        if( frand(0,1)<p )
            x += 1;
        else
            x -= 1;
        t += 1.0;
        step += 1;
    }
    return x;
}

void run_mc(int a, int b, int x, double p, int N, int proc_amount = 1, int proc_rank = 0) {
    // srand(time(0));
    double t = 0.0;
    double w = 0.0;

    int overhead = N % proc_amount;
    int block_size = N / proc_amount;
    if (proc_rank < overhead)
        block_size++;
    int start = block_size * proc_rank;
    if (proc_rank >= overhead)
        start += overhead;
    for (int i = start; i < start + block_size; i++) {
        int out = do_walk(a, b, x, p, t);
        if (out == b)
            w += 1;
    }

    double t_common, w_common;
    MPI_Reduce(&t, &t_common, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);
    MPI_Reduce(&w, &w_common, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    if (!proc_rank) {
        ofstream f("output_" + to_string((long long)(N)) + '_' + to_string((long long)(proc_amount)) + ".txt");
        f << w_common / N << " " << t_common / N << endl;
        f.close();
    }
}

int main(int argc, char** argv)
{
    MPI_Init(&argc, &argv);
    int proc_amount, proc_rank;
    MPI_Comm_size(MPI_COMM_WORLD, &proc_amount);
    MPI_Comm_rank(MPI_COMM_WORLD, &proc_rank);

    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    int x = atoi(argv[3]);
    double p = atof(argv[4]);
    int N = atoi(argv[5]);

    double start = MPI_Wtime();
    run_mc(a, b, x, p, N, proc_amount, proc_rank);
    if (!proc_rank) {
        ofstream f("stat_" + to_string((long long)(N)) + '_' + to_string((long long)(proc_amount)) + ".txt");
        f << a << ' ' << b << ' ' << x << ' ' << p << ' ' << N << endl << MPI_Wtime() - start << ' ' << proc_amount << endl;
        f.close();
    }
    MPI_Finalize();

    return 0;
}