#######################################################
# 
# JSONCheck.py
# Python implementation of the Class JSONCheck
# Generated by Enterprise Architect
# Created on:      25-Oct-2016 12:41:38
# Original author: Jane Lewis
# 
#######################################################
import json
from CovgValidator import CovgValidator
from CovgCollValidator import CovgCollValidator
from DomainValidator import DomainValidator
from ParamValidator import ParamValidator


def enum(**enums):
    return type('Enum', (), enums)


def loadfile(filename):
    """
    :param filename: full path/name of json file to load
    :return: dictionary containing json object
    """
    with open(filename) as file:
        return json.load(file)


class JSONCheck:
    """
    Load the JSON file to be checked, delegate to appropriate validation class depending on main type.
    """
    def __init__(self):
        """

        :return:
        """
        self.m_top_node_key = "type"
        self.top_node_value_dict = {"Coverage": CovgValidator(),
                                    "CoverageCollection": CovgCollValidator(),
                                    "Domain": DomainValidator(),
                                    "Parameter": ParamValidator()}
        self.m_validator = None

    def check_json(self, filename):
        """
        Checks for main object type of Coverage or CoverageCollection only at present.
        note: other types allowed: Domain, NdArray, TiledNdArray - these all appear within a coverage usually

        :param filename: full path/name of json file to validate
        :return: none
        :raise: Exceptions TBD
        """
        # read the JSON file to be checked
        json_data = self.loadfile(filename)
        # check the resulting dict based on top-level nodes - one of the main types above
        try:
            the_validator = self.top_node_value_dict[json_data.get(self.m_top_node_key)]
            the_validator.validate_json(json_data)
        except:
            # it's neither so raise error
            raise json.jsonschema.SchemaError("File is not recognised.")


