#include<iostream>

using namespace std;

void n21(int n) {
    if (n == 0) {
        return;
    }
    cout << n << endl;
    n21(n-1);
}

int main() {
    int n;
    cout<< "Enter N" << endl;
    cin >> n;
    cout << "N 2 1:" << endl;
    n21(n);
}