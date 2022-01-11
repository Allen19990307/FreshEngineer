package JanWeek1Interview;

import java.util.HashSet;

/**
 * @Author:Allen
 * @Descrition:
 * @Date:1/11/2022 3:09 PM
 */
public class SameFactors {
     //使用HashSet，其中的元素个数不可重复，所以最终只会有5个元素。
    public static HashSet<Integer>  pare(int[] s1,int[] s2){
        HashSet<Integer> s3 =new HashSet<Integer>();
        for(int i = 0 ; i < s1.length ; i++){
           for(int j = 0 ; j < s2.length ; j++ ){
               if(s1[i] == s2[j]){
             //s1和s2 中相同的元素赋值给s3
                   s3.add(s1[i]);
               }
           }
        }
        return s3;
    }
    public static void main(String[] args) {
        int[] s1 = new int[]{1,2,3,4,63,3};
        int[] s2 = new int[]{1,2,3,4,63,3};
        HashSet<Integer> pare = pare(s1, s2);
        for(Integer se :pare){
            System.out.println(se+" ");
        }

        /*Iterator<Integer> iterator = pare.iterator();
        while(iterator.hasNext()){
            System.out.print(iterator.next()+" ");
        }*/

    }
}
