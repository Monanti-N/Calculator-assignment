def modify_content(content):
    # Example modification: Convert text to uppercase
    return content.upper()

def main():
    input_file = input("Enter the filename to read from: ")
    try:
        with open(input_file, 'r') as f:
            content = f.read()
            print("File read successfully.")
            
        modified_content = modify_content(content)
        
        output_file = "modified_" + input_file
        with open(output_file, 'w') as f:
            f.write(modified_content)
            print(f"Modified content written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except IOError:
        print(f"Error: Could not read from or write to file '{input_file}'.")

if __name__ == "__main__":
    main()
