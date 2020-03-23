#include<iostream>
#include<vector>
#include<algorithm>
#include <bits/stdc++.h> 
using namespace std;

int main(){
 	int N, temp;
    vector<int> linha;
    cin >> N;
    for(int i = 0; i<N; i++){
    	cin >> temp;
        linha.push_back(temp);
    }
    sort(linha.begin(), linha.end())
   	for(int i = 0; i<N-1; i++){
		cout << linha[i] << " ";
    }
    cout << linha.back();
    return 0;
}