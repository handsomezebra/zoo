import torch
from transformers import AlbertTokenizer, AlbertModel

pretrained_weights = 'albert-xxlarge-v2'
tokenizer = AlbertTokenizer.from_pretrained(pretrained_weights)
model = AlbertModel.from_pretrained(pretrained_weights)


def predict(text_list):
    tokenization_result = [tokenizer.encode(t, add_special_tokens=True, max_length=512) for t in text_list]
    print(tokenization_result)
    input_ids = torch.tensor(tokenization_result)  # Add special tokens takes care of adding [CLS], [SEP], <s>... tokens in the right way for each model.
    with torch.no_grad():
        last_hidden_states = model(input_ids)  # Models outputs are now tuples

    return last_hidden_states


if __name__ == "__main__":
    result = predict(["[CLS] Hello a world!", "How are you? [SEP]"])
    print(result[0].shape, result[1].shape, result)