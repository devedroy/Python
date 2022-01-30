#include<iostream>
using namespace std;

void func1() {
    cout << "func1" << endl;
}

void func2() {
    cout << "Before Func 1" << endl;
    func1();
    cout << "After Func 1" << endl;
}

int main() {
    cout << "Before Func 2" << endl;
    func2();
    cout << "After Func 2" << endl;
}