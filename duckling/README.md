# Duckling

This is the docker file for Duckling. Duckling is a Haskell library that parses text into structured data. [[code]](https://github.com/facebook/duckling)

## Usage
1. build
`docker build -t zoo_duckling .` 
2. run
`docker run -d -p 10000:10000 zoo_duckling`
3. test
`pytest` 
