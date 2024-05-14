void heapify(int arr[], int n, int i)
{
    int largest = i; // Initialize largest as root
    int l = 2 * i + 1; // left = 2*i + 1
    int r = 2 * i + 2; // right = 2*i + 2
 
    // If left child is larger than root
    if (l < n && arr[l] > arr[largest])
        largest = l;
 
    // If right child is larger than largest so far
    if (r < n && arr[r] > arr[largest])
        largest = r;
 
    // If largest is not root
    if (largest != i) {
        swap(arr[i], arr[largest]);
 
        // Recursively heapify the affected sub-tree
        heapify(arr, n, largest);
    }
}
 
// main function to do heap sort
void heapSort(int arr[], int n)
{
    // Build heap (rearrange array)
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
 
    // One by one extract an element from heap
    for (int i = n - 1; i > 0; i--) {
        // Move current root to end
        swap(arr[0], arr[i]);
 
        // call max heapify on the reduced heap
        heapify(arr, i, 0);
    }
}
void printArray(int arr[], int n)
{
    for (int i = 0; i < n; ++i)
        cout << arr[i] << " ";
    cout << "\n";
}

// uses a vector to creat a Binar Heap
class BinHeap{

private:
    vector<int> heapvector;
    int currentSize;

public:
    // initializes the vector and an attribute currentSize
    // as 0 to allow for interger division.
    BinHeap(vector<int> heapvector){
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

    void buildheap(int array[]){

        int n = sizeof(array)*2 / sizeof(array[0]);
        heapSort(array,n);

        vector<int> vector(array,array+(sizeof(array)*2 / sizeof(array[0])));

        int i = vector.size() / 2;
        this->currentSize = vector.size();
        this->heapvector.insert(this->heapvector.end(), vector.begin(), vector.end());
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
};


