package JanWeek1Interview;

import org.apache.spark.sql.catalyst.plans.logical.Sort;

/**
 * @Author:Allen
 * @Descrition: 吴军老师的新书《计算之魂》自己整理了下其中提到的算法
 * 常见的几种算法排序，冒泡排序及其优化，判断是否已经满足顺序的排列   时间复杂度： n^2
 * 主流的算法：归并排序，堆排序，快速排序  时间复杂度： n*logn
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
    /*实现归并排序，分而治之的思想
    * Attention: boundary is important in this section,because we need to consider the process that we calculate
    * */
    public static void Sort1(int[] s1,int left,int right){
       int[] temp = new int[s1.length];
       Sort2(s1,left,right,temp);
    }
    public static void Sort2(int[] s1,int left,int right,int[] temp){
        if(left < right){
            int mid = (right + left) / 2;
            Sort2(s1, left ,mid,temp);
            Sort2(s1,mid + 1,right,temp);
            MergeSort(s1,left,mid,right,temp);
        }

    }
    public static void MergeSort(int[] s1,int left,int mid,int right,int[] temp){
       int i = left;
       int j = mid + 1;
       int t = 0 ;
       //限制条件的选择
       while (i < mid + 1 && j<= right){
           if(s1[i] <= s1[j]){
             temp[t++] = s1[i++];
           }else {
             temp[t++] = s1[j++];
           }
       }
       while( j <= right){
          temp[t++] = s1[j++];
       }
       while( i <= mid){
          temp[t++] = s1[i++];
       }
       t = 0;
       while(left <= right){
           s1[left++] = temp [t++];
       }
    }
    public static void main(String[] args) {
     int[] s1 = new int[]{1,2,31,4134,124,124,23,131,24};
//       BubbleSort1(s1);
        Sort1(s1,0,s1.length - 1  );

      for(int s2 : s1){
          System.out.print(s2+" ");
      }
    }
}
