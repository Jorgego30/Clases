#include "Class_BinarySearchTree.hpp"

class BinarySearchTreeAVL
{
    // references the TreeNode
    // that is the root of the binary search tree.
    private:
        TreeNode *root;
        int size;
        int balanceFactor;

        /*searches the binary tree comparing the new key to the key in the current node. If the new key is less than the current node, search the left subtree. If the new key is greater than the current node, search the right subtree.*/
        /* When there is no left (or right) child to search, we have found the position in the tree where the new node should be installed.*/
        /*To add a node to the tree, create a new TreeNode object and insert the object at the point discovered in the previous step.*/
        // this is all done recursively
        void _put(int key, string val, TreeNode *currentNode){
            if (key < currentNode->key){
                if (currentNode->hasLeftChild()){
                    this->_put(key, val, currentNode->leftChild);
                    
                }
                else{
                    currentNode->leftChild = new TreeNode(key, val, currentNode);
                    this->updateBalance(currentNode->leftChild);
                }
            }
            else{
                if (currentNode->hasRightChild()){
                    this->_put(key, val, currentNode->rightChild);
                }
                else{
                    currentNode->rightChild = new TreeNode(key, val, currentNode);
                    this->updateBalance(currentNode->rightChild);
                }
            }
        }

               // Uses the same search method as _put, and returns
        // a TreeNode to get
        TreeNode  *_get(int key, TreeNode *currentNode){
            if (!currentNode){
                return NULL;
            }
            else if (currentNode->key == key){
                return currentNode;
            }
            else if (key < currentNode->key){
                return this->_get(key, currentNode->leftChild);
            }
            else{
                return this->_get(key, currentNode->rightChild);
            }
        }

    public:
        BinarySearchTreeAVL()
        {
            this->root = NULL;
            this->size = 0;
            this->balanceFactor=0;
        }

        int length()
        {
            return this->size;
        }

        // Checks to see if the tree has a root,
        // if there is not a root then it will create a new TreeNode
        // and install it as the root of the tree.
        // If a root node is already in place than it calls _put
        // to search the tree
        void put(int key, string val){
            if (this->root){
                this->_put(key, val, this->root);
            }
            else{
                this->root = new TreeNode(key, val);
            }
            this->size = this->size + 1;
        }

        // prints string associated with key to console
        string get(int key){
            if (this->root){
                TreeNode *res = this->_get(key, this->root);
                if (res){
                    return res->payload;
                }
                else{
                    return 0;
                }
            }
            else{
                return 0;
            }
        }

        int updateBalance(TreeNode *node)
        {
            if (node->balanceFactor > 1 || node->balanceFactor < -1)
            {
                this->rebalance(node);
                return 0;
            }
            if (node->parent != NULL)
            {
                if (node->isLeftChild())

                    node->parent->balanceFactor += 1;

                else if (node->isRightChild())

                    node->parent->balanceFactor -= 1;

                if (node->parent->balanceFactor != 0)

                    this->updateBalance(node->parent);

            }
        }

        void rotateLeft(TreeNode *rotRoot)
        {
            TreeNode *newRoot = rotRoot->rightChild;
            rotRoot->rightChild = newRoot->leftChild;
            if (newRoot->leftChild != NULL){
                newRoot->leftChild->parent = rotRoot;
            }
            newRoot->parent = rotRoot->parent;
            if (rotRoot->isRoot()){
                this->root = newRoot;
            }
            else{
                if (rotRoot->isLeftChild()){
                    rotRoot->parent->leftChild = newRoot;
                }
                else{
                    rotRoot->parent->rightChild = newRoot;
                }
            }
            newRoot->leftChild = rotRoot;
            rotRoot->parent = newRoot;
            rotRoot->balanceFactor = rotRoot->balanceFactor + 1 - min(newRoot->balanceFactor, 0);
            newRoot->balanceFactor = newRoot->balanceFactor + 1 + max(rotRoot->balanceFactor, 0);
        }
        void rotateRight(TreeNode *rotRoot)
        {
            TreeNode *newRoot = rotRoot->leftChild;
            rotRoot->leftChild = newRoot->rightChild;
            if (newRoot->rightChild != NULL){
                newRoot->rightChild->parent = rotRoot;
            }
            newRoot->parent = rotRoot->parent;
            if (rotRoot->isRoot())
            {
                this->root = newRoot;
            }
            else{
                if (rotRoot->isRightChild()){
                    rotRoot->parent->rightChild = newRoot;
                }
                else{
                    rotRoot->parent->leftChild = newRoot;
                }
            }
            newRoot->rightChild = rotRoot;
            rotRoot->parent = newRoot;
            rotRoot->balanceFactor = rotRoot->balanceFactor - 1 - min(newRoot->balanceFactor, 0);
            newRoot->balanceFactor = newRoot->balanceFactor - 1 + max(rotRoot->balanceFactor, 0);
        }
        
