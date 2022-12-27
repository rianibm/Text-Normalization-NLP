# importing libraries
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer
from natsort import natsorted
import string

def read_file(filename):
        with open(filename, 'r', encoding ="ascii", errors ="surrogateescape") as f:
                stuff = f.read()
                f.close()
                return stuff

def preprocessing(final_string):
        # Tokenize.
        tokenizer = TweetTokenizer()
        token_list = tokenizer.tokenize(final_string)

        # Hapus punctuations.
        table = str.maketrans('', '', '\t')
        token_list = [word.translate(table) for word in token_list]
        punctuations = (string.punctuation).replace("'", "")
        trans_table = str.maketrans('', '', punctuations)
        stripped_words = [word.translate(trans_table) for word in token_list]
        token_list = [str for str in stripped_words if str]

        # ubah ke lowercase
        token_list =[word.lower() for word in token_list]
        return token_list

# nama folder tempat dokumen.
folder_names = ["docs"]

# inisialisasi stemmer.
stemmer = PorterStemmer()
fileno = 0
pos_index = {}

# unutk mapping antara no file dengan namanya (fileno -> file name).
file_map = {}

for folder_name in folder_names:
        # Open files.
        file_names = natsorted(os.listdir(folder_name))

        for file_name in file_names:
                # Read isi file
                stuff = read_file(folder_name + "/" + file_name)

                # hapus punctuation, hapus stopword
                final_token_list = preprocessing(stuff)

                # pos -> posisi, term pada tokens.
                for pos, term in enumerate(final_token_list):
                        term = stemmer.stem(term)
                        # jika term sudah ada di dict
                        if term in pos_index:
                                # freq + 1
                                pos_index[term][0] = pos_index[term][0] + 1
                                # cek apakah term ada di DocID seblmnya.
                                if fileno in pos_index[term][1]:
                                        pos_index[term][1][fileno].append(pos)
                                else:
                                        pos_index[term][1][fileno] = [pos]
                        # Jika term tidak ada dalam pos_index posisi
                        # (first encounter).
                        else:
                                 pos_index[term] = []
                                 pos_index[term].append(1)
                                 # inisialisasi posting list
                                 pos_index[term].append({})
                                 # documen id
                                 pos_index[term][1][fileno] = [pos]
                # map no file ke nama file
                file_map[fileno] = folder_name + "/" + file_name

                # counter untuk nomor file
                fileno += 1

print("ID Dokumen: ")
for k,i in file_map.items():
    print(str(k)+" -> "+i)

print("Posting List: ")
print("Keterangan: misalnya 'malaria': [8, {0: [0, 10, 35, 58, 80, 88, 131], 1: [0]}]")
print("Artinya term 'malaria' muncul pada dokumen 1 pada indeks ke [0, 10, dst] dan pada dokumen 2 pada indeks ke 0, frequency-nya 8")
print("\n")
print(pos_index)

print("\n")
inp = input("Masukan term: ")
sample_pos_idx = pos_index[inp]

print("Pos index term " + inp +": " + str(sample_pos_idx))
print("Exist pada dukumen: ")
print("Dokumen -> posisi")
file_list = sample_pos_idx[1]
for fileno, positions in file_list.items():
    print(file_map[fileno]+ "-->" + str(positions))


