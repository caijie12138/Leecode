import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    public static String convert(String s, int numRows) {
        int dist = 2 * numRows - 2;
        String result = "";
        if (s.length() == 0 || numRows == 0 || numRows == 1)
            return s;
        for (int i = 0; i < numRows; i++)//从第一行到最后一行
            for (int j = i; j < s.length(); j += dist) {
                result += s.charAt(j);
                if (i != 0 && i != numRows - 1 && j-2*i+dist <s.length())
                    result += s.charAt(j - 2*i + dist);
            }
            return result;

    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String s = bufferedReader.readLine();
        String num = bufferedReader.readLine();
        int n = Integer.parseInt(num);
        System.out.println(convert(s, n));

    }
}
