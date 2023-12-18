cd stanford-parser-2021-05-05
java -mx10g -cp "*;" edu.stanford.nlp.parser.lexparser.LexicalizedParser -outputFormat "penn,typedDependencies" edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz ..\shuffled.txt > ..\grammars.txt
pause