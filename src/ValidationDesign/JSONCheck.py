#######################################################
# 
# JSONCheck.py
# Python implementation of the Class JSONCheck
# Generated by Enterprise Architect
# Created on:      25-Oct-2016 12:41:38
# Original author: Bug
# 
#######################################################
import json
import jsonschema

from Validator import Validator
from CovgValidator import CovgValidator
from CovgCollValidator import CovgCollValidator
from DomainValidator import DomainValidator
from ParamValidator import ParamValidator

def enum(**enums):
    return type('Enum', (), enums)

class JSONCheck:
    """Load the JSON file to be checked, subdivide according to sections, pass each
    section to relevant validator.
    """
    def __init__(self):
        self.m_covg_nodes = enum(the_type="type", domain="domain", params="parameters",
                                 ranges="ranges", range_alt="rangeAlternates")

        self.m_covg_coll_nodes = enum(the_type="type", domain="domainType", params="parameters",
                                      the_ref="referencing", covgs="coverages")

        # self.m_val_index = enum(covg=0, covg_coll=1, domain=2, param=3)

        # self.m_validators = [0] * 4  # 4 validator instances
        # self.m_validators[self.m_val_index.domain] = DomainValidator()
        # self.m_validators[self.m_val_index.param] = ParamValidator()
        # self.m_validators[self.m_val_index.covg] = CovgValidator(self.m_covg_nodes)
        # self.m_validators[self.m_val_index.covg_coll] = CovgCollValidator(self.m_covg_coll_nodes)

        self.m_covg_validator = CovgValidator(self.m_covg_nodes)
        self.m_covg_coll_validator = CovgCollValidator(self.m_covg_coll_nodes)

    def check_json(self, filename):
        # read the JSON file to be checked
        json_data = self._loadfile(filename)
        # check the resulting dict based on top-level nodes - one or other of enums above
        if json_data.has_key(self.m_covg_nodes.domain):
            # it's a normal coverage so pass to appropriate validator
            self.m_covg_validator.validate_json(json_data)
        elif json_data.has_key(self.m_covg_coll_nodes.domain):
            # it's a coverage collection so pass to appropriate validator
            self.m_covg_coll_validator.validate_json(json_data)
        else:
            # it's neither so raise error
            raise jsonschema.SchemaError("File is not a coverage or coverage collection.")

    def _divide_nodes(self):
        pass

    def _loadfile(self, filename):
        with open(filename) as file:
            return json.load(file)