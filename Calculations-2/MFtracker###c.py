'''

CodeVita 2015, MF Tracker
MF Tracker
Mani is a savvy investor. He is reviewing his financial investment performance. He is currently analyzing his investment into mutual funds he had made in the past. From those funds he earned a certain amount each. Coincidentally, it so happened that all the funds that Mani had invested in, had in turn invested the funds in same set of stocks. So when he exited, he exited all Mutual Funds at the same time. Mani has past statements from each Fund which tell him about the number of holdings of each stock and the value of the entire portfolio when he exited those funds.

Mani is now curious to find out what was the price of each stock across all funds when he exited. He wants to do this to find out if his decision to exit the funds based on today’s price was right or wrong. Your task is to help Mani find stock prices when he exited them.

Compute stock prices up to 11 decimal places and print them up to 2 decimal places.

Let’s say all funds invested in TCS, Infy and Wipro, then Mani has the following knowledge

Fund 1 -> # of shares of TCS, Infy and Wipro each and overall value of Mani’s portfolio
Fund 2 -> # of shares of TCS, Infy and Wipro each and overall value of Mani’s portfolio
Fund 3 -> # of shares of TCS, Infy and Wipro each and overall value of Mani’s portfolio
Input Format:
First line contains T, the number of test cases. The following lines contain:

First line contains a single number N which denotes two things

Number of stocks in each mutual fund
Number of funds is also same as N
Next N lines, each contain a tuple representing two things

The quantities of each of the N stocks in the fund, delimited by space
The value of the holdings in that fund
Output Format:
Print price of each stock, upto 2 decimal point, on one line (first one on first line, second one on second line … Nth one on Nth line). First stock is the one that comes first in the first tuple. Second stock is the one that comes second in the first tuple. So on and so forth.

OR

Print “Unsolvable” if the values of individual stocks cannot be calculated.

Sample Input / Output
Input:

10 9 8 56900
7 15 9 63200
12 8 1 49500
Output:

2600.00
2100.00
1500.00
Input:

10 9 8 56900
20 18 16 113800
30 27 24 170700
Output:

Unsolvable

'''

#include <iostream>
#include <cmath>
#include<cstdio>
#include <vector>
#include<iomanip>
using namespace std;
vector<double> gauss(vector< vector<double> > A) {
    int n = A.size();
    for (int i=0; i<n; i++) {
        double maxEl = abs(A[i][i]);
        int maxRow = i;
        for (int k=i+1; k<n; k++) {
            if (abs(A[k][i]) > maxEl) {
                maxEl = abs(A[k][i]);
                maxRow = k;
            }
        }
        for (int k=i; k<n+1;k++) {
            double tmp = A[maxRow][k];
            A[maxRow][k] = A[i][k];
            A[i][k] = tmp;
        }
        for (int k=i+1; k<n; k++) {
            double c = -A[k][i]/A[i][i];
            for (int j=i; j<n+1; j++) {
                if (i==j) {
                    A[k][j] = 0;
                } else {
                    A[k][j] += c * A[i][j];
                }
            }
        }
    }
    vector<double> x(n);
    for (int i=n-1; i>=0; i--) {
        x[i] = A[i][n]/A[i][i];
        for (int k=i-1;k>=0; k--) {
            A[k][n] -= A[k][i] * x[i];
        }
    }
    return x;
}
int main() {
    int n,f,h;
    cin>>f;
    for(h=0;h<f;h++){
    cin >> n;
    vector<double> line(n+1,0);
    vector< vector<double> > A(n,line);
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> A[i][j];
        }
        cin >> A[i][n];
    }
    vector<double> x(n);
    x = gauss(A);
    for (int i=0; i<n; i++) {
        if (x[i]>=0){
            if (i==0) printf("%.2f",x[i]);
            else
        printf("\n%.2f",x[i]);
        }
        else{
            cout<<"Unsolvable";
            break;}
    }
    cout << endl;}
}




