package view;

import dao.function;

import java.util.Scanner;

/**
 * @Author:Allen
 * @Descrition:
 * @Date:1/9/2022 7:48 PM
 */
public class view {
    public static void main(String[] args) {
        System.out.println("欢迎来到okr的挑战世界");
        System.out.println("当你决心有所成就的时候，请输入大写的OKR:  ");
        Scanner scanner = new Scanner(System.in);
        String next = scanner.next();

        if("OKR".equals(next)){
            System.out.println("首先我们需要确定一些规则");
        }else{
            System.out.println("追求卓越方有传奇,我们高处相见");
        }
        function.CsFunction();

    }
}
