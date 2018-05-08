import java.io.*;
// import

class test_internal{
    public int j;
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
    }

    @Override
    public String toString() {
        return "test{" +
            "i = " + getI() +
            "}";
    }

}
