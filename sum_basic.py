from typing import List


PUNCTUATION_CHARS = [",", "(", ")", ".", "%", "-"]


def get_rate_of_occurance_of_word_in_sentence(
    target_word: str,
    sentence,
) -> float:
    sentence_without_punctuation = "".join([
        char for char in sentence
        if char not in PUNCTUATION_CHARS
    ])
    
    words_in_sentence = sentence_without_punctuation.split(" ")
    
    frequence_of_target_word = 0
    for word_in_sentence in words_in_sentence:
        if word_in_sentence == target_word:
            frequence_of_target_word += 1
        
    return frequence_of_target_word / len(words_in_sentence)
    
    

def get_average_distribution_across_words(sentence):
    sentence_without_punctuation = "".join([
        char for char in sentence
        if char not in PUNCTUATION_CHARS
    ])
    
    words_in_sentence = sentence_without_punctuation.split(" ")
    
    distributions_for_unique_words = [
        get_rate_of_occurance_of_word_in_sentence(
            target_word=word_in_sentence,
            sentence=sentence_without_punctuation,
        )
        for word_in_sentence
        in words_in_sentence
    ]
    
    sum_of_weights = sum(distributions_for_unique_words)
    return sum_of_weights
    

def gather_summary(
    sentences: List[str],
    target_word: str,
    length_limit: int,
):
    best_sentence = None
    
    best_score = -float("inf")
    for sentence in sentences:
        words_in_sentence = sentence.split(" ")
        if target_word in words_in_sentence:
            score_for_sentence = get_average_distribution_across_words(sentence)
            if score_for_sentence > best_score:
                best_score = score_for_sentence
                best_sentence = sentence

    return condense_sentence(
        sentence=best_sentence,
        length_limit=length_limit,
    )

def condense_sentence(
    sentence: str,
    length_limit: int,
):
    # TODO: Condense sentence to have a size smaller than the lenght limit
    return sentence

print(
    get_average_distribution_across_words(
        sentence='blackberry  fruit fruit fruit fruit, with the fruit',
    )
)

# print(
#     get_unique_distribution(
#         target_word="fruit",
#         sentence='blackberry fruit, with the fruit',
#     )
# )


SENTENCES = [
  'The raspberry is the edible fruit of a multitude of plant species in the genus Rubus of the rose family, most of which are in the subgenus Idaeobatus',
  'The name also applies to these plants themselves',
  'Raspberries are perennial with woody stems',
  'World production of raspberries in 2020 was 895,771 tonnes, led by Russia with 20% of the total',
  'A raspberry is an aggregate fruit, developing from the numerous distinct carpels of a single flower',
  'What distinguishes the raspberry from its blackberry relatives is whether or not the torus (receptacle or stem) "picks with" (ie, stays with) the fruit',
  'When picking a blackberry fruit, the torus stays with the fruit',
  'With a raspberry, the torus remains on the plant, leaving a hollow core in the raspberry fruit',
  'Raspberries are grown for the fresh fruit market and for commercial processing into individually quick frozen (IQF) fruit, purée, juice, or as dried fruit used in a variety of grocery products such as raspberry pie',
  'Raspberries need ample sun and water for optimal development',
  'Raspberries thrive in well-drained soil with a pH between 6 and 7 with ample organic matter to assist in retaining water',
  'While moisture is essential, wet and heavy soils or excess irrigation can bring on Phytophthora root rot, which is one of the most serious pest problems facing the red raspberry',
  'As a cultivated plant in moist, temperate regions, it is easy to grow and has a tendency to spread unless pruned',
  'Escaped raspberries frequently appear as garden weeds, spread by seeds found in bird droppings'
  'An individual raspberry weighs 3-5 g (0.11-0.18 oz), and is made up of around 100 drupelets, each of which consists of a juicy pulp and a single central seed',
  'A raspberry bush can yield several hundred berries a year'
]
