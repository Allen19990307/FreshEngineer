package JanWeek2Work

import org.apache.flink.api.java.utils.ParameterTool
import org.apache.flink.api.scala._
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment

/**
 * @Author:Allen
 * @Descrition: 关于Flink的基本概念和用法的练习使用
 * @Date:1/17/2022 3:58 PM
 */
object WordCount1 {
  def main(args: Array[String]): Unit = {
    /*设置一些连接的参数*/
//    val params = ParameterTool.fromArgs(args)
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    val value = env.readTextFile("src/resource/dreamCatcher2.txt")
    println(value)
  }
}
