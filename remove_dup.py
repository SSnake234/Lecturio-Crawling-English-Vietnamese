def remove_duplicates(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    print(f"Number of lines before removing duplicates: {len(lines)}")
    unique_lines = list(set(lines))
    
    with open(file_path, 'w') as file:
        file.writelines(unique_lines)
    print(f"Number of lines after removing duplicates: {len(unique_lines)}")

if __name__ == "__main__":
    remove_duplicates('links/lectures3.txt')