#include<iostream>

using namespace std;

void n21(int n) {
    if (n == 0) {
        return;
    }
    n21(n-1);
    cout << n << endl;
}

int main() {
    int n;
    cout<< "Enter N" << endl;
    cin >> n;
    cout << "1 2 N:" << endl;
    n21(n);
}