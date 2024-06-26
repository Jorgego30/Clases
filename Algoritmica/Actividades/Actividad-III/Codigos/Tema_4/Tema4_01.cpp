#include <iostream>
#include <vector>
using namespace std;

// Checks to see if item is in a vector returns true or false (1 or 0) using sequential Search
bool sequentialSearch(vector<int> avector, int item) 
{
    unsigned int pos = 0;
    bool found = false;

    while (pos < avector.size() && !found) 
        if (avector[pos] == item) 
            found = true;
        else 
            pos++;
    return found;
}

int main() 
{
    // Vector initialized using an array
    int arr[] = {1, 2, 32, 8, 17, 19, 42, 13, 0};
    vector<int> testvector(arr,arr+(sizeof(arr)/sizeof(arr[0])));

    cout << sequentialSearch(testvector, 3) << endl;
    cout << sequentialSearch(testvector, 13) << endl;

    return 0;
}

