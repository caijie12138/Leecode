import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    public static int reverse(int x) {
        String result = "";
        int a = Math.abs(x);
        try {
            String res = String.valueOf(a);
            StringBuilder sb = new StringBuilder(res);
            if (x < 0)
                result = "-";
            result += sb.reverse().toString();
            return Integer.parseInt(result);
        } catch (Exception e) {
            return 0;
        }
       // return Integer.parseInt(result);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String l = bufferedReader.readLine();
        int x = Integer.parseInt(l);
        System.out.println(reverse(x));

    }
}

