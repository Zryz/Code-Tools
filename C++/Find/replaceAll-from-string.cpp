#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_set>

int main(){
  std::string word = "Bob";
  std::string text = "This is Bob. He is a good Bob. The best Bob. The one true Bob to rule all Bob's.";
  std::string asterisks;
  for (int a=0;a<word.length();a++)
  {
    asterisks += "*";
  }
  int occurrences = 0;
  std::string::size_type start = 0;
  while ((start = text.find(word, start)) != std::string::npos) {
    ++occurrences;
    start += word.length();
}
  for (int i=0;i<occurrences;i++){
    text.replace(text.find(word, i), word.size(), asterisks);
  }
  std::cout << text;
  }
