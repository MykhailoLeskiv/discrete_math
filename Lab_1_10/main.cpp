#include "functions.h"
using namespace std;
int main()
{
	setlocale(LC_ALL, "ukr");
	int n;
	cout << "Введiть розмiрнiсть матрицi: "; cin >> n;
	bool **matrix;
	matrix = new bool *[n];
	for (int i = 0; i < n; i++)
		matrix[i] = new bool[n];
	char choice;
	cout << "Автоматична генерацiя? "; cin >> choice;
	if (choice == 'y') AutoGenerate(matrix, n);
	else ManualGenerate(matrix, n);
	cout << "Матриця вiдношення R: " << endl;
	PrintMatrix(matrix, n);
	cout << "\nМатриця транзитивного замикання R: " << endl;
	PrintMatrix(CalcTransientClosureMatrix(matrix, n), n);
	delete[] matrix;
	system("pause");
	return 0;
}