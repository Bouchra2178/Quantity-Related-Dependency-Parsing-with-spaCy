import random
import spacy
from pathlib import Path
from tqdm import tqdm
from spacy.training.example import Example
# nlp = spacy.load("en_core_web_sm")

# phrases = [
#     "Many stars illuminated the night sky",
#     "Few clouds dotted the vast horizon",
#     "Several birds chirped in the early morning",
#     "Opportunities are numerous and await your exploration",
#     "Countless grains of sand covered the beach",
#     "Abundant flowers in the garden bloomed",
#     "Sufficient evidence supported the claim",
#     "The progress was hindered by limited resources",
#     "Infinite possibilities stretched before us",
#     "Ample time was given to complete the task",
#     "Excessive noise disrupted the otherwise peaceful environment",
#     "Sparse vegetation covered the expansive desert landscape",
#     "Adequate information was provided for better understanding",
#     "Scarce rainfall significantly affected the crop yield",
#     "Plentiful fruits adorned the trees",
#     "Substantial progress was made in the ongoing project",
#     "Minimal effort surprisingly yielded maximum results",
#     "The maximum speed was reached on the highway",
#     "Minimum requirements for eligibility must be met",
#     "Average rainfall for the region was recorded",
#     "Equal opportunities were given to candidates",
#     "Unequal distribution of wealth often leads to disparities",
#     "Sizable investments were wisely made in the stock market",
#     "Tiny insects quietly crawled on the forest floor",
#     "Huge waves suddenly crashed against the rocky shore",
#     "Gigantic mountains loomed in the distance",
#     "Small pebbles lined the riverbank",
#     "Large crowds suddenly gathered for the event",
#     "Vast plains extended as far as the eye could see",
#     "Time allocated for the presentation was limited",
#     "Unlimited access to resources was granted to members",
#     "All students actively participated in the school assembly",
#     "None of the cookies remained in the jar",
#     "Every person has a unique perspective",
#     "Each member significantly contributed to the team effort",
#     "Some apples unexpectedly fell from the old tree",
#     "No excuses were accepted for sudden tardiness",
#     "Wholehearted dedication always leads to success",
#     "Half of the pizza was unexpectedly left untouched",
#     "Double the effort often results in a breakthrough",
#     "The carnival was triple the fun",
#     "Excitement quadrupled with four attractions",
#     "Multiple options were thoughtfully available for selection",
#     "Significant contributions were made by single individuals",
#     "Team success depended on how individual strengths complemented each other",
#     "A successful outcome resulted from collective efforts",
#     "Total commitment is always required for excellence",
#     "Insufficient partial completion of the task is not acceptable",
#     "Necessary transparency requires full disclosure",
#     "The audience was disappointed as empty promises were made",
#     "Whole families gathered for the festive occasion",
#     "The road was lined with countless trees",
#     "Sizable portions of food were served at the banquet",
#     "Many birds nested in the tall trees",
#     "The beach was scattered with tiny seashells",
#     "Some days are busier than others",
#     "Limited resources hindered the research project",
#     "The room was filled with numerous colorful balloons",
#     "Adequate time was given for preparation",
#     "Gigantic waves crashed against the cliffs",
#     "Unequal opportunities led to disparities in society",
#     "Several options were considered before making a decision",
#     "Countless hours were spent on the intricate design",
#     "A minimal investment resulted in maximum profit",
#     "Large crowds gathered for the grand opening",
#     "The vast desert landscape stretched for miles",
#     "Ample supplies were stored in the warehouse",
#     "Every member of the team played a crucial role",
#     "The old tree provided shade for many",
#     "Scarce information was available about the mysterious creature",
#     "The entire village participated in the annual festival",
#     "Individual efforts contributed to the overall success",
#     "Multiple challenges were overcome through teamwork",
#     "Empty promises left the audience disappointed",
#     "No compromises were made on the quality of the product",
#     "Many books lined the shelves of the library",
#     "Few clouds appeared in the clear blue sky",
#     "Several students excelled in their exams",
#     "Opportunities for growth are numerous in this field",
#     "Countless stars twinkled in the night",
#     "Abundant resources were available for the research",
#     "Sufficient time was allocated for the presentation",
#     "Limited spaces were left for the upcoming event",
#     "Infinite possibilities awaited exploration",
#     "Ample opportunities for learning were provided",
#     "Excessive heat made the afternoon uncomfortable",
#     "Sparse vegetation covered the vast landscape",
#     "Adequate provisions were made for the journey",
#     "Scarce information about the topic hindered progress",
#     "Plentiful rainfall contributed to a bountiful harvest",
#     "Substantial evidence supported the theory",
#     "Minimal effort led to a maximum impact",
#     "The maximum speed limit on the highway was 70 mph",
#     "Minimum requirements for the project were outlined",
#     "Average temperatures for the month were recorded",
#     "Equal chances were given to all participants",
#     "Unequal distribution of resources led to disparities",
#     "Sizable investments were made in the startup",
#     "Tiny details made a significant difference",
#     "Huge mountains dominated the landscape",
#     "Gigantic waves crashed against the cliffs",
#     "Small details often matter the most",
#     "Large crowds gathered for the grand event",
#     "Vast oceans stretched beyond the horizon",
#     "Limited tickets were available for the concert",
#     "Unlimited potential lies within each individual",
#     "All employees actively participated in the workshop",
#     "None of the questions remained unanswered",
#     "Every moment holds a unique opportunity",
#     "Each member contributed to the success of the project",
#     "Some days are more challenging than others",
#     "No excuses were tolerated for incomplete tasks",
#     "Wholehearted dedication is key to achieving goals",
#     "Half of the cookies were quickly devoured",
#     "Double the effort was required to meet the deadline",
#     "The carnival was triple the excitement of previous years",
#     "Excitement quadrupled with the unexpected surprise",
#     "Multiple solutions were proposed for the problem",
#     "Significant achievements were made by individual efforts",
#     "Team success depended on the collaboration of all members",
#     "A successful outcome resulted from the collective expertise",
#     "Total commitment is necessary for project excellence",
#     "Insufficient preparation can lead to poor performance",
#     "Necessary precautions require full attention",
#     "The audience was delighted as promises were fulfilled",
#     "Whole families gathered for the festive celebration",
#     "The road was lined with countless flowers",
#     "Sizable portions of cake were served at the party",
#     "Many birds nested in the tall trees",
#     "The beach was scattered with tiny seashells",
#     "Some days are busier than others",
#     "Limited resources challenged the research team",
#     "The room was filled with numerous awards",
#     "Adequate time was given for thorough examination",
#     "Gigantic waves crashed against the cliffs",
#     "Unequal opportunities must be addressed for a fair society",
#     "Several options were presented for consideration",
#     "Countless hours of hard work led to success",
#     "A minimal investment in education yields maximum knowledge",
#     "Large crowds gathered for the grand opening ceremony",
#     "The vast desert landscape stretched for miles",
#     "Ample supplies were stocked for the winter season",
#     "Every member of the team played a crucial role",
#     "The old tree provided shade for many generations",
#     "Scarce information about the rare species led to curiosity",
#     "The entire village participated in the annual tradition",
#     "Individual efforts contributed to the overall success",
#     "Multiple challenges were overcome through collaborative efforts",
#     "Empty promises disappoint and lead to mistrust",
#     "No compromises should be made on the quality of service"
# ]
# print(len(phrases))
# quantitative_adjectives = ["Many", "Few", "Several", "Numerous", "Countless", "Abundant", "Sufficient", "Limited", "Infinite",
#                            "Ample", "Excessive", "Sparse", "Adequate", "Scarce", "Plentiful", "Substantial", "Minimal", "Maximum",
#                            "Minimum", "Average", "Equal", "Unequal", "Sizable", "Tiny", "Huge", "Gigantic", "Small", "Large", "Vast",
#                            "Limited", "Unlimited", "All", "None", "Every", "Each", "Some", "No", "Whole", "Half", "Double", "Triple", "Quadruple", "Multiple", "Single", "Individual", "Collective", "Total", "Partial", "Full", "Empty"]

