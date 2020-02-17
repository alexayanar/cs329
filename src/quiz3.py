# ========================================================================
# Copyright 2020 Emory University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========================================================================
import nltk
from typing import Set, Optional, List
from nltk.corpus.reader import Synset
from nltk.corpus import wordnet as wn
nltk.download('wordnet')

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def antonyms(word: str, pos: Optional[str] = None) -> Set[str]:
    ants = set()
    syn = set()
    for synset in wn.synsets(word, pos):
        for lemma in synset.lemmas():
            syn.add(lemma.name())
            if lemma.antonyms():
                ants.add(lemma.antonyms()[0].name)
    return ants


def lch_paths(word_0: str, word_1: str) -> List[List[Synset]]:
    dogs = wn.synsets('dog', pos='n')
    synset_0 = dogs[0]
    cats = wn.synsets('cat', pos='n')
    synset_1 = cats[0]
    # synset_0 = wn.synset(word_0) error needed 3 values to unpack
    # when amended, given error need 2 values and 3 were given
    # synset_0 = syn0[0]
    # synset_1 = wn.synset(word_1)
    # synset_1 = syn1[0]

    hypernym_paths_0 = synset_0.hypernym_paths()
    lch = synset_0.lowest_common_hypernyms(synset_1)
    paths = []

    for hypernym in lch:
        paths.extend(hypernym.hypernym_paths())
        for syn_list in hypernym_paths_0:
            i = next((i for i, syn in enumerate(syn_list) if syn == hypernym), -1)
            if i >= 0: paths.append(syn_list[:i + 1])
    return paths


if __name__ == '__main__':
    print(antonyms('buy', pos='v'))
for path in lch_paths('dog', 'cat'):
    print(path)

print()
