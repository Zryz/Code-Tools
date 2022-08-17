#include <iostream>
#include <string>
#include <vector>
#include "ttt.h"

int main() {
game_board();
int p1_played;
int p2_played;
int plays = 0;
while (!winning() && plays < 9) {
if (turn == false) {
      std::cout << "1-2-3\n";
      std::cout << "4-5-6\n";
      std::cout << "7-8-9\n";
      std::cout << "Player 1: ";
      std::cin >> p1_played;
      p1_choice(p1_played -1);
      game_board();
      plays++;
}
else {
      std::cout << "1-2-3\n";
      std::cout << "4-5-6\n";
      std::cout << "7-8-9\n";
      std::cout << "Please choose your square Player 2: ";
      std::cin >> p2_played;
      p2_choice(p2_played -1);
      game_board();
      plays++;
}
}
if (plays == 9 && !winning()) {
  std::cout << "It is a draw!\n";
}
else if (turn == true) {
  std::cout << "Congratulations Player 1. You won!\n";
}
else {
  std::cout << "Congratulations Player 2. You won!\n";
}
}
