package JanWeek1Interview;

/**
 * @Author:Allen
 * @Descrition:  探究死锁发生的条件,这段代码双方都在等对方释放资源，是不是很像我们谈恋爱，总认为对方需要先服软。
 * @Date:1/13/2022 11:34 AM
 */
public class DeadLockDemo {
    private static String A = "A";
    private static String B = "B";

    public static void main(String[] args) {
         new DeadLockDemo().deadLock();
    }
    private void deadLock(){
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                synchronized (A) {
                    try {
                        Thread.sleep(2000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    synchronized (B) {
                        System.out.println("1");
                    }
                }
            }
        });
        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                synchronized (B) {
                    synchronized (A) {
                        System.out.println("2");
                    }
                }
            }
        });
        t1.start();
        t2.start();
    }


}
