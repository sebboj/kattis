#include <string>
#include <iostream>

using namespace std;

int main(){
	int x,y,n;
	cin >> x >> y >> n;
	for(int z = 1;z <= n; z++){
		if(z%x == 0 && z%y == 0)
			cout << "FizzBuzz" << endl;
		else if(z%x == 0)
			cout << "Fizz" << endl;
		else if(z%y == 0)
			cout << "Buzz" << endl;
		else
			cout << z << endl;
	}
}
