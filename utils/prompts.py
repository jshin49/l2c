from collections import OrderedDict
from typing import Dict

import torch

PROMPTS_TYPE = Dict[str, str]
ENCODED_PROMPTS_TYPE = Dict[str, Dict[str, Dict[str, torch.Tensor]]]
PROMPTS: PROMPTS_TYPE = OrderedDict([
    # XLS
    ("summarization", "summarize: "),
    ("translation-doc-fr-en", "translate French to English: "),
    ("translation-doc-en-fr", "translate English to French: "),
    ("XLS-fr-en", "summarize and translate French to English: "),
    ("XLS-en-fr", "summarize and translate English to French: "),
    ("translation-doc-de-en", "translate German to English: "),
    ("translation-doc-en-de", "translate English to German: "),
    ("XLS-de-en", "summarize and translate German to English: "),
    ("XLS-en-de", "summarize and translate English to German: "),
    ("translation-doc-en-zh", "Translate English to Chinese: "),
    ("translation-sum-en-zh", "Translate English to Chinese: "),
    ("XLS-en-zh", "Summarize and translate English to Chinese: "),
    ("translation-doc-ru-en", "Translate Russian to English: "),
    ("translation-sum-ru-en", "Translate Russian to English: "),
    ("XLS-ru-en", "Summarize and translate Russian to English: "),
    ("translation-doc-vi-en", "Translate Vietnamese to English: "),
    ("translation-sum-vi-en", "Translate Vietnamese to English: "),
    ("XLS-vi-en", "Summarize and translate Vietnamese to English: "),
    ("translation-doc-es-en", "Translate Spanish to English: "),
    ("translation-sum-es-en", "Translate Spanish to English: "),
    ("XLS-es-en", "Summarize and translate Spanish to English: "),
    ("translation-doc-tr-en", "Translate Turkish to English: "),
    ("translation-sum-tr-en", "Translate Turkish to English: "),
    ("XLS-tr-en", "Summarize and translate Turkish to English: "),
    # XNLI
    ("NLI", "English nli: "),
    ("ar_en+NLI", "Arabic nli: "),
    ("bg_en+NLI", "Bulgarian nli: "),
    ("de_en+NLI", "German nli: "),
    ("el_en+NLI", "Greek nli: "),
    ("es_en+NLI", "Spanish nli: "),
    ("fr_en+NLI", "French nli: "),
    ("hi_en+NLI", "Hindi nli: "),
    ("ru_en+NLI", "Russian nli: "),
    ("sw_en+NLI", "Swahili nli: "),
    ("th_en+NLI", "Thai nli: "),
    ("tr_en+NLI", "Turkish nli: "),
    ("ur_en+NLI", "Urdu nli: "),
    ("vi_en+NLI", "Vietnamese nli: "),
    ("zh_en+NLI", "Chinese nli: "),
    ("ar_en", "Arabic to English: "),
    ("bg_en", "Bulgarian to English: "),
    ("de_en", "German to English: "),
    ("el_en", "Greek to English: "),
    ("es_en", "Spanish to English: "),
    ("fr_en", "French to English: "),
    ("hi_en", "Hindi to English: "),
    ("ru_en", "Russian to English: "),
    ("sw_en", "Swahili to English: "),
    ("th_en", "Thai to English: "),
    ("tr_en", "Turkish to English: "),
    ("ur_en", "Urdu to English: "),
    ("vi_en", "Vietnamese to English: "),
    ("zh_en", "Chinese to English: "),
    # StylePTB natural version of prompts
    # ("PPR", "without prepositions: "),
    # ("PTA", "to active voice: "),
    # ("ATP", "to passive voice: "),
    # ("TFU", "to future tense: "),
    # ("TPR", "to present tense: "),
    # ("TPA", "to past tense: "),
    # ("ARR", "without adjectives or adverbs: ")
    # ("PBF", "move prepositions to front: ")
    # ("PFB", "move prepositions to back: ")
    # ("PPR+ATP", "to passive voice without prepositions: "),
    # ("PPR+PTA", "to active voice without prepositions: "),
    # ("TFU+ATP", "to future tense and passive voice: "),
    # ("TFU+PTA", "to future tense and active voice: "),
    # ("TPR+ATP", "to present tense and passive voice: "),
    # ("TPR+PTA", "to present tense and active voice: "),
    # ("TPA+ATP", "to past tense and passive voice: "),
    # ("TPA+PTA", "to past tense and active voice: "),
    # ("TFU+PPR", "to future tense without prepositions: "),
    # ("TPR+PPR", "to present tense without prepositions: "),
    # ("TPA+PPR", "to past tense without prepositions: "),
    # ("ARR+PFB", "move prepositions to back without adjectives or adverbs: "),
    # ("ARR+PBF", "move prepositions to front without adjectives or adverbs: "),
    # ("TFU+ARR", "to future tense without adjectives or adverbs: "),
    # ("TPA+ARR", "to past tense without adjectives or adverbs: "),
    # ("TPR+ARR", "to present tense without adjectives or adverbs: "),
    # ("TFU+PBF", "to future tense and move prepositions to front: "),
    # ("TFU+PFB", "to future tense and move prepositions to back: "),
    # ("TPA+PFB", "to past tense and move prepositions to back: "),
    # ("TPA+PBF", "to past tense and move prepositions to front: "),
    # ("TPR+PBF", "to present tense and move prepositions to front: "),
    # ("TPR+PFB", "to present tense and move prepositions to back: "),
    # stylePTB artificial prompts
    ("PPR", "PPR: "),
    ("PTA", "PTA: "),
    ("ATP", "ATP: "),
    ("TFU", "TFU: "),
    ("TPR", "TPR: "),
    ("TPA", "TPA: "),
    ("ARR", "ARR: "),
    ("PBF", "PBF: "),
    ("PFB", "PFB: "),
    ("PPR+ATP", "PPR + ATP: "),
    ("PPR+PTA", "PPR + PTA: "),
    ("TFU+ATP", "TFU + ATP: "),
    ("TFU+PTA", "TFU + PTA: "),
    ("TPR+ATP", "TPR + ATP: "),
    ("TPR+PTA", "TPR + PTA: "),
    ("TPA+ATP", "TPA + ATP: "),
    ("TPA+PTA", "TPA + PTA: "),
    ("TFU+PPR", "TFU + PPR: "),
    ("TPR+PPR", "TPR + PPR: "),
    ("TPA+PPR", "TPA + PPR: "),
    ("ARR+PFB", "ARR + PFB: "),
    ("ARR+PBF", "ARR + PBF: "),
    ("TFU+ARR", "TFU + ARR: "),
    ("TPA+ARR", "TPA + ARR: "),
    ("TPR+ARR", "TPR + ARR: "),
    ("TFU+PBF", "TFU + PBF: "),
    ("TFU+PFB", "TFU + PFB: "),
    ("TPA+PFB", "TPA + PFB: "),
    ("TPA+PBF", "TPA + PBF: "),
    ("TPR+PBF", "TPR + PBF: "),
    ("TPR+PFB", "TPR + PFB: "),
])
