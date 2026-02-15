def total_salary(path):
    try:
        with open(path, 'r') as file:
            total = 0
            avg = 0
            count = 0
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        salary = float(parts[1])
                        total += salary
                        count += 1
                    except ValueError:
                        continue
            avg = total / count if count > 0 else 0
            return (total, avg) if count > 0 else (0, 0) 
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
result = total_salary('Salary.txt')
print(result)