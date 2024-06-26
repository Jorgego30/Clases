#include <iostream>
#include <vector>
using namespace std;

// Checks to see if item is in a vector returns true or false (1 or 0) using ordered sequential Search
bool orderedSequentialSearch(vector<int> avector, int item) 
{
    unsigned int pos = 0;
    bool found = false;
    bool stop = false;
    while (pos < avector.size() && !found && !stop) 
        if (avector[pos] == item) 
            found = true;
        else 
            if (avector[pos] > item) 
                stop = true;
            else 
                pos++;
    return found;
}

int main() 
{
    // Vector initialized using an array
    int arr[] = {0, 1, 2, 8, 13, 17, 19, 32, 42};
    vector<int> testvector(arr,arr+(sizeof(arr)/sizeof(arr[0])));

    cout << orderedSequentialSearch(testvector, 3) << endl;
    cout << orderedSequentialSearch(testvector, 13) << endl;

    return 0;
}


