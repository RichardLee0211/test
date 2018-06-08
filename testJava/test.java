import java.io.*;
// import

class test_internal{
    public int j;
    public double what;
    public char c;
    public String str;
}

public class test extends test_internal{
    public int i;
    public static void main(String[] args){
        System.out.println("hello");
    }

    public int getI() {
        return i;
    }

    public void setI(int i) {
        this.i = i;
        this.c = 'w';
    }

    @Override
    public String toString() {
        return "test{" +
            "i = " + getI() +
            "}";
    }

}
