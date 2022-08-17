std::vector<char> board(9, ' ');
void game_board();
bool winning();
void p1_choice(int p1);
void p2_choice(int p2);
bool turn = false;

bool winning() {
    bool solved = false;
    if ((board[0] == board[3]) && (board[0] == board[6]) && board[0] != ' ') {
      return true;
    }
    else if ((board[1] == board[4]) && (board[1] == board[7]) && board[1] != ' ') {
      return true;
    }
    else if ((board[2] == board[5]) && (board[2] == board[8]) && board[2] != ' ') {
      return true;
    }
    else if ((board[0] == board[1]) && (board[0] == board[2]) && board[0] != ' ') {
      return true;
    }
    else if ((board[3] == board[4]) && (board[3] == board[5]) && board[3] != ' ') {
      return true;
    }
    else if ((board[6] == board[7]) && (board[6] == board[8]) && board[6] != ' ') {
      return true;
    }
    else if ((board[0] == board[4]) && (board[0] == board [8]) && board[0] != ' ') {
      return true;
    }
    else if ((board[6] == board[4]) && (board[6] == board [2]) && board[6] != ' ') {
        return true;
      }
    return solved;
}


void p1_choice(int p1){
if (board[p1] == ' '){
board[p1] = 'X';
turn = true;
std::cout << "\033[2J\033[1;1H";
}
else if (board[p1] == 'X' || board[p1] == 'O'){
  std::cout << "Slot taken! Try again!\n";
  turn = false;
}
}

void p2_choice(int p2){
if (board[p2] == ' '){
board[p2] = 'O';
turn = false;
std::cout << "\033[2J\033[1;1H";
}
else if (board[p2] == 'X' || board[p2] == 'O'){
  std::cout << "Slot taken! Try again!\n";
  turn = false;
}
}

void game_board(){
std::cout << board[0] << " || " << board[1] << " || " << board [2] << "\n";
std::cout << "__||___||__\n";
std::cout << board[3] << " || " << board[4] << " || " << board [5] << "\n";
std::cout << "__||___||__\n";
std::cout << board[6] << " || " << board[7] << " || " << board [8] << "\n";
std::cout << "__||___||__\n";
}
