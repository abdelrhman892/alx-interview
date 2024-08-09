import sys


def is_safe(board, row, col, N):
    # Check this column on upper rows
    for i in range(row):
        if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
            return False
    return True


def solve_nqueens_util(board, row, N, solutions):
    if row == N:
        # A solution is found, append the board configuration to solutions
        solution = [[i, board[i]] for i in range(N)]
        solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens_util(board, row + 1, N, solutions)
            # Backtrack (not necessary to reset, as it will be overwritten)


def solve_nqueens(N):
    board = [-1] * N
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    return solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
