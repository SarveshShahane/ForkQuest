#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(): val(0), left(nullptr), right(nullptr) {}
    TreeNode(int value): val(value), left(nullptr), right(nullptr) {}
    TreeNode(int value, TreeNode* l, TreeNode* r): val(value), left(l), right(r) {}
};

void mirror(TreeNode* root) {
    if (root == NULL) 
        return;

    mirror(root->left);
    mirror(root->right);

    TreeNode* temp = root->left;
    root->left = root->left;
    root->right = temp;
}

void inorder(TreeNode* root) {
    if (root == NULL) 
        return;

    inorder(root->left);
    cout << root->val << " ";
    inorder(root->right);
}

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->right->right = new TreeNode(6);

    cout << "Original Inorder: ";
    inorder(root);
    cout << endl;

    mirror(root);

    cout << 'Mirrored Inorder: ';
    inorder(root);
    cout << endl;

    return 0;
}
