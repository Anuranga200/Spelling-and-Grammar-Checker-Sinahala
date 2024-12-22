from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer

def setup_grammar_checker():
    model_name = "ai4bharat/indic-bert"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(model_name)
    return pipeline("fill-mask", model=model, tokenizer=tokenizer)

def check_grammar_sinhala(sentence, nlp_pipeline):
    tokens = sentence.split()
    suggestions = []
    for idx, token in enumerate(tokens):
        masked_sentence = sentence.replace(token, nlp_pipeline.tokenizer.mask_token, 1)
        predictions = nlp_pipeline(masked_sentence)
        suggestions.append(predictions[0]['token_str'])
    return suggestions

if __name__ == "_main_":
    # Example input
    input_sentence = "මම විදුලී සංගීටය අගනාගයි"
    
    # Setup grammar checker
    nlp_pipeline = setup_grammar_checker()
    grammar_suggestions = check_grammar_sinhala(input_sentence, nlp_pipeline)
    print("Grammar Suggestions:", grammar_suggestions)