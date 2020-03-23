#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main(){
    int T1,T2,T3;
    
    vector<int> pos;
    vector<int> sortedpos;
    cin >> T1;
    cin >> T2;
    cin >> T3;
    pos.push_back(T1);
    pos.push_back(T2);
    pos.push_back(T3);
    sortedpos = pos;
    sort(sortedpos.begin(), sortedpos.end());

    for (size_t i = 0; i < 3; i++){
        vector<int>::iterator itr = find(pos.begin(), pos.end(), sortedpos[i]);
        cout << distance(pos.begin(), itr)+1 << "\n";
    }
    
        
    return 0;
}