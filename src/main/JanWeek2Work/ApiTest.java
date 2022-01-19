package JanWeek2Work;


import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

/**
 * @Author:Allen
 * @Descrition: 使用Api获取数据
 * @Date:1/19/2022 11:05 AM
 */
public class ApiTest {
    public static String request(String httpUrl,String httpArg) {
        BufferedReader reader = null;
        String result = null;
        StringBuffer sbf = new StringBuffer();
        //httpUrl = httpUrl + "?" + httpArg;
        try {
            URL url = new URL(httpUrl);
            HttpURLConnection connection = (HttpURLConnection) url
                    .openConnection();
            connection.setRequestMethod("GET");
            InputStream is = connection.getInputStream();
            reader = new BufferedReader(new InputStreamReader(is, "UTF-8"));
            String strRead = null;
            while ((strRead = reader.readLine()) != null) {
                sbf.append(strRead);
                sbf.append("\r\n");
            }
            reader.close();
            result = sbf.toString();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return result;
    }

    public static void main(String[] args) {
        /**
         * @param urlAll
         *            :请求接口
         * @param httpArg
         *            :参数
         * @return 返回结果
         */
        String httpUrl = "http://gc.ditu.aliyun.com/geocoding?a=深圳";
        String httpArg="";
        System.out.println(request(httpUrl,httpArg));
    }
}
