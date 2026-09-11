import os
import sys


def open_files_recursively(current_path, target):
    """Recursively searches a directory tree for a target file and prints its contents.

        Performs a depth-first traversal starting from `current_path`. When `target` is
        found, its content is read and printed to stdout, and the program terminates
        immediately using `sys.exit()`.

        Args:
            current_path (str): The root or directory path to start searching from.
            target (str): The exact filename (e.g., 'draft.txt') to search for.

        Returns:
            None: The function doesn't return value; it exits the process upon finding
            the target file.

        Raises:
            FileNotFoundError: If `current_path` is not a valid directory on the OS.
            SystemExit: Terminates the entire Python interpreter session when the file is found.
        """
    items = os.listdir(current_path) # Get all items name (folders and files)

    for item in items: # Iterate through each item inside the current directory (item is just a string)
        # Construct the absolute/relative path so os functions know exact location
        full_path = os.path.join(current_path, item)

        # BASE CASE
        if os.path.isfile(full_path) and item == target: # If the current path is a file (e.g. my_workspace\notes.txt)
            print(f"\n📄 Opening file: {full_path}")
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"Content: {content}")
                sys.exit() # Instantly terminate the program
        # RECURSIVE CALL
        elif os.path.isdir(full_path):
            print(f"\n📂 Opening directory: {full_path}")
            # Pause current function frame and dive into the subfolder
            open_files_recursively(full_path, target) # Pass the current full_path and target as args


# --- MAIN EXECUTION ---
# Check if top-level directory exists before starting the search
starting_folder = "my_workspace"
target_filename = "draft.txt"

if os.path.exists(starting_folder):
    open_files_recursively(starting_folder, target_filename)
    # Note: If sys.exit() triggers inside the function, code below never executes.
    print(f"\nSearch complete: '{target_filename}' was not found in '{starting_folder}'.")
else:
    print(f"Error: The directory '{starting_folder}' does not exist!")


# Test case where item x.txt is inside of folder 1, item y.txt is inside of folder 3 and folder 3 are inside folder 2
# my_workspace\
# ├── folder_2\          <-- Sibling 1
# │   └── folder_3\       <-- child
# │       └── y.txt      <-- child also target
# └── folder_1\          <-- Sibling 2
#     └── x.txt          <-- child

# Let's stipulate that list dir give use a list of sorted str item
r"""
Iterate each item in the list. 

Iter-1:
    Fullpath become my_workspace\folder_1
    check if become false, elif true -> recursive call, param is current full_path and target
        new_scope:
            Iter-1:
                As usual join cause Fullpath to become my_workspace\folder_1\x.txt
                check if and elif become false (is an item but not target)
                return none and get out of that scope
        back to parent scope continue at line 41, oops no line left to execute, loop 1 is done.
Iter-2:
    Fullpath become my_workspace\folder_2
    elif is true, do the call.
    new_scope:
        items values it just 1 string which is folder_2, then iterate that (1) + join
        Fullpath become my_workspace\folder_2\folder_3
        check elif is true
        another new_scope:
            items have 1 str value y.txt
            iteration (1), Fullpath become my_workspace\folder_2\folder_3\y.txt
            check if is true then print + read, terminate all.
"""