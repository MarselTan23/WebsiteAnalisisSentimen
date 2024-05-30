import nltk
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary

norm = {
    " dgn ": " dengan ",
    " gue ": " saya ",
    " bgmn ": " bagaimana ",
    " tdk ": " tidak ",
    " blum ": " belum ",
    " mantaaaaaaaappp ": " bagus ",
    " josss ": " bagus ",
    " thanks ": " terima kasih ",
    " fast ": " cepat ",
    " dg ": " dengan ",
    " trims ": " terima kasih ",
    " brg ": " barang ",
    " gx ": " tidak ",
    " recommended ": " rekomendasi ",
    " recomend ": " rekomendasi ",
    " good ": " bagus ",
    " cepet ": " cepat ",
    " bgt ": " sangat ",
    " banget ": " sangat ",
    " keren ": " bagus ",
    " baget ": " bagus ",
    " klo ": " kalau ",
    " ga ": " tidak ",
    " gak ": " tidak ",
    " g ": " tidak ",
    " bg ": " tidak ",
    " bgs ": " bagus ",
    " bgus ": " bagus ",
    " jd ": " jadi ",
    " yg ": " yang ",
    " d ": " di ",
    " dtg ": " datang ",
    " tr ": " terima ",
    " mhn ": " mohon ",
    " pgn ": " ingin ",
    " mo ": " mau ",
    " dpt ": " dapat ",
    " dapet ": " dapat ",
    " lg ": " lagi ",
    " jd ": " jadi ",
    " gpp ": " tidak apa-apa ",
    " bnyk ": " banyak ",
    " bs ": " bisa ",
    " bsa ": " bisa ",
    " skg ": " sekarang ",
    " nnti ": " nanti ",
    " sngt ": " sangat ",
    " bngt ": " banget ",
    " tp ": " tapi ",
    " keren ": " bagus ",
    " lama ": " lama ",
    " ramah ": " baik ",
    " keren ": " bagus ",
    " luar biasa ": " bagus ",
    " puas ": " senang ",
    " baik ": " bagus ",
    " oke ": " baik ",
    " ok ": " baik ",
    " bagussss ": " bagus ",
    " memuaskan ": " baik ",
    " puass ": " senang ",
    " rekomen ": " rekomendasi ",
    " recomended ": " rekomendasi ",
    " rekomen banget ": " rekomendasi ",
    " recommended banget ": " rekomendasi ",
    " recommended banget ": " rekomendasi ",
    " recomended banget ": " rekomendasi ",
    " bermanfaat ": " bagus ",
    " rekomended ": " rekomendasi ",
    " ok ": " baik ",
    " murah ": " bagus ",
    " recommended banget ": " rekomendasi ",
    " sangat membantu ": " bagus ",
    " joss ": " bagus ",
    " joss banget ": " bagus ",
    " mantap ": " bagus ",
    " mantap banget ": " bagus ",
    " terbaik ": " bagus ",
    " terbaik banget ": " bagus ",
    " sangat memuaskan ": " bagus ",
    " sangat bagus ": " bagus ",
    " sangat bagus banget ": " bagus "}

def normalisasi(str_text):
  for i in norm:
    str_text = str_text.replace(i, norm[i])
  return str_text

more_stop_words = []

stop_words = StopWordRemoverFactory().get_stop_words()
new_array = ArrayDictionary(stop_words)
stop_words_remover_new = StopWordRemover(new_array)

def stopword(str_text):
  str_text = stop_words_remover_new.remove(str_text)
  return str_text

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def stemming(komentar):
  factory = StemmerFactory()
  stemmer = factory.create_stemmer()
  do = []
  for w in komentar:
    dt = stemmer.stem(w)
    do.append(dt)
  d_clean = []
  d_clean = " ".join(do)
  print(d_clean)
  return d_clean