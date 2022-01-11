package JanWeek1Interview;

/**
 * @Author:Allen
 * @Descrition:
 * @Date:1/10/2022 10:12 AM
 */
public class MaximumDistance {
    //方案一： 暴力拆解方法
    public static int pair(int[] s1, int[] s2){
        int outcome = 0 ;
        int res = 0 ;
//
      for(int i = 0; i < s1.length; i++){
          for(int j = 0 ; j < s2.length ;j++){
             if(i <= j && s1[i] <= s2[j]) {
                outcome = j-i;
             }
             if(outcome >= res){
                 res =outcome ;
             }
          }
      }
       return res;
    }
    public static void main(String[] args) {
//        int[] s1 = new int[]{55, 30, 5, 4, 2};
//        int[] s2 = new int[]{100, 20, 10, 10,5};
//        int[] s1 = new int[]{2,2,2};
//        int[] s2 = new int[]{10, 10, 1};
        int[] s1 = new int[]{ 30, 29, 19, 5};
        int[] s2 = new int[]{25,25,25,25,25};
        int pair = pair(s1, s2);
        System.out.println("Maximum Distance is "+pair);
    }
}
