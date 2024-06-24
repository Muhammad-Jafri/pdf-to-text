import subprocess
import os
import sys

input_dir = "./pdfs"

def get_command(filename):
    return f"pdftotext -layout {filename} ./txts/{filename.split('/')[-1].replace('.pdf', '.txt')}"

def main():
    if not os.path.exists(input_dir):
        print("Input directory does not exist")
        sys.exit(1)

    if not os.path.exists("./txts"):
        os.makedirs("./txts")

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            command = get_command(f"{input_dir}/{filename}")
            subprocess.run(command, shell=True)
            
if __name__ == "__main__":
    main()
