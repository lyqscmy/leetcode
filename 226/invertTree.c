struct TreeNode *invertTree(struct TreeNode *root) {
  if (root == NULL) {
    return root;
  }

  if (root->left != NULL) {
    root->left = invertTree(root->left);
  }

  if (root->right != NULL) {
    root->right = invertTree(root->right);
  }

  struct TreeNode *tmp = root->left;
  root->left = root->right;
  root->right = tmp;
  return root;
}
