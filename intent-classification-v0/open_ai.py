import preprocessing as pp
import openai

def data_extractor(text):
    # cleaning text
    clean_text = pp.clean_hash_ment(text)

    # openai connection
    openai.api_key = "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"
    prompt = "cümlesindeki tam adres, adresteki il, adresteki ilçe, kişi, telefon, durum bilgilerini düzenli bir formatta ve Türkçe dilinde yeniden yaz. eğer bir bilgi belirtilmemişse 'belirtilmemiş' yaz. hashtag'leri ve mention'ları dikkate alma. eğer bir şehrin veya ilçenin kısaltması yazılmışsa tam haline çevir. eğer 'https://t.co' ile başlayan bir link varsa o konum linkidir. onu da konum linki olarak belirt.  yazdığım cümleyi yeniden yazmanı istemiyorum."
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"'{clean_text}' " + prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )



    return response["choices"][0]["text"]