package JanWeek1Interview;



/**
 * @Author:Allen
 * @Descrition:二叉树的深度优先遍历
 * @Date:1/10/2022 8:56 PM
 */
public class MaximumDepthofBinaryTree {
    public static class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
      TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
          this.right = right;
      }
  }
    public static int count(TreeNode s1){
        if(s1 == null){
            return  0 ;
        }else{
           int left = count(s1.left);
           int right  = count(s1.right);
          return Math.max(left,right)+1;
        }
    }

    public static void main(String[] args) {
        TreeNode s1 = new TreeNode(){};
        int count = count(s1);
        System.out.println("Max Depth: "+count);
    }
}
