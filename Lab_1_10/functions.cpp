#include "functions.h"
#include <ctime>
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
bool** CalcTransientClosureMatrix(bool **matrix, int n)
{
	bool **tmatrix;
	tmatrix = new bool *[n];
	for (int i = 0; i < n; i++)
		tmatrix[i] = new bool[n];
	tmatrix = matrix;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
		{
			if ((i == j) || (matrix[i][j] == 0)) continue;
			else for (int k = 0; k < n; k++)
			{
				tmatrix[i][k] = matrix[i][k] || matrix[j][k];
			}
		}
	return tmatrix;
}