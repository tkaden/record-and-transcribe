import pandas as pd
import re
import os


# Function to create a text file from a timestamp and corresponding output
def create_text_file(timestamp, content, directory):
    # Replace ':' and '.' with '_'
    filename_timestamp = re.sub(r'[:.]', '_', timestamp)
    # Define the file path with the proper name
    file_path = os.path.join(directory, f'{filename_timestamp}.txt')
    # Write the content to the file
    with open(file_path, 'w') as file:
        file.write(content)
    print(file_path)
    return file_path

# Function to read the CSV and create text files
def process_csv_and_create_files(csv_file_path, output_directory):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Loop through the DataFrame
    for index, row in df.iterrows():
        # Check if the 'output' column is not empty or NaN
        if pd.notna(row['output']):
            timestamp = row['timestamp']
            output = row['output']
            # Create a text file for each non-empty 'output'
            create_text_file(timestamp, output, output_directory)

# Example usage:
# The paths are placeholders and should be replaced with actual paths where the log.csv file is located
# and where the user wants to save the output text files.

# Path to the CSV file
csv_file_path = 'flagged/log.csv' # Replace with the actual path

# Directory where text files will be saved
output_directory = 'output' # Replace with the actual path

# Call the function to process the CSV and create files
process_csv_and_create_files(csv_file_path, output_directory)
