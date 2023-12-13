import os
import pandas as pd
from datetime import datetime

# Define the paths
flagged_csv_path = 'flagged/log.csv'
transcripts_dir = 'transcripts/'
output_dir = 'processed_flagged_data'
os.makedirs(output_dir, exist_ok=True)

# Read the CSV file
df = pd.read_csv(flagged_csv_path)

# Create a set of existing transcript filenames
existing_transcripts = set(os.listdir(transcripts_dir))

# Process each row in the CSV
for index, row in df.iterrows():
    timestamp = datetime.strptime(row['timestamp'], "%Y-%m-%d %H:%M:%S.%f")
    transcript_filename = f'{timestamp.strftime("%Y%m%d_%H%M%S")}.txt'
    transcript_filepath = os.path.join(transcripts_dir, transcript_filename)

    if transcript_filename not in existing_transcripts:
        # If the transcript does not exist, create one
        transcript_text = row['output']
        with open(transcript_filepath, 'w') as file:
            file.write(transcript_text)
        print(f"Created transcript: {transcript_filename}")
    else:
        print(f"Transcript already exists: {transcript_filename}")
