from .utils.maps import B2A_MAP, A2B_MAP
from .utils.utils import normalizer

class AvroConverter:
    def __init__(self):
        self.bengali_trie = B2A_MAP
        self.banglish_trie = A2B_MAP
        self.normalizer = normalizer()

    def bengali_to_avro(self, bengali_text):
        bengali_text = self.normalizer.normalize_bengali_text(bengali_text) + " "
        
        result = []
        i = 0
        text_len = len(bengali_text)
        
        while i < text_len:
            current = self.bengali_trie
            longest_match = None
            match_length = 0
            
            for j in range(i, text_len):
                char = bengali_text[j]
                if char in current:
                    current = current[char]
                    if 'end' in current:
                        longest_match = current['end']
                        match_length = j - i + 1
                else:
                    break
            
            if longest_match:
                
                result.append(longest_match)
                i += match_length
            else:
                
                result.append(bengali_text[i])
                i += 1
        return self.normalizer.normalize_english_text(''.join(result)).strip()

    def avro_to_bengali(self, avro_text):
        avro_text = self.normalizer.normalize_english_text(avro_text) + " "
        result = []
        i = 0
        text_len = len(avro_text)
        
        while i < text_len:
            current = self.banglish_trie
            longest_match = None
            match_length = 0
            
            for j in range(i, text_len):
                char = avro_text[j]
                if char in current:
                    current = current[char]
                    if 'end' in current:
                        longest_match = current['end']
                        match_length = j - i + 1
                else:
                    break
            
            if longest_match:
                result.append(longest_match)
                i += match_length
            else:
                result.append(avro_text[i])
                i += 1
                
        return self.normalizer.normalize_bengali_text(''.join(result), unicode_normalize=False).strip()

