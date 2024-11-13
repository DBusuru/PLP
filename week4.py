def read_and_modify_file(input_filename, output_filename):
    try:
        # Try to open the input file for reading
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (for example, convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Successfully read from {input_filename} and wrote to {output_filename}.")
    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except IOError:
        print(f"Error: Could not read from {input_filename} or write to {output_filename}.")

def main():
    # Ask the user for the input and output file names
    input_filename = input("Enter the name of the file to read from: ")
    output_filename = input("Enter the name of the file to write to: ")

    # Perform the read and write operation with error handling
    read_and_modify_file(input_filename, output_filename)

# Call the main function
if __name__ == "__main__":
    main()
