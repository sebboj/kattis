#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(){
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int n,m;
	cin >> n;
	cin >> m;
	string words[n];

	for(int z = 0;z < n; z++){
		string g;
		cin >> g;
		words[z] = g;
	}

	for(int o = 0;o < m; o++){
		string s;
		cin >> s;
		transform(s.begin(), s.end(), s.begin(),::tolower);
		string gg = "";

		for(int i = 0;i < n; i++){
			string wo = words[i];
			if(wo.find(s[0]) != string::npos){
				wo = wo.substr(wo.find(s[0])+1);
				if(wo.find(s[1]) != string::npos){
					wo = wo.substr(wo.find(s[1])+1);
					if(wo.find(s[2]) != string::npos){
						wo = wo.substr(wo.find(s[2])+1);
						gg = words[i];
						break;
					}
				}
			}
		}

		if (gg.length() == 0)
			cout << "No valid word\n";
		else
			cout << gg << "\n";
	}
	return 0;
}
