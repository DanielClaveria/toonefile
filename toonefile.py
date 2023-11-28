import os

def main():
    '''Genera archivo result.txt con todo el código del proyecto'''
    ''
    
    exclusions = ["__pycache__", "envpy", "result.txt"]

    main_folder_path = './'

    with open('result.txt', 'w') as result_file:
        result_file.write('')  # Clear the file

    for root, dirs, files in os.walk(main_folder_path):
        dirs[:] = [d for d in dirs if d not in exclusions]

        for file in files:
            if file not in exclusions:
                full_path = os.path.join(root, file)
                print(full_path)

                try:
                    with open(full_path, 'r') as f:
                        content = f.read()
                        print(content)                        
                        with open('result.txt', 'a') as result_file:
                            result_file.write(f"\n\nFile: {file}\n\n{content}\n")
                except Exception as e:
                    print(f"Error opening the file {file}: {str(e)}")


if __name__ == '__main__':
    main()
