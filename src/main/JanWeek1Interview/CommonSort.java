package JanWeek1Interview;

/**
 * @Author:Allen
 * @Descrition: 常见的几种算法排序，冒泡排序及其优化，判断是否已经满足顺序的排列
 * @Date:1/16/2022 5:07 PM
 */
public class CommonSort {
   public static void BubbleSort(int[] s1){
      for(int i = 0 ; i < s1.length ; i++){
          for(int j = i + 1 ; j < s1.length ;j++){
            if(s1[i] > s1[j]){
                int temp = s1[j];
                s1[j] = s1[i];
                s1[i] = temp;
            }
          }
      }
   }
   /*优化1：最外层的是否已经为从小到大的顺序。 最外层已经满足顺序的排列，那么就恢复正常的排序情况*/
    public static void BubbleSort1(int[] s1){
        int j;
        for(int i = 0 ; i < s1.length ; i++){
            j = 0 ;
            for( j = i + 1 ; j < s1.length -1;j++){
                if(s1[j] > s1[j+1]){
                    int temp = s1[j];
                    s1[j] = s1[j+1];
                    s1[j+1] = temp;
                    j = 1;
                }
            }
            if(j == 0){
              return;
            }
        }
    }
    public static void main(String[] args) {
     int[] s1 = new int[]{1,2,31,4134,124,124,23,131,24};
       BubbleSort1(s1);
      for(int s2 : s1){
          System.out.print(s2+" ");
      }
    }
}
