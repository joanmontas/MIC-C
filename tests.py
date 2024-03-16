# Copyright Joan Montas
# All rights reserved.
# License under GNU General Public License v3.0

import unittest
# TODO(JoanMontas) turn test into its own class, an have a main entry point
if __name__ == "__main__":
    allTestsLocation = ["SyntacticAnalysis/test", "SemanticAnalysis/test"]

    allTests = unittest.TestSuite()
    for i in allTestsLocation:

        loader = unittest.TestLoader()
        suite = loader.discover(i, pattern="test*.py")
        allTests.addTest(suite)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(allTests)
