
public class ByteCodeTest {
	
	public static int factorial(int num)
	{
		  if (num == 0 || num == 1)
			  return 1;
		  else
			  return num * factorial(num-1);
	}
	
	int fact(int i, int acc) {
		  if ( i == 0 ) 
		    return acc;
		  else
		    return fact( i -1, acc * i);
		}

}
