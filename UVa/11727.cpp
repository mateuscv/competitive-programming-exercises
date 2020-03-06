#include<stdio.h>
#include<algorithm>

using namespace std;

int main(){
    int number_of_test_cases;
    int salaries[3];

    scanf("%d", &number_of_test_cases);

    for (size_t i = 0; i < number_of_test_cases; i++){
        for (size_t j = 0; j < 3; j++){
            scanf("%d", &salaries[j]);
        }
        sort(salaries, salaries+3);
        printf("Case %d: %d\n", i+1, salaries[1]);    
    }

    return 0;
}