package JanWeek1Interview;

/**
 * @Author:Allen
 * @Descrition:
 * @Date:1/11/2022 5:33 PM
 */
public class QuickSort {
    public  static void QuickSort(int[] s1){
        QuickFunc(s1,0,s1.length-1);
    }
    public static void QuickFunc(int[] s1,int left ,int right){
        //确定返回的基准值，左边的数值均小于右边的数值
        if(left >= right){
            return;
        }
        int index = Partition(s1,left,right);
        QuickFunc( s1,left,index - 1);
        QuickFunc( s1, index + 1 ,right);  //为什么不是index，而是index + 1呢？
    }
    public static int Partition(int[] s1,int left,int right){
        int privot =left  ;
        int index = privot + 1;
        for(int i = index ; i <= right ; i++){ //这边为什么需要i <= right
            if( s1[i] < s1[privot] ){
               swap(s1,i,index);  //基准值的确立
                index++;
            }
        }
        swap(s1,privot,index-1);
        return index - 1; //此处为何基准值需要减去1？
    }
    public static void swap(int[]s1,int i,int j){
        int temp = s1[j];
        s1[j] = s1[i];
        s1[i]  = temp;
    }
    public static void main(String[] args) {
        int[] s1 = new int[]{6,5,4,3,2,1};
        QuickSort(s1);
        for(int i = 0 ; i <s1.length ; i++){
            System.out.print(s1[i]+" ");
        }
    }
}
