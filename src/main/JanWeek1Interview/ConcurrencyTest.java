package JanWeek1Interview;

/**
 * @Author:Allen
 * @Descrition: 并发编程
 * @Date:1/11/2022 9:41 PM
 */
public class ConcurrencyTest {
    private static final long count = 100001;

    public static void main(String[] args) {

    }
    /*并发编程的情况*/
    public static void concurrency() throws InterruptedException {
        long start = System.currentTimeMillis();
        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                int a = 0;
                for (long i = 0; i < count; i++) {
                    a += 5;
                }
            }
        });
        thread.start();
        int b = 0;
        for(long i = 0 ; i <count ;i++){
             b--;
         }
        thread.join();
        long res = System.currentTimeMillis() - start;
        System.out.println("concurrency "+res+ " ms,b = "+b);
    }
    public static void serial(){

    }


}
