from happytransformer import HappyTextToText
from happytransformer import TTSettings

happy_tt = HappyTextToText("T5", "prithivida/grammar_error_correcter_v1")

text = "gec: " + " Whot do someone thinks of grammar checkers? Please not that they are not perfect. Style problems get a blue marker: It is 7 P.M. in the evening. The weather was nice on Monday, 22 November 2021"
settings = TTSettings(do_sample=True, top_k=10, temperature=0.5,  min_length=1, max_length=100)
result = happy_tt.generate_text(text, args=settings)

print(result.text)

# import language_tool_python 
# my_tool = language_tool_python.LanguageTool('en-US')

# my_text = """LanguageTool provides utility to check grammar and spelling errors. We just have to paste the text here and click the 'Check Text' button. Click the colored phrases for for information on potential errors. or we can use this text too see an some of the issues that LanguageTool can dedect. Whot do someone thinks of grammar checkers? Please not that they are not perfect. Style problems get a blue marker: It is 7 P.M. in the evening. The weather was nice on Monday, 22 November 2021"""   
   
# # getting the matches  
# my_matches = my_tool.check(my_text)  
  
# # printing matches  
# print(my_matches)  