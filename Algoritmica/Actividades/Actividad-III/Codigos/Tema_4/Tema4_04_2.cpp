#include <iostream>
using namespace std;

// Checks to see if item is in a vector returns true or false (1 or 0) using binary Search and uses start and end indices
bool binarySearch(int arr[], int start, int end, int item)
{
    if (end >= start)
    {
        int mid = start + (end - start) / 2;
        if (arr[mid] == item)
            return true;
        if (arr[mid] > item)
            return binarySearch(arr, start, mid - 1, item);
        else
            return binarySearch(arr, mid + 1, end, item);
    }

    return false;
}

int main(void)
{
    int arr[] = {0, 1, 2, 8, 13, 17, 19, 32, 42};
    int arrLength = sizeof(arr) / sizeof(arr[0]);

    cout << binarySearch(arr, 0, arrLength, 3) << endl;
    cout << binarySearch(arr, 0, arrLength, 13) << endl;

    return 0;
}
