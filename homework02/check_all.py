import time

import sudoku


def main():
    puzzles = ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]
    
    for filename in puzzles:
        print(f"\n{'='*50}")
        print(f"Решение {filename}")
        print('='*50)
        
        try:
            grid = sudoku.read_sudoku(filename)
            print("Начальное состояние:")
            sudoku.display(grid)
            
            start = time.time()
            solution = sudoku.solve(grid)
            end = time.time()
            
            if solution:
                print("\nРешение найдено:")
                sudoku.display(solution)
                
                if sudoku.check_solution(solution):
                    print(f"✓ Решение корректно! Время: {end-start:.3f} секунд")
                else:
                    print("✗ Решение некорректно!")
            else:
                print("✗ Решение не найдено!")
                
        except FileNotFoundError:
            print(f"Файл {filename} не найден")

if __name__ == "__main__":
    main()
