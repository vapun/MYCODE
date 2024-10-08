#include <stdio.h>
#include <windows.h>
#include <conio.h>

void gotoxy(int x, int y);
void draw_ship(int x, int y);
void erase_ship(int x,int y);
void assignment2();

const int SHIP_LENGTH = 7;
const int SCREEN_WIDTH = 80;
const int SCREEN_HEIGHT = 24;

int main()
{
	// draw_ship(10, 5);
	// assignment2();

	// clear screen
	system("cls");

	char ch = ' ';
	int x = 2, y = 20;
	draw_ship(x, y);
	// move left/ right
	do {
		if (_kbhit()) {
			ch = _getch();
    
			// Assignment 3
			if (ch == 'a') {
                if(x-1 != -1){
                erase_ship(x,y);
                draw_ship(--x, y); 
                }
            }

			if (ch == 'd') {
                if(x+1 != 80){
                erase_ship(x,y);
                draw_ship(++x, y); }
            }

			if (ch == 'w') {
                if(y-1 != -1){
                erase_ship(x,y);
                draw_ship(x, --y); }
            }

			if (ch == 's') {
                if(y+1 != 24){
                erase_ship(x,y);
                draw_ship(x, ++y); }
            }

			fflush(stdin);
		}
		Sleep(500);
	// exit
	} while (ch != 'x');
	return 0;
}

void gotoxy(int x, int y)
{
	COORD c = { x, y };
	SetConsoleCursorPosition(
		GetStdHandle(STD_OUTPUT_HANDLE), c);
}

// Assignment 1
void draw_ship(int x, int y)
{
	gotoxy(x, y);
	printf(" <-0-> ");
}

// Assignment 2
void assignment2()
{
	for (int i = 1; i < SCREEN_WIDTH - SHIP_LENGTH; i++)
	{
		draw_ship(i, 20);
		Sleep(500);
	}

}

// Assignment 4
void erase_ship(int x,int y)
{
	gotoxy(x, y);
	printf("       ");
}
