#include <iostream>

int main()
{
  std::cout << "Hello, World!";

  const char * p = "a" ;
  std::cout << p;
  char c;


  for (const char * p = "a" ; c = (*p); p++) {
    std::cout << c;
    std::cout << "i";
    std::cout << "\n";
  }
}
