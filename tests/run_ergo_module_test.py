import sys
import yaml
from pyergo import \
    pyergo_start_session, pyergo_end_session,       \
    pyergo_command, pyergo_query,                   \
    HILOGFunctor, PROLOGFunctor,                    \
    ERGOVariable, ERGOString, ERGOIRI, ERGOSymbol,  \
    ERGOIRI, ERGOCharlist, ERGODatetime,            \
    ERGODuration, ERGOUserDatatype,                 \
    pyxsb_query, pyxsb_command,                     \
    XSBFunctor, XSBVariable, XSBAtom, XSBString,    \
    PYERGOException, PYXSBException

HOME = '/Users/hadfield/Local/vital-git/vital-logic-python/'
CONFIG = HOME + 'logic_config.yaml'


def load_config():
    with open(CONFIG, "r") as config_stream:
        try:
            return yaml.safe_load(config_stream)
        except yaml.YAMLError as exc:
            print("Exception with config file.")


config = load_config()
ERGO_ROOT = config['logic_engine']['ERGO_ROOT']
XSB_DIR = config['logic_engine']['XSB_DIR']


def main():
    pyergo_start_session(XSB_DIR, ERGO_ROOT)
    pyergo_command("writeln('Hello World!')@\\plg.")
    pyergo_command("add {'/Users/hadfield/Local/vital-git/vital-logic-python/test_rules/test_rules.ergo' >> logic}.")
    for row in pyergo_query('?C::Thing@logic, Socrates:?C@logic.'):
        # print("row", row[0])
        [(XVarname, XVarVal)] = row[0]
        # Xresult = XVarname + '=' + str(XVarVal)
        class_result = str(XVarVal)[1:-1]
        # print("result: ", Xresult, row[1], row[2], row[3].value)
        print("Socrates classification: " + class_result)
    for row in pyergo_query('?C::Thing@logic, Merlin:?C@logic.'):
        # print("row", row[0])
        [(XVarname, XVarVal)] = row[0]
        class_result = str(XVarVal)[1:-1]
        print("Merlin classification: " + class_result)
    pyergo_end_session()

# add module for domain
# load domain data

# repeat 10X
# add module for instance data
# load instance data and rules
# do query of instance data referencing domain data
# delete instance module

# reporting timing


if __name__ == "__main__":
    main()
