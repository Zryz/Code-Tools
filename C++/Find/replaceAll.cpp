#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_set>

int main(){
  std::string text;
  std::cout << "Enter text to search: ";
  std::getline(std::cin, text);
  std::string find;
  std::cout << "Enter word to find: ";
  std::getline(std::cin, find);
  std::string replace;
  std::cout << "Enter what to replace with: ";
  std::getline(std::cin, replace);
  int occurrences = 0;
  std::string::size_type start = 0;
  while ((start = text.find(find, start)) != std::string::npos) {
    ++occurrences;
    start += find.length();
}
  for (int i=0;i<occurrences;i++){
    text.replace(text.find(find, i), find.size(), replace);
  }
  std::cout << text << "\n";
  }
