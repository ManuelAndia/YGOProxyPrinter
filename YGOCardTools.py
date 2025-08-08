# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 17:18:25 2025

@author: Eukerion
"""

import requests, re, itertools, json
import numpy as np
from PIL import Image

#from fpdf import FPDF
# pdf = FPDF()
# # imagelist is the list with all image filenames
# for image in imagelist:
#     pdf.add_page()
#     pdf.image(image,x,y,w,h)
# pdf.output("yourfile.pdf", "F")

pattern = r"\d+"

#%% Functions
def language_request(language="en"):
    assert(language.lower() in ["en", "fr", "de", "it", "pt"])
    return "" if language.lower()=="en" else f"&language={language.lower()}"

#%% Classes
class Card(object):
    def __init__(self, d):
        for k,v in d.items():
            super().__setattr__(k, v)
    
    def get_Number(self):
        Number = re.search(pattern, self.Name)
        if Number is None:
            self.Number = -1
        else:
            _Number = int(Number.group())
            self.Number = _Number
    
    def get_image_URL(self, n="all", size="small"):
        if size=="small":
            key = "image_url_small" 
        elif size=="large":
            key = "image_url"
        else:
            raise NotImplementedError(f"Size '{size}' is not allowed ('small' or 'large').")
        
        if n=="all": # return a list of all the images URLs for all the card's artworks
            return [_img[key] for _img in self.Card_images]
        elif isinstance(n, int): # return only the desired artwork image
            return self.Card_images[n][key]
        else:
            raise TypeError(f"Value of `n` must be int, not {type(n)}.")
    
    def get_image_raw(self, n="all", size="small"):
        url = self.get_image_URL(n=n, size=size)
        if n=="all":
            return [requests.get(_url).content for _url in url]
        else:
            return requests.get(url).content
    
    def get_image(self, n="all", size="small"):
        url = self.get_image_URL(n=n, size=size)
        if n=="all":
            return [Image.open(requests.get(_url, stream=True).raw) for _url in url]
        else:
            return Image.open(requests.get(url, stream=True).raw)
    
    def __repr__(self):
        return self.Name
    
    def __str__(self):
        return "A card named {}.".format(self.Name)

class CardList(list):
    def __init__(self, card_list, verbose=False):
        self.verbose = verbose
        super().__init__(card_list)
    
    def get_cards_from_names(self, name_list):
        return self[sum([self.Name==elm for elm in name_list]).astype(bool)] # filter by name
    
    def __getattr__(self, name):
        if all(hasattr(elm, name) for elm in self):
            return np.array([elm.__getattribute__(name) for elm in self])
        else:
            super().__getattribute__(name)
    
    def __getitem__(self, N):
        if type(N)==np.ndarray:
            return self.__class__(np.array(self)[N])
        else:
            return super().__getitem__(N)
    
    def __str__(self):
        return "A list of {} cards.".format(len(self))
    
    def __add__(self, other):
        return self.__class__(self.card_list + other.card_list, verbose=self.verbose)

class NumberXyzCardList(CardList):
    def __init__(self, card_list, verbose=False):
        self.verbose = verbose
        super().__init__(card_list, verbose=verbose)
    
    def get_combinations(self, Number, Ncombinations=4):
        res = []
        Numbers = self.Number # all Numbers in card list
        ind = (Numbers < Number) # keep only Numbers stricly lower than Number
        new_card_list = self[ind] # card list with only the relevant Numbers
        all_combinations = list(itertools.combinations([elm.__dict__ for elm in new_card_list], Ncombinations)) # trick to make itertools faster (had to get rid of the classes defined here for a few lines...)
        Ncomb = len(all_combinations)
        if self.verbose: print("Found {} combinations.".format(Ncomb))
        for i, combination in enumerate(all_combinations):
            #if self.verbose: print("{}/{}".format(i, Ncomb))
            if sum([card["Number"] for card in combination])==Number: # check if the sum of all "Number" attributes of the combination match the desired "Number"
                if len(set([card["Level"] for card in combination]))==Ncombinations: # check if all Xyz ranks are different from each other
                    #res.append(combination)
                    res.append(self.__class__([Card(elm) for elm in combination])) # create new card list to add to results
        if self.verbose: print("Found {} combinations matching Number {}.".format(len(res), Number))
        # all_combinations = list(itertools.combinations(self, Ncombinations))
        # Ncomb = len(all_combinations)
        # for i, combination in enumerate(all_combinations):
        #     if self.verbose: print("{}/{}".format(i, Ncomb))
        #     _card_list = CardList(combination)
        #     if sum(_card_list.Number)==Number: # check if the sum of all "Number" attributes of the combination match the desired "Number"
        #         if len(set(_card_list.Level))==Ncombinations: # check if all Xyz ranks are different from each other
        #             res.append([1,2,3,4])
        return self.__class__(res)
    
    def get_combinations_with_specific_Numbers(self, Number, list_Numbers, Ncombinations=4):
        res = []
        N = len(list_Numbers)
        combinations = self.get_combinations(Number, Ncombinations=Ncombinations)
        for elm in combinations:
            if sum(n in elm.Number for n in list_Numbers)==min(N, Ncombinations): # the number of "Number"s found in the current card combination must be either equal to the length of the Numbers list, or
                                                                                  # to the length of the combination, whichever is smaller
                if elm not in res: res.append(self.__class__(list(elm)))
        return res
    
    def get_combinations_from_available_cards(self, Ncombinations=4):
        res = {}
        for card in self:
            _available_cards = self.copy()
            _available_cards.remove(card)
            _available_cards = self.__class__(_available_cards)
            res[card] = self.get_combinations_with_specific_Numbers(card.Number,
                                                                    _available_cards.Number,
                                                                    Ncombinations=Ncombinations)
            print("You can make {} with the following combinations: {}".format(card.Name, res[card]))
        return res

class CardListFromYGOProDeck(object):
    def __init__(self, API_request, verbose=False, card_list_type=CardList):
        self.verbose = verbose
        
        # Get answer for API request
        answer = requests.request("GET", API_request)
        
        # Turn results into dictionary
        # results = ast.literal_eval(answer.content.decode()) # old version
        results = json.loads(answer.content.decode())
        
        list_all_cards = results["data"]
        
        if verbose:
            # Print list of cards to check
            # for card in list_all_cards: print(card["name"])
            print("Fetched {} cards from YGOProDeck API.".format(len(list_all_cards)))
        
        card_list = []
        for card in list_all_cards:
            d = dict(zip(map(lambda x:x.capitalize(), card.keys()), card.values())) # create new dict with same keys (but capitalized 1st letter) and same values as each dict returned by YGOProDeck
            new_card = Card(d)
            card_list.append(new_card)
        
        self.card_list = card_list_type(card_list, verbose=verbose)

class NumberXyzCardListFromYGOProDeck(CardListFromYGOProDeck):
    def __init__(self, verbose=False):
        self.verbose = verbose
        
        # Get all "Number" XYZ Monsters
        API_request = r"https://db.ygoprodeck.com/api/v7/cardinfo.php?fname=Number&type=XYZ%20Monster"
        
        # Initialize card list
        super().__init__(API_request, verbose=verbose, card_list_type=NumberXyzCardList)
    
        # Check "Number" in card text
        for card in self.card_list:
            card.get_Number() # add "Number" attribute by analyzing all cards' names
        
            # Remove invalid "Number"s
            if card.Number<0: self.card_list.remove(card)

class NameMatchesFromYGOProDeck(CardListFromYGOProDeck):
    def __init__(self, card_name, language="en", **kwargs):
        _lang = language_request(language)
        
        # Get all matches for search
        API_request = r"https://db.ygoprodeck.com/api/v7/cardinfo.php?fname={card_name}{language}".format(card_name=card_name,
                                                                                                          language=_lang)
        
        super().__init__(API_request, **kwargs)

#%% Main script
if __name__=="__main__":
    l = NameMatchesFromYGOProDeck("tri-brigade")