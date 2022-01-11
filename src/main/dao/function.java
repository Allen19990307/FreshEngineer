package dao;

import java.util.Scanner;

/**
 * @Author:Allen
 * @Descrition: 极致刻意练习，创造巅峰水平
 * @Date:1/10/2022 9:14 AM
 */
public class function {
    public static void CsFunction() {
        System.out.println("请输入你的英文名：   ");
        Scanner scanner = new Scanner(System.in);
        String next1 = scanner.next();
        System.out.println("在接下的2022，__承诺夯实基础，极致刻意练习");
        System.out.println("请输入宣誓人的姓名：   ");
        String next = scanner.next();
        if(!next.equals(next1)){
            System.out.println("有缘再见");
        }else{
            System.out.println("需要掌握的底层知识：计算机网络，计算机组成原理，操作系统，数据结构");
            System.out.println("需要完善的算法计算：Leetcode的高频算法");
        }
    }
}
