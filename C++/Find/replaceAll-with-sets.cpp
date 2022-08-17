#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_set>

int main(){
  std::string word = "Bob";
  std::string text = "This is Bolb. He is a good Bob. The best Bob. The one true Bob to rule all Bob's'";
  std::unordered_set<int> locations;
  for (int i=0; i<text.length()-word.length();i++)
  {
    locations.insert(text.find(word, i));
  }
  for (int j=0; j<text.length();j++)
  {
    auto setLoc (locations.begin());
    for (int b=0; b<locations.size();b++)
    {
      for(int a=0;a<word.size() && *setLoc != -1;a++){
        text[*setLoc+a] = '*';
      }
    setLoc++;
    }
  }
   std::cout << text;
}
