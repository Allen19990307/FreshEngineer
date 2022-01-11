package JanWeek1Interview;

import java.util.HashSet;

/**
 * @Author:Allen
 * @Descrition:
 * @Date:1/10/2022 10:30 AM
 */
public class HashTrain  {

    public static int accumulate(String s) {
        int number = 0 ;
        int i = 0;
        char[] chars = s.toCharArray();
//        HashMap<Integer,Character> s1 = new HashMap<Integer,Character>();
        HashSet<Character> s1 = new HashSet<Character>();
        for(Character chars1:chars){
            if(!s1.contains(chars1)){
                s1.add(chars1);
                i = s1.size();
            }else if(i > number){
               number  = i ;
               s1.clear();
               s1.add(chars1);
            }else {
                i = 0;
            }
        }
        return number;
    }

    public static void main(String[] args) {
        String s = "pwwkew";
        String s1 = "bbbbb";
        String s2 = "abcabcbb";
        String s3 = "abb";
        int accumulate = accumulate(s3);
        System.out.println("Accumulate maximum:  "+accumulate);

    }
}
