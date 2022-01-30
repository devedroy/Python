#include<iostream>

using namespace std;

int logNb2(int n) {
  if (n == 0) {
    return 0;
  }
  else {
      return 1 + logNb2(n / 2);
  }
}

int main() {
    int n;
    cout<< "Enter N" << endl;
    cin >> n;
    cout << "Log " << n << " base 2 is: " << endl;
    cout << logNb2(n);
}