/**
 * stats review problem on www.hackerrank.com
    *
    * Let's review some statistics! Given a list of numbers, calculate its sample mean, sample median, sample mode, sample variance, and sample standard deviation.
    *
    * If you're not familiar with these terms do a little research! Please note that there are different equations for sample statistics vs population statistics.
    *
    * Input Format
    *
    * The only line of the input will consist of space delimited numbers.
    *
    * These numbers can be any valid floating point numbers or integers.
    *
    * Constraints
    * the number of float will between 1 and 1000
    * the value of float will between -2^10 and 2^10
    *
    * Output Format
    *
    * Output to STDOUT each of the following values on separate lines in the following order:
    *
    * sample mean
    * sample median
    * sample mode (If there are multiple, choose the smallest, if there are none, output an empty line)
    * sample variance
    * sample standard deviation
    * Each value should be rounded to the nearest integer.
 */

#include<iostream>
#include<algorithm>
#include<string>
#include<vector>

#include<cmath>
#include<cstring>
#include<stdio.h>

using namespace std;


/**
 * return the number of x in a[]
 */
int GeShu(float a[], int size, float x){
    int i,num = 0;

    for (i = 0; i < size; ++i)
    {
        if (x == a[i])
        {
            ++num;
        }
    }
    return num;
}

/**
 * return modd of a[]
 */
float Arr(float a[], int size){
    float temp = 0.0;
    int i;

    temp = a[0];
    for (i = 0; i < size; ++i)
    {
        if (GeShu(a, size, a[i]) < GeShu(a, size , a[i+1]))
        {
            temp = a[i+1];
        }
    }
    return temp;
}

#define CHAR_NUM_PER_LINE 102400

vector<float> myFloat;

void input_handler()
{
    char line[CHAR_NUM_PER_LINE];
    char* tmpStr;

    cin.getline(line, sizeof(line));
    tmpStr = strtok(line, " ");
    myFloat.push_back(stof(tmpStr));
    while((tmpStr = strtok(NULL, " ")) != NULL){
        myFloat.push_back(stof(tmpStr));
    }
}

int main()
{
    input_handler();

    int count=(int)myFloat.size();

    /* mean */
    float sum = 0.0;
    for(int i=0; i<count; i++){
        sum += myFloat[i];
    }
    float mean = sum/count;
    cout<<mean<<endl;

    /* median */
    sort(myFloat.begin(), myFloat.end());
    if(count%2 == 1)
        cout<<myFloat[count/2]<<endl;
    else{
        cout<<(myFloat[count/2]+myFloat[count/2+1])/2<<endl;
    }

    /**
     * mode
     * the number repeats most
     * because myFloat is already sorted, so find mode could be easy
     */

    float tmpModeNum = myFloat[0]; // the tmp Mode num
    int tmpCount = 0; // the count of tmp mode num
    int modeCount = 0; // the count of mode number
    int mode; // the one required

    for(int i=1; i<count; i++){
        if(myFloat[i] == tmpModeNum)
            tmpCount++;
        else{ // switch to another number
            tmpCount = 1;
            tmpModeNum = myFloat[i];
        }
        // find another possible mode num
        if(tmpCount > modeCount){
            modeCount = tmpCount;
            mode = (int)round(tmpModeNum);
        }
    }
    if(modeCount == 1)
        cout<<endl;
    else
        cout<<mode<<endl;

    // variance and deviation
    // s^2 = 1/n * ((x1-mean)^2 + (x2-mean)^2 + ... )
    double tmp =0.0;
    for(int i=0; i<count; i++){
        tmp += (double) (myFloat[i] - mean)*(myFloat[i] - mean);
    }
    unsigned long vari = (unsigned long) (tmp/(count-1));
    unsigned long deviat = (unsigned long) sqrt(tmp/(count-1));

    cout<<vari<<endl;
    cout<<deviat<<endl;

    return 0;
}
