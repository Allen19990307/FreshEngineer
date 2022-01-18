package JanWeek2Work

import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.sql.SparkSession

/**
 * @Author:Allen
 * @Descrition:Spark基本的算子实现
 * @Date:1/17/2022 11:19 AM
 */
object WordCount {
  def main(args: Array[String]): Unit = {
    val sparkConf = new SparkConf().setAppName("WorkTime").setMaster("local[*]")
    val sparkContext = new SparkContext(sparkConf)
    sparkContext.setLogLevel("warn")
    val rootValue  = sparkContext.textFile("D:\\Allen‘s repository\\FreshEngineer\\src\\resource\\dreamCatcher.txt")
    val SplitValue1 = rootValue.flatMap(line => line.split(" "))
    val CountValue1 = SplitValue1.map(x => {
      (x, 1)
    })
    val Sumvalue = CountValue1.reduceByKey(_ + _)
    Sumvalue.foreach(print)



  }
}
