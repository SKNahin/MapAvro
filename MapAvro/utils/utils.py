from bnunicodenormalizer import Normalizer 


class normalizer:
    def __init__(self):
        self.bnorm=Normalizer()
        self.allowed_bengali_chars = ['ঢ', 'ঋ', '্', 'য', 'া', 'ঞ', 'ঙ', 'ঢ়', 'ষ', 'ঠ', 'ছ', 'ধ', 'ঘ', 'ঝ', 'খ', 'থ', 'ঐ', 'ঔ', 'র', 'ও', 'ঈ', 'ঊ', 'ব', 'ড', 'ণ', 'ড়', 'শ', 'ট', 'চ', 'দ', 'ফ', 'গ', 'হ', 'জ', 'ক', 'ল', 'ম', 'ন', 'প', 'স', 'ত', 'ভ', 'য়', 'ৃ', 'ো', 'ই', 'উ', 'এ', 'অ', 'ৈ', 'ৌ', 'আ', ' ', 'ী', 'ূ', 'ে', 'ি', 'ু', 'ৎ', 'ং', '!', ',', '।', '?', 'ঃ', 'ঁ']
        self.allowed_english_chars = ['D', 'h', 'o', 'r', 'i', "'", 'z', 'a', 'N', 'G', 'g', 'R', 'H', 'S', 'T', 'c', 'd', 'j', 'k', 't', 'O', 'I', 'U', 'y', 'w', 'b', 'f', 'l', 'm', 'n', 'p', 's', 'v', 'u', 'e', ' ', '!', ',', '.', '?', 'X', 'x']

    def normalize_bengali_text(self,text,unicode_normalize=True):
        if unicode_normalize:
            text=" ".join([self.bnorm(t)['normalized'] for t in text.split(" ")])
            text = text.replace("-", " ").replace('—'," ").replace("য"+'়',"য়").replace("ড"+'়',"ড়").replace('ঢ' + '়',"ঢ়")
        text = self.filter_bengali_chars(text,self.allowed_bengali_chars)
        return text
    
    def normalize_english_text(self,text):
        text = text.replace("-", " ").replace('—'," ")
        text = self.filter_bengali_chars(text,self.allowed_english_chars)
        return text
    
    def filter_bengali_chars(self,text,allowed_bengali_chars):
        allowed_chars_set = set(allowed_bengali_chars)
        trans_table = {ord(char): None for char in ''.join(chr(i) for i in range(0x110000) if chr(i) not in allowed_chars_set)}
        filtered_text = text.translate(trans_table)
        return filtered_text




