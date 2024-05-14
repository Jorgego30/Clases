//Problema 2.- Implementar un programa en C++ que realice todos los recorridos (preorden, inorden, postorden y
//recorrido en anchura) del árbol siguiente:
#include <iostream>
#include <queue>

using namespace std;

// Definición de la estructura de un nodo del árbol
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// Función para recorrido preorden: Raíz -> Izquierda -> Derecha
void preOrder(TreeNode* root) {
    if (root != nullptr) {
        cout << root->val << " ";
        preOrder(root->left);
        preOrder(root->right);
    }
}

// Función para recorrido inorden: Izquierda -> Raíz -> Derecha
void inOrder(TreeNode* root) {
    if (root != nullptr) {
        inOrder(root->left);
        cout << root->val << " ";
        inOrder(root->right);
    }
}

// Función para recorrido postorden: Izquierda -> Derecha -> Raíz
void postOrder(TreeNode* root) {
    if (root != nullptr) {
        postOrder(root->left);
        postOrder(root->right);
        cout << root->val << " ";
    }
}

// Función para recorrido en anchura
void breadthFirst(TreeNode* root) {
    if (root == nullptr) return;
    
    queue<TreeNode*> q;
    q.push(root);
    
    while (!q.empty()) {
        TreeNode* current = q.front();
        q.pop();
        
        cout << current->val << " ";
        
        if (current->left != nullptr) q.push(current->left);
        if (current->right != nullptr) q.push(current->right);
    }
}

int main() {
    // Construcción del árbol
    TreeNode* root = new TreeNode(17);
    root->left = new TreeNode(8);
    root->right = new TreeNode(25);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(12);
    root->right->left = new TreeNode(20);
    root->right->right = new TreeNode(32);
    root->left->left->left = new TreeNode(1);
    root->left->left->right = new TreeNode(6);
    root->left->right->left = new TreeNode(10);
    
    // Realizar los recorridos
    cout << "Recorrido preorden: ";
    preOrder(root);
    cout << endl;
    
    cout << "Recorrido inorden: ";
    inOrder(root);
    cout << endl;
    
    cout << "Recorrido postorden: ";
    postOrder(root);
    cout << endl;
    
    cout << "Recorrido en anchura: ";
    breadthFirst(root);
    cout << endl;
    
    return 0;
}
