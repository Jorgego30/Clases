#include <iostream>
#include <queue>
#include <vector>
#include <random>
#include <time.h>
#include <cstdlib>
#include "Class_Impresion.hpp"
using namespace std;



bool newPrintTask()
{
    
    return (rand() % 180 + 1) == 180;
}

void simulation(int numSeconds, int pagesPerMinute)
{
    Printer labprinter(pagesPerMinute);

    
    priority_queue<Task> printQueue;

    
    vector<int> waitingTimes;

    
    for (int i = 0; i < numSeconds; i++)
    {

        
        if (newPrintTask())
        {
            Task task(i);       
            printQueue.push(task); 
        }

        
        if (!labprinter.busy() && !printQueue.empty())
        {
            Task nextTask = printQueue.top(); 
            printQueue.pop();                   

            
            waitingTimes.push_back(nextTask.waitTime(i));
            labprinter.startNext(nextTask);
        }

        
        labprinter.tick();
    }

    
    float total = 0;
    for (int waitTime : waitingTimes)
        total += waitTime;

    cout << "Tiempo de espera medio " << total / waitingTimes.size() << " secs " << printQueue.size() << " Tarea(s) pendiente(s)." << endl;
}

int main()
{
    srand(time(NULL));

    for (int i = 0; i < 10; i++)
        simulation(3600, 6);

    return 0;
}