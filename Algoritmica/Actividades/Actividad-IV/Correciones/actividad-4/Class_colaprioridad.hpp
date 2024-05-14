// uses a vector to creat a Binar Heap
#include <vector>
class BinHeapPrioridad{

private:
    
    int currentSize;

public:
    vector<int> heapvector;
    // initializes the vector and an attribute currentSize
    // as 0 to allow for interger division.
    BinHeapPrioridad(vector<int> heapvector){
        this->heapvector = heapvector;
        this->currentSize = 0;
    }

    // prelocates and item as far up in the
    // tree as possible to maintain
    // the Heap property
    void percUp(int i){
        while ((i / 2) > 0){
            if (this->heapvector[i] < this->heapvector[i/2]){
                int tmp = this->heapvector[i/2];
                this->heapvector[i/2] = this->heapvector[i];
                this->heapvector[i] = tmp;
            }
            i = i/2;
        }

    }

    // appends item to the end of the vector
    void insert(int k){
        this->heapvector.push_back(k);
        this->currentSize = this->currentSize + 1;
        this->percUp(this->currentSize);
    }

    // prelocates and item as far up in the
    // tree as possible to maintain
    // the Heap property
    void percDown(int i){
        while ((i*2) <= this->currentSize){
            int mc = this->minChild(i);
            if (this->heapvector[i] > this->heapvector[mc]){
                int tmp = this->heapvector[i];
                this->heapvector[i] = this->heapvector[mc];
                this->heapvector[mc] = tmp;
            }
            i = mc;
        }
    }

    int minChild(int i){
        if (((i*2)+1) > this->currentSize){
            return i * 2;
        }
        else{
            if (this->heapvector[i*2] < this->heapvector[(i*2)+1]){
                return i * 2;
            }
            else{
                return (i * 2) + 1;
            }
        }
    }

    // restores full complince with the heap structure
    // and heap order properties after the root is removed
    // by  taking the last item and moving it to the root position
    // and pushing the new root node down the tree to its proper postion.
    int delMin(){
        int retval = this->heapvector[1];
        this->heapvector[1] = this->heapvector[this->currentSize];
        this->currentSize = this->currentSize - 1;
        this->heapvector.pop_back();
        this->percDown(1);
        return retval;
    }

    void buildheap(vector<int> avector){
        int i = avector.size() / 2;
        this->currentSize = avector.size();
        this->heapvector.insert(this->heapvector.end(), avector.begin(), avector.end());
        while (i > 0){
            this->percDown(i);
            i = i - 1;
        }
    }

    bool isEmpty(){
        if (this->heapvector.size()>0){
            return false;
        }
        return true;
    }

    int findMin(){
        return this->heapvector[1];
    }

    void avanzar(int val){
        bool done = false;
        int i = 1;
        int miKey = 0;
        while ((done == false) and (i <= this->currentSize ))
        {
            if(this->heapvector[i] == val){
                done = true;
                miKey = i; 
            }
            else{
                i = i+1;
            }
        }
        if(miKey > 0){
            this->heapvector[miKey] = this->heapvector[miKey];
            percUp(miKey);
        }
        
    }
};