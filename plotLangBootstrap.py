from pymeta.grammar import OMeta

def sumStrings(lst):
	str_sum = ""
	for string in lst:
		str_sum += string
	return str_sum

pymeta_file = open("plotlang_grammar.txt", "r")
exampleGrammar = pymeta_file.read()

farduino_source = open("bogusdata.pll", "r")
farduinoCode = farduino_source.read()

FarduinoCompiler = OMeta.makeGrammar(exampleGrammar, globals())
#Example = OMeta.makeGrammar(exampleGrammar, globals())

g = FarduinoCompiler(farduinoCode)
#g = Example("[1..6];")
result, error = g.apply("Program")

print(result)
output = open("test_plotlang.py", "w")
output.write(result)
output.close()
