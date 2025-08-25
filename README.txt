*regex-input-anonym.py*
	'A command-line application that anonymizes sensitive information in text by replacing email addresses and phone numbers with generic tags.'
	Features:
		-Email Address Detection: Finds and replaces email addresses with *email* tags
		-Phone Number Recognition: Detects and anonymizes phone numbers with *phone* tags
		-File Saving: Option to save anonymized text to a file for future reference

*anonomizer.py*
	'A Streamlit web application that anonymizes sensitive information in text, protecting personal data by replacing identifiable information with generic tags.'
	Features:
		-Named Entity Recognition: Identifies and anonymizes names, organizations, locations, and other entities using SpaCy's advanced NLP capabilities
		-Email Address Detection: Finds and replaces email addresses with <email> tags
		-Download Functionality: Allows users to download the anonymized text as a .txt file
	Dependencies:
		-Spacy
		-Streamlit
		-en_core_web_lg (SpaCy language model)




