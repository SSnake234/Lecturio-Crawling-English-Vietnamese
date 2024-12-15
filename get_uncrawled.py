import os

def get_uncrawled_files(folder_path):
    try:
        files = os.listdir(folder_path)
        for file in files:
            if len(file) >= 5:
                try:
                    file = file.replace('.json', '')
                    file_suffix = int(file[-5:])
                    print(file_suffix)
                except ValueError:
                    print(f"Cannot convert the last 5 characters of {file} to an integer.")
            else:
                print(f"File name {file} is too short to process.")
    except FileNotFoundError:
        print(f"The folder {folder_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

folder_path = "D:/Undergraduate Research/Lecturio"
get_uncrawled_files(folder_path)
uncrawled_indices = set(range(16146))  # Create a set of all possible indices from 0 to 12000

# Get the set of file_suffixes from the folder
file_suffixes = set()
try:
    files = os.listdir(folder_path)
    for file in files:
        if len(file) >= 5:
            try:
                file = file.replace('.json', '')
                file_suffix = int(file[-5:])
                file_suffixes.add(file_suffix)
            except ValueError:
                continue
except FileNotFoundError:
    print(f"The folder {folder_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

# Find the uncrawled indices
uncrawled_indices -= file_suffixes

# Write the uncrawled indices to a file
output_path = "uncrawled_index.txt"
try:
    with open(output_path, 'w') as f:
        for index in sorted(uncrawled_indices):
            f.write(f"{index}\n")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")