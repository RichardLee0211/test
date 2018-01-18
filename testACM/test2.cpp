#include<iostream>
#include<string.h>

using namespace std;

int main(){
    unsigned int N = 0;
    cin>>N;
    unsigned int x, y, z;
    unsigned int recording[N][3];
    //memset(recording, 0, sizeof(recording));
    int i = 0;
    unsigned int sum=0;
    for(x=1; x<N; x++){
        for(y=1; y<N; y++){
            for(z=1; z<N; z++){
                if( x*x+y*y+z*z == N){
                    recording[i][0] = x;
                    recording[i][1] = y;
                    recording[i][2] = z;
                    //cout<<x<<" "<<y<<" "<<z<<endl;
                    i++;
                }
            }
        }
    }

    for(int j=0; j<i; j++){
        for(int h=j+1; h<i; h++){
            if(
                    (
                    recording[j][0] == recording[h][0] &&
                    recording[j][1] == recording[h][2] &&
                    recording[j][2] == recording[h][1])
                    ||
                    (
                    recording[j][0] == recording[h][1] &&
                    recording[j][1] == recording[h][0] &&
                    recording[j][2] == recording[h][2])
                    ||
                    (
                    recording[j][0] == recording[h][1] &&
                    recording[j][1] == recording[h][2] &&
                    recording[j][2] == recording[h][0])
                    ||
                    (
                    recording[j][0] == recording[h][2] &&
                    recording[j][1] == recording[h][1] &&
                    recording[j][2] == recording[h][0])
                    ||
                    (
                    recording[j][0] == recording[h][2] &&
                    recording[j][1] == recording[h][0] &&
                    recording[j][2] == recording[h][1])


                    ){
                recording[j][0] = 0;
                recording[j][1] = 0;
                recording[j][2] = 0;
            }
        }
    }

    for(int j=0; j<i; j++){
        sum += recording[j][0];
        sum += recording[j][1];
        sum += recording[j][2];
    }

    printf("%d\n", sum);
    return 0;
}
