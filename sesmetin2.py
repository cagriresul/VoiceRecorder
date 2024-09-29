import speech_recognition as sr
import pyttsx3

# Tanıyıcıyı başlat
r = sr.Recognizer()


# Metni konuşmaya çeviren fonksiyon
def Konus(metin):
    # Motoru başlat
    engine = pyttsx3.init()
    engine.say(metin)
    engine.runAndWait()


# Kullanıcının konuşmasını sürekli dinlemek için döngü
while True:
    try:
        # Mikrofondan girdi kaynağı olarak kullan
        with sr.Microphone() as source2:
            # Ortamdaki gürültüye göre enerjiyi ayarla
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # Kullanıcının söylediklerini dinle
            audio2 = r.listen(source2)

            # Google'ı kullanarak sesi tanı
            Metin = r.recognize_google(audio2, language="tr-TR")
            Metin = Metin.lower()

            print(f"Söylediniz: {Metin}")
            Konus(Metin)

    except sr.RequestError as e:
        print(f"Sonuçlar alınamadı; {e}")

    except sr.UnknownValueError:
        print("Anlaşılamayan bir hata oluştu")
