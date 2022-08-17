#include <iostream>
#include <string>
#include <algorithm>


//declares a function that accepts referenced strings and returns the bleeped string
std::string bleep(std::string &str, std::string &sen);

//defines the behaviour of the bleep function
std::string bleep(std::string &str,std::string &sen) {
//transforms to lower case for case-insensitive comparison
  std::string lower = sen;
  std::transform(str.begin(), str.end(), str.begin(), ::tolower);
  std::transform(lower.begin(), lower.end(), lower.begin(), ::tolower);
//uses lower case for the searching parameters
//also keeps parameters of loop within limits of the text length (to avoid undefined behaviour)
  for (int i = 0; i < lower.length() - str.length(); ++i)
  {
//hit marker to count no. of times characters in a string match against word
    int hit = 0;
//increases hit marker by one each time the text contains a character found in word - whilst also cycling through each letter of the word
    for (int g=0; g<str.length(); g++)
      {
        if (lower[i+g] == str[g])
          {
            ++hit;
          }
      }
  //when the marker has managed to get to the same size as the word length i.e word is found - apply '*' to the un-transformed text
    if (hit == str.size())
      {
        for (int r=0; r<str.length();r++)
          {
            sen[i+r] = '*';
          }
      }
  }
 return sen;
}

int main() {
  //set the text to compare against the word to filter
  std::string word = "yellow";
  std::string text = "I was walking down the street under the yellow sun. I turned the corner and saw a yellow car with yellow wheels. yellow.";
  //apply the function to the data provided
  std::cout << bleep(word, text);
 }