# #Returns a dictionary containing the heads and modified dependencies
# def process_sentence(sentence, quantitative_adjectives):
#     doc = nlp(sentence)
#     heads = [token.head.i for token in doc]
#     deps = [token.dep_ for token in doc]
    
#     quantity_indices = []
    
#     for i, token in enumerate(doc):
#         if token.text.lower() in [adj.lower() for adj in quantitative_adjectives]:
#             quantity_indices.append(i)
    
#     for i in quantity_indices:
#         deps[i] = 'QUANTITY'

    
#     result = {
#         'heads': heads,
#         'deps': deps
#     }
    
#     return result

# def create_train_data(sentences, quantitative_adjectives):
#     TRAIN_DATA = []
    
#     for sentence in sentences:
#         processed_data = process_sentence(sentence, quantitative_adjectives)
        
#         # Check if 'QUANTITY' is in the dependencies
#         if 'QUANTITY' in processed_data['deps']:
#             TRAIN_DATA.append((sentence, processed_data))
    
#     return TRAIN_DATA

# TRAIN_DATA2 = create_train_data(phrases, quantitative_adjectives)


# # Initialize a blank 'en' model
# nlp = spacy.blank('en')
# print("Created blank 'en' model")
# print(nlp.pipe_names)
# # if 'parser' in nlp.pipe_names:
# #     nlp.remove_pipe('parser')


# parser=nlp.add_pipe('parser')
# j=0
# # Add labels to the parser
# unique_labels = set()
# for text, annotations in TRAIN_DATA2:
#     for dep in annotations.get('deps', []):
#         unique_labels.add(dep)

# for label in unique_labels:
#     print(label)
#     parser.add_label(label)


# print(nlp.pipe_names)

# other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'parser']
# with nlp.disable_pipes(*other_pipes):
#     optimizer = nlp.begin_training()
#     for itn in tqdm(range(20), 'TRAINING'):
#         random.shuffle(TRAIN_DATA2)
#         losses = {}

#         for text, annotations in TRAIN_DATA2:
#             example = Example.from_dict(nlp.make_doc(text), annotations)
#             nlp.update([example], sgd=optimizer, losses=losses) #we can use batch to optimize the processus size=10 mean each 




# nlp.to_disk("./model/updated_parser_essay4")

# Load the model from the saved directory
nlp2 = spacy.load("./model/updated_parser_essay4")
test_phrases = [
    "The marathon had small participants",
    "Few people attended the conference",
    "Several options were considered before making a decision",
    "the night sky illuminated  numerous stars",
    "you have many cars"
    ]
docs=nlp2.pipe(test_phrases)
for doc in docs:
  print(doc.text)
  print([(t.text, t.dep_, t.head.text) for t in doc
    if t.dep_ != '-'])
