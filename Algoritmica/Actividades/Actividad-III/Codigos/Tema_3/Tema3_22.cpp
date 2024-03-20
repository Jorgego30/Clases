#include <iostream>
#include <vector>
using namespace std;

int dpMakeChange(vector<int> coinValueList, int change, vector<int> minCoins)
{
    for (int cents = 0; cents < change + 1; cents++)
    { //loop finds solution for all sets of change from 0 to int change.
        int coinCount = cents;
        for (int j : coinValueList)
            if (j <= cents)
                if (minCoins[cents - j] + 1 < coinCount)
                    coinCount = minCoins[cents - j] + 1; //assigns the number of coins that is used to make the change.
        minCoins[cents] = coinCount;
    }
    return minCoins[change];
}

int main()
{
    vector<int> coinValueList = {1, 5, 10, 21, 25};
    int change = 63;
    vector<int> minCoins(64, 0);
    cout << dpMakeChange(coinValueList, change, minCoins) << endl;
    return 0;
}
