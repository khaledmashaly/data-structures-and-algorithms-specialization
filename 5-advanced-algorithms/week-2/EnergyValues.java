import java.util.Scanner;

class AugMatrix {
    private int n;
	private double[][] a;
    private double[] b;
    private int lastPivotRow = -1;
    private int lastPivotCol = -1;

    private double getA(int row, int col) {
        return a[row][col];
    }

    void setA(double a, int row, int col) {
        this.a[row][col] = a;
    }

    void setB(double b, int row) {
        this.b[row] = b;
    }

    void setLastPivot(int row, int col) {
        this.lastPivotRow = row;
        this.lastPivotCol = col;
    }

    AugMatrix(int n) {
        this.n = n;
		this.a = new double[n][n];
		this.b = new double[n];
	}

	/*void print() {
        System.out.println('\n');
		for(int row = 0; row < n; ++row) {
		    for(int col = 0; col < n; ++col) {
		        System.out.print(a[row][col] + " ");
            }
            System.out.println("| " + b[row]);
        }
        System.out.println('\n');
	}*/


    void sol() {
        StringBuilder sol = new StringBuilder();
        for(int row = 0; row < n; ++row) {
            sol.append(b[row]).append(' ');
        }
        System.out.println(sol);
    }

	int[] getPivot() {
        if (lastPivotRow == n-1) return null;
		int col = lastPivotCol + 1, row = lastPivotRow + 1;
		outerLoop:
		for (; col < n; ++col) {
		    row = lastPivotRow + 1;
			for (; row < n; ++row) {
				if (a[row][col] != 0) break outerLoop;
			}
		}

		if (row == n && col == n && getA(n - 1, n - 1) == 0)
		    return null;

		return new int[] {row, col};
	}

    void scalePivotRow() {
        double pivot = a[lastPivotRow][lastPivotCol];
        scaleRow(lastPivotRow, pivot);
    }

    /**
     * scale a row by the given scalar
     * @param row - 0-based index of row to scale
     * @param scalar - value to scale row by
     */
	private void scaleRow(int row, double scalar) {
		for (int col = 0; col < n; ++col) {
			a[row][col] /= scalar;
		}
		b[row] /= scalar;
	}

	void subtractRows() {
        for(int row = 0; row < n; ++row) {
            if (row == lastPivotRow) continue;
            double scalar = a[row][lastPivotCol];
            for(int col = 0; col < n; ++col) {
                a[row][col] -= a[lastPivotRow][col] * scalar;
            }
            b[row] -= b[lastPivotRow] * scalar;
        }
	}

	int swapPivotRow(int pivotRow) {
        if (pivotRow == lastPivotRow + 1) return pivotRow;
        swapRows(pivotRow, lastPivotRow + 1);
        return lastPivotRow + 1;
    }

	private void swapRows(int firstRow, int secondRow) {
		double tmp;
		for (int col = 0; col < n; ++col) {
			tmp = a[firstRow][col];
			a[firstRow][col] = a[secondRow][col];
			a[secondRow][col] = tmp;
		}
		tmp = b[firstRow];
		b[firstRow] = b[secondRow];
		b[secondRow] = tmp;
	}
}


class EnergyValues {
	private static AugMatrix readMatrix() {
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		AugMatrix augMatrix = new AugMatrix(n);
		for (int row = 0; row < n; ++row) {
			for (int col = 0; col < n; ++col) {
				augMatrix.setA(scanner.nextDouble(), row, col);
			}
            augMatrix.setB(scanner.nextDouble(), row);
		}
		return augMatrix;
	}

	public static void main (String[] args) {
		AugMatrix augMatrix = readMatrix();
		for(;;) {
            int[] pivot = augMatrix.getPivot();
            if (pivot == null) break;
            int row = pivot[0], col = pivot[1];
            row = augMatrix.swapPivotRow(row);
            augMatrix.setLastPivot(row, col);
            augMatrix.scalePivotRow();
            augMatrix.subtractRows();
        }
        augMatrix.sol();
	}
}
