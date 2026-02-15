def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    name = parts[0].strip()
                    try:
                        cat_info = {"id": parts[0].strip(), "name": parts[1].strip(), "age": parts[2].strip()}
                        cats_list.append(cat_info)
                    except ValueError:
                        continue
        return cats_list
    except FileNotFoundError:
        print(f"File {path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    

cats_info = get_cats_info('Cats.txt')
print(cats_info)