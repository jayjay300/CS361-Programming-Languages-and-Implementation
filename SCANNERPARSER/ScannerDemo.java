

/*
 * @author Christelle
 * 
 */
public class ScannerDemo {
//JOHN MULCAHY AND JEN MCCALL
	//private static String file1 = "C:\\Users\\John\\Desktop\\file.txt";
	private static String file1 = "C:\\Users\\cscharff\\Desktop\\TESTSCANNERPARSER2010\\GIVEN\\PARSER\\prog2.jay";
	private static int counter = 1;

	public static void main(String args[]) {

		TokenStream ts = new TokenStream(file1);

		System.out.println(file1);
		Token t;
		//int tcount = 1;
		while (!ts.isEndofFile()) {
			t= ts.nextToken();
			if(t == null || t.getValue() == ""){
				if(!ts.isEndofFile()){								//also skipped comments are recognized as null. I believed comments should be seen as null, are they?
					System.out.println("Token " + counter);
			System.out.println("Token is null");	
			counter++;
				}
			}
			else{
				//System.out.println("Token is not null"); necessary if every token is not null? comment out 
				//System.out.println(t.toString());
				System.out.println("Token " + counter);
				System.out.print("Type: "+t.getType());
				System.out.println("  Value: "+t.getValue());
				counter++;
			}
			t.toString();
		}
	}
}
