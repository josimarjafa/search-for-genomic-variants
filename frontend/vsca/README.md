# Variant Search Coding Assignment (VSCA) by Josimar Andrade


## Assignment

Application that allows a user to search for genomic variants by gene name and display the results in a tabular view.

## Features

1. Allow the user to enter a gene name to search for variants in that gene. Display the results in a table that shows various attributes associated with each genomic variant.

2. Provide an auto-suggest feature for entering the gene name.

3. Provide two RESTful endpoints supporting the functionality listed in steps 1 and 2.


## Datasource

A zipped TSV file of variants is available in /data/variants.tsv.zip. Each row in the TSV file represents a genomic variant and contains a Gene column with the gene name. A variant will belong to one and only one gene, but multiple variants may belong to the same gene.



NOTE: All the development was made on Ubuntu 18.04.3 LTS x86_64

## Implementation

FrontEnd     --> React

Our expectation is you will be writing some server code, client code, and applying some basic styling to create a working web application. The application should include unit tests.

Here’s an example of how you might group and display the information:

![variants table example](./example_table.png)


## The result

![the result](./Screenshot.png)

## File directory

└── vsca
    ├── example_table.png
    ├── package.json
    ├── public
    │   ├── index.html
    │   └── i.png
    ├── README.md
    ├── Screenshot.png
    └── src
        ├── App.css
        ├── App.js
        ├── App.test.js
        ├── components
        │   ├── genes.js
        │   └── search.js
        ├── index.css
        ├── index.js
        ├── i.png
        └── logo.svg

## Installation (build and run) single server.

Install dependencies:
    npm install

## Tests

Backend:
    npm test
    
Result:
----------------------------------------------------------------------
 PASS  src/App.test.js
  ✓ renders without crashing (36ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   0 total
Time:        1.134s
Ran all test suites.


## Run single server.

start the server:
    npm start      

## Usage

Browser:
    http://localhost:3000/

## Scalability with Kubernetes

--- Not implemented

## High performance Test

--- Not implemented


## Submitting Your Solution

Please clone this repository and upload an archive to Greenhouse, or upload your repository to GitHub and send us a link. Update this README to include instructions on how to install, test, and run your application. Bonus: Deploy it and include the URL here.

As part of the review process, we may comment on or ask questions about specific parts of the code.

Please return your solution within 1 week. This is not an expectation of the time required to complete the assignment. Rather, it’s meant to provide buffer for busy schedules.

## License
Copyright (c) 2019. Josimar Andrade, No Rights Reserved


