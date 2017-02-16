import java.util.Arrays;

public class cd {
	public static void main(String[] args){
		Kattio kb = new Kattio(System.in, System.out);
		int n = kb.getInt();
	    int m = kb.getInt();
			while(n != 0 && m != 0){
			    int[] jack = new int[n];
			    for(int i=0;i<n;i++)
			        jack[i] = kb.getInt();
			    int cd = 0;
			    for(int k=0;k<m;k++)
			       if(java.util.Arrays.binarySearch(jack, kb.getInt())>-1)
			    	   cd++;
			    System.out.println(cd);
			    n = kb.getInt();
			    m = kb.getInt();
			}
			    
	}
}
