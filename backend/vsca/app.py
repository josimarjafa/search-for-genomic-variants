from flask import Flask, jsonify
from flask_cors import CORS

import pandas as pd

app = Flask(__name__)
CORS(app)


@app.route('/')
def root_home():
    return "Variant Search Coding Assignment (VSCA) by Josimar Andrade" \
           "\n\n Please search a gene variation with /gene/<gene_name> or /gene/autocomplete/<gene_name> for autocomplete"


@app.route('/gene/<string:name>')
def route_gene_auto(name: str):
    try:
        return dataset.getGene(name.upper()).to_json(orient='records')
    except KeyError:
        return []


@app.route('/gene/autocomplete/<string:name>')
def route_gene(name: str):
    return jsonify(dataset.getGeneAuto(name.upper()))

class Dataset:

    def __init__(self, file='data/variants.tsv'):
        self.readDataset(file)


    def getGene(self, name: str) -> pd.Series:
        return self.__data[self.__data['Gene']==name]


    def getGeneAuto(self, name: str) -> list:
        list_name = list(pd.unique(self.__data[self.__data['Gene'].str.contains(name)==True]['Gene']))
        list_name.sort()
        return list_name


    def getData(self):
        return self.__data


    def readDataset(self, file):
        app.logger.info("Set up dataset")
        # read the data and store data in DataFrame
        self.__data = pd.read_csv(file, sep='\t')
        # print a summary of the data in variants_data data
        app.logger.info(f"Dataset Loaded with {len(self.__data.index)} records")
        return self.__data

dataset = Dataset()


if __name__ == '__main__':
    app.run()
