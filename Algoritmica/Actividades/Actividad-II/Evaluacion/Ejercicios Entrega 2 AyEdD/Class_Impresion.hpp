#include <cstdlib>

class Task {
public:
    Task(int time) {
        marcatiempo = time;
        pages=(rand()%20) + 1;
    }

    int getmarca() {
        return marcatiempo;
    }

    int getPages() {
        return pages;
    }

    int waitTime(int currenttime) {
        return (currenttime - marcatiempo);
    }

public:
    int marcatiempo;
    int pages;
};

bool operator<(Task a, Task b) {return a.marcatiempo < b.marcatiempo ? true : false;}

class Printer {
public:
    Printer(int pagesPerMinute) {
        pagerate = pagesPerMinute;
        timeRemaining=0;
        working = false;
    }

    void tick() {
        
        if (working) { 
            timeRemaining--;
            if (timeRemaining <= 0)
                working = false; 
        }
    }

    bool busy() {
        return working;
    }

    void startNext(Task newtask) {
        currentTask=newtask;
        timeRemaining=newtask.getPages()*60/pagerate;
        working = true;
    }

private:
    int pagerate; 
    Task currentTask = {0};
    bool working; 
    int timeRemaining; 
};
