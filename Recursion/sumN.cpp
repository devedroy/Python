#include<iostream>

using namespace std;

int sumN(int n) {
  if (n == 1) {
    return 1;
  }
  else {
    return n + sumN(n - 1);
  }
 
}

int main() {
    int n;
    cout<< "Enter N" << endl;
    cin >> n;
    cout << sumN(n);
}