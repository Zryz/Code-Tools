#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_set>

void replaceAll(std::string& str, const std::string& from, const std::string& to);
void make_asterisks(std::string str);
std::string asterisks;

int main(){
  std::string word = "Bob";
  std::string text = "This is Bob. He is a good Bob. The best Bob. The one true Bob to rule all Bob's.";
  make_asterisks(word);
  replaceAll(text, word, asterisks);
  std::cout << text;
}
void make_asterisks(std::string str){
for (int a=0;a<str.length();a++)
{
  asterisks += "*";
}
}
void replaceAll(std::string& str, const std::string& from, const std::string& to) {
  if(from.empty())
      return;
  size_t start_pos = 0;
  while((start_pos = str.find(from, start_pos)) != std::string::npos) {
      str.replace(start_pos, from.length(), to);
      start_pos += to.length(); // In case 'to' contains 'from', like replacing 'x' with 'yx'
  }
}
