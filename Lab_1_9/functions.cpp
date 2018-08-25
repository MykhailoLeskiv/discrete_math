#include <iostream>
#include <ctime>
#include "functions.h"
using namespace std;
void AutoGenerate(bool **matrix, int n)
{
	srand(time(NULL));
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			matrix[i][j] = (rand() % 2);
}
void ManualGenerate(bool **matrix, int n)
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
		{
			cout << "¬ведiть елемент [" << i + 1 << "][" << j + 1 << "] : ";
			cin >> matrix[i][j];
		}
}
void PrintMatrix(bool **matrix, int n)
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
		{
			if (j != n - 1) cout << matrix[i][j] << " ";
			else cout << matrix[i][j] << endl;
		}
}
bool** MatrixMultiplicate(bool **matrix1, bool **matrix2, int n)
{
	bool **matrix;
	matrix = new bool *[n];
	for (int i = 0; i < n; i++)
	{
		matrix[i] = new bool[n];
	}
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
		{
			matrix[i][j] = 0;
			for (int k = 0; k < n; k++)
			{
				matrix[i][j] = matrix[i][j] || (matrix1[i][k] && matrix2[k][j]);
			}
		}
	return matrix;
}