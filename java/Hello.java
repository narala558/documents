import java.io.File;
import java.util.Arrays;


public class Hello {

    static String directoryName = "foo";
    static final int HOURS = 9001;

    public static void main(String[] args) {
        System.out.println("Hello, World!");
        System.out.println(HOURS);

        createFiles();

        Hello hello = new Hello();
        hello.createFiles();

        System.out.println("\n\n\nstring array");
        String[] s = hello.strings();
        System.out.println(s);
        System.out.println(s.length);
        for(String element:s) {
            System.out.println( element );
        }
        String theString = Arrays.toString(s);
        System.out.println(theString);
    }


    private static void createFiles() {
        File directory = new File(directoryName);
        if (!directory.exists()){
            directory.mkdir();
            // If you require it to make the entire directory path including parents,
            // use directory.mkdirs(); here instead.
        }
    }

    private String[] strings() {
        String[] data = new String[10];
        data = new String[] {"foo", "bar"};
        return data;
    }
}
