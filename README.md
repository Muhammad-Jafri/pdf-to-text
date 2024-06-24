# PDF to TEXT Convertor


## Installation

Step-by-step instructions on how to get the development environment running.

```bash
# Clone the repository
git clone https://github.com/Muhammad-Jafri/pdf-to-text.git

# Navigate to the project directory
cd pdf-to-text/

# Create the pdf folder and paste the pdf files there
mkdir pdfs

# Create the output folder
mkdir txts

# Build the docker container
docker build -t pdf-to-text-converter .

# Mount the local folders to docker and then run the container
docker run --rm -v "$(pwd)/pdfs:/usr/src/app/pdfs" -v "$(pwd)/txts:/usr/src/app/txts" pdf-to-text-converter
