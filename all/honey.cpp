#include <iostream>
#include <string>

using namespace std;

int main(){
	int cases;
	cin >> cases;   //lol idek, here is the sequence tho
	long long nums[] = {1,0,6,12,90,360,2040,10080,54810,290640,1588356,8676360,47977776,266378112,1488801600,8355739392,47104393050,266482019232,1512589408044,8610448069080,49144928795820,281164160225520};
	for(int z = 0;z < cases; z++){
		int steps;
		cin >> steps;
		cout << nums[steps] << endl;
	}
}
