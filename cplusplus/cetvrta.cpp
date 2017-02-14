#include <iostream>
#include <string>

using namespace std;

int main(){
	int x1,y1,x2,y2,x3,y3;
	cin >> x1 >> y1;
	cin >> x2 >> y2;
	cin >> x3 >> y3;
	int x[2] = {x2,x3};
	int y[2] = {y2,y3};
	int x4;
	int y4;
	if(x1 == x[0])
		x4 = x[1];
	else if(x1 == x[1])
		x4 = x[0];
	else
		x4 = x1;
	if(y1 == y[0])
			y4 = y[1];
	else if(y1 == y[1])
			y4 = y[0];
	else
			y4 = y1;
	cout << x4 << " " << y4 << endl;
}
