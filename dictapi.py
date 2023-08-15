import requests


class DictionaryAPI:
    
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

    def get_response(self, word):
        url = self.url + word
        response = requests.get(url).json()
        return response

    def get_definition(self,response):
        return response[0]['meanings'][1]['definitions'][0].get('definition',[])

    def get_synonyms(self, response):
        return response[0]['meanings'][0].get('synonyms', [])
    
    def get_pos(self,response):
        return response[0]['meanings'][0].get('partOfSpeech', [])
    
    def get_antonym(self,response):
        return response[0]['meanings'][0].get('antonyms', [])

    def get_phonetic(self,response):
        return response[0]['phonetics'][0].get('text', [])

    def get_audio(self,response):
        return response[0]['phonetics'][0].get('audio', [])

    def get_example(self,response):
        return response[0]['meanings'][1]['definitions'][0].get('example',[])
