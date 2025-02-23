import pandas as pd
import numpy as np

from sklearn.utils.class_weight import compute_class_weight

# merge two lists into a dataframe
'''
input: 
	l1: list1
	l2: list2
	c1_label: label1
	c2_label: label2
	
returns:
	merged df
'''
def merge_lists_df(l1, l2, c1_label, c2_label):
	if len(l1) != len(l2):
		print("Lists must be of equal size.")
		return
	else:
		list_of_tuples = list(zip(l1, l2))  
		df = pd.DataFrame(list_of_tuples, columns = [c1_label, c2_label])
		return df
		

# compute the class weights to deal with class imbalance
def get_cw(labels):
	class_wts = compute_class_weight('balanced', np.unique(labels), labels)
	class_wts = list(class_wts)
	return class_wts
	
# get contributory sentences
def get_cont_sent(data, pred):
	contr_sentences = list()
	for i in range(len(pred)):
		if pred[i] == 0:
			pass
		else:
			contr_sentences.append(data[i])
	return contr_sentences

def parse(text):
	tokenized_text = text.splitlines()
	sentences = ["Title"]
	headings_list = ["Abstract", "Introduction", "Results", "Experiments", "Conclusion"]
	# assuming the first two sentences comprise the title
	sentences.append(tokenized_text[0] + " " + tokenized_text[1])
	i = 2
	print(len(tokenized_text))
	while i < len(tokenized_text):
		if tokenized_text[i] in headings_list:
			sentences.append(tokenized_text[i])
			k = i + 1
			while True:
				if k == len(tokenized_text):
					break
				else:
					sentence = tokenized_text[k]
				if sentence in headings_list:
					break
				else:
					if len(sentence) > 5:
						sentences.append(sentence)
					k += 1
			i = k
		else:
			i += 1

	return sentences