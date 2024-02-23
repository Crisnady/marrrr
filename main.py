meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "tanggapan terhadap lelucon",
            "SHEESH": "sedikit ketidaksetujuan",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "AGGRO": "untuk menjadi agresif/marah",
            }
            
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    if word == "LOL":
        print(meme_dict["LOL"])
    elif word == "CRINGE":
        print(meme_dict["CRINGE"])
    elif word == "ROFL":
        print(meme_dict["ROFL"])
    elif word == "SHEESH":
        print(meme_dict["SHEESH"])
    elif word == "CREEPY":
        print(meme_dict["CREEPY"])
    elif word == "AGGRO":
        print(meme_dict["AGGRO"])
else:
    print("maaf jawaban tidak ditemukan")
    
