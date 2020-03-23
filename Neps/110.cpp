#include<iostream>
using namespace std;

int main(){
	int N, temp, temp2, biggest, seq;
    cin >> N;
    biggest = 1;
    seq = 1;
    for (int i = 0; i<N; i++){
    	cin >> temp2;
        if (i>0){
        	if(temp2 == temp){
            	seq++;
            } else {
                seq = 1;
            }
            if (seq > biggest){
            	biggest = seq;
            }
        }
        temp = temp2;
    }
    cout << biggest;
	return 0;
}