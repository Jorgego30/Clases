#include <iostream>
#include <ctime>
#include <vector>
using namespace std;

// Tests the time of the vector "push_back()" operation

void test1(int num)
{
    vector<int> vect;
    for (int i = 0; i < num; i++)
        vect.push_back(i);
}

int main()
{
    int numruns = 10000;
    clock_t begin_t1 = clock();
    for (int i = 0; i < numruns; i++)
        test1(numruns);

    clock_t end_t1 = clock();
    double elapsed_secs = double(end_t1 - begin_t1);
    cout << fixed << endl;
    cout << "push_back " << elapsed_secs << " microseconds" << endl;

    return 0;
}