        void rebalance(TreeNode *node){
            if (node->balanceFactor < 0){
                if (node->rightChild->balanceFactor > 0){
                    this->rotateRight(node->rightChild);
                    this->rotateLeft(node);
                }
                else{
                    this->rotateLeft(node);
                }
            }
            else if (node->balanceFactor > 0){
                if (node->leftChild->balanceFactor < 0){
                    this->rotateLeft(node->leftChild);
                    this->rotateRight(node);
                }
                else {
                    this->rotateRight(node);
                }
            }
        }
        
        void del(int key){
            if (this->size > 1){
                TreeNode *nodeToRemove = this->_get(key, this->root);
                if (nodeToRemove){
                    this->remove(nodeToRemove);
                    this->size = this->size - 1;
                }
                else{
                    cerr << "Error, key not in tree" << endl;
                }
            }
            else if (this->size == 1 && this->root->key == key){
                this->root = NULL;
                this->size = this->size - 1;
            }
            else{
                cerr << "Error, key not in tree" << endl;
            }
        }

        void remove(TreeNode *currentNode){
            if (currentNode->isLeaf()){ //leaf
                if (currentNode == currentNode->parent->leftChild){
                    currentNode->parent->leftChild = NULL;
                }
                else{
                    currentNode->parent->rightChild = NULL;
                }
            }
            else if (currentNode->hasBothChildren()){ //interior
                TreeNode *succ = currentNode->findSuccessor();
                succ->spliceOut();
                currentNode->key = succ->key;
                currentNode->payload = succ->payload;
            }
            else{ // this node has one child
                if (currentNode->hasLeftChild()){
                    if (currentNode->isLeftChild()){
                        currentNode->leftChild->parent = currentNode->parent;
                        currentNode->parent->leftChild = currentNode->leftChild;
                        this->updateBalance(currentNode->leftChild);
                    }
                    else if (currentNode->isRightChild()){
                        currentNode->leftChild->parent = currentNode->parent;
                        currentNode->parent->rightChild = currentNode->leftChild;
                        this->updateBalance(currentNode->leftChild);
                    }
                    else{
                        currentNode->replaceNodeData(currentNode->leftChild->key,
                                                        currentNode->leftChild->payload,
                                                        currentNode->leftChild->leftChild,
                                                        currentNode->leftChild->rightChild);
                    }

                }
                else{
                    if (currentNode->isLeftChild()){
                        currentNode->rightChild->parent = currentNode->parent;
                        currentNode->parent->leftChild = currentNode->rightChild;
                        this->updateBalance(currentNode->rightChild);
                    }
                    else if (currentNode->isRightChild()){
                        currentNode->rightChild->parent = currentNode->parent;
                        currentNode->parent->rightChild = currentNode->rightChild;
                        this->updateBalance(currentNode->rightChild);
                    }
                    else{
                        currentNode->replaceNodeData(currentNode->rightChild->key,
                                                        currentNode->rightChild->payload,
                                                        currentNode->rightChild->leftChild,
                                                        currentNode->rightChild->rightChild);
                    }
                }
            }
        }
};