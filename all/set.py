# #include <iostream>
# #include <string>
# #include <vector>
#
# using namespace std;
#
# int s(string a, string b, string c){
#   int no = 0;
#   int yes = 0;
#   for(int g = 0;g < 4;g ++){
#     if(a[g] == b[g] && b[g] == c[g]){
#       yes += 1;
#     }
#     if(a[g] != b[g] && b[g] != c[g] && a[g] != c[g]){
#       no += 1;
#     }
#   }
#   if(yes + no == 4){
#     return yes;
#   }
#   else
#     return 0;
# }
#
# int main()
# {
#   vector<string> cards;
#   for(int z = 0;z < 12;z ++){
#       string o;
#       cin >> o;
#       cards.push_back(o);
#   }
#   int h = 0;
#   for(int i = 0;i < 12;i ++){
#     for(int n = i + 1;n < 12;n ++){
#       for(int k = n + 1;k < 12;k ++){
#         if(s(cards[i], cards[n], cards[k]) != 0){
#           cout << i+1 << " " << n+1 << " " << k+1 << endl;
#           h += 1;
#         }
#       }
#     }
#   }
#   if(h == 0){
#     cout << "no sets";
#   }
# }
