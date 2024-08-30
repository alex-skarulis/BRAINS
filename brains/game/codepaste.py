import os
from datetime import datetime

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Create the output file path
data_directory = os.path.join(current_directory, "../data/")

# Ensure the data directory exists
os.makedirs(data_directory, exist_ok=True)

# Generate the filename based on the current date and time
timestamp = datetime.now().strftime("%Y%m%d%H%M")
output_file_name = f"codepaste_{timestamp}.md"

# Create the full output file path
output_file_path = os.path.join(data_directory, output_file_name)

# Open the output file in write mode
with open(output_file_path, "w") as output_file:
    # Iterate over all files in the current directory
    for file_name in os.listdir(current_directory):
        file_path = os.path.join(current_directory, file_name)
        
        # Check if the file is a regular file and is a .py or text file
        if os.path.isfile(file_path) and file_name.endswith(('.py', '.txt')):
            # Open the file and read its contents
            with open(file_path, "r") as file:
                file_contents = file.read()
            
            # Write the file name and contents to the output file
            output_file.write(f"## {file_name}\n\n")
            output_file.write("```\n")  # Add newline after the opening backticks
            output_file.write(file_contents)
            output_file.write("\n```\n\n")  # Add newline before the closing backticks