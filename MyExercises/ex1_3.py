import sys 

# 读文件 Data/portfolio.dat

def portfolio_cost(filename):
    total_cost = 0
    
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            try:
                shares = int(parts[1])
                price = float(parts[2])
                total_cost += shares * price
            except ValueError as e:
                print(f"Row {line} ignored due to ValueError: {e}")
                
    return total_cost

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: pcost filename")
    
    print(f"Args: {sys.argv}")

    filename = sys.argv[1]
    cost = portfolio_cost(filename)
    print(f"Total cost: {cost}")
