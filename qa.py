from transformers import BertForQuestionAnswering,pipeline
from transformers import AutoTokenizer

model=BertForQuestionAnswering.from_pretrained('deepset/bert-base-cased-squad2')
tokenizer=AutoTokenizer.from_pretrained('deepset/bert-base-cased-squad2')

nlp=pipeline("question-answering",model='deepset/bert-base-cased-squad2',tokenizer='deepset/bert-base-cased-squad2')

f=open('test.txt')
usr=input("Enter your question :")
QA_input={
    'question':usr,
    'context': f.read()
}
res=nlp(QA_input)
if res['score']>0.1:
    print("Response :",res['answer'])
    
else:
    print('answer not found')