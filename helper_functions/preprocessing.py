import re
import emoji




arabic_punctuations = '''`÷×؛<>()*&^%][،/:"؟.,'{}~¦+|!”…“–•۱۲۳٤٥٦٧۸۹٠'''
translator = str.maketrans('', '', arabic_punctuations)


def give_emoji_free_text(text):
    return emoji.get_emoji_regexp().sub(r'', text)

def normalizeArabic(text):
    text = text.strip()
    text = re.sub("[إأٱآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "ء", text)
    text = re.sub("ئ", "ء", text)
    text = re.sub("ة", "ه", text)
    text = re.sub("گ", "ك", text)
    text = ''.join(ch for ch in text)
    return text
    
    
def pre_processing(text):

    # removing longitaion
    text = re.sub(r'(.)\1+', r"\1\1", text)
    # remove hashtags
    text = re.sub(r'#', '', text)
    # removing user name
    text = re.sub('@[^\s]+', ' ', text)  
    #Convert www.* or https?://* to " "
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))',' ',text)
    
    # removing \n because I found it in some tweets while insepecting the data
    text = re.sub(r"\n"," ",text)
    # removing english characters
    text = re.sub(r'[A-Za-z0-9]', '', text)
    # removing puntication at last because of # and @
    text = text.translate(translator)
    # this one to remove underscore from text because it was affecting hashtags when it was in puntications
    text = re.sub(r'_',' ',text)
    # removing emoji and tashikel
    #text = emoji_pattern.sub(r'', text)
    text = give_emoji_free_text(text)
    noise = re.compile(""" ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ     # Sukun
                         """, re.VERBOSE)
    text = re.sub(noise, '', text)

    # normalizing text
    text = normalizeArabic(text)
    
    # removing space more than 1
    text = re.sub(r'\s{2,}', ' ', text)
    
    return text
