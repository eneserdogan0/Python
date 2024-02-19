class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        if not books:
            print("Henüz kitap eklemediniz lütfen kitap ekledikten sonra listelemeyi deneyin")
        else:
            print("Kitaplar:")
            for book in books:
                book_info = book.strip().split(',')
                print(f"Kitap Adı: {book_info[0]}, Yazar: {book_info[1]}, Yayın Tarihi: {book_info[2]}, Sayfa Sayısı: {book_info[3]}")

    def add_book(self):
        Baslik = input("Kitap Adı: ")
        Yazar = input("Yazar: ")

        while True:
            Yayin_Tarihi = input("Yayın Tarihi (YYYY MM DD)(yıl,ay ve günü boşluk koyarak yazınız) ")
            if len(Yayin_Tarihi.split()) == 3 and all(part.isdigit() for part in Yayin_Tarihi.split()):
                Yayin_Tarihi = '/'.join(Yayin_Tarihi.split())
                year = int(Yayin_Tarihi.split('/')[0])
                if not (1000 <= year <= 2025):
                    print("Geçersiz yıl Yıl 1000 ile 2025 arasında giriniz")
                    continue
                break
            else:
                print("Geçersiz tarih formatı Lütfen YIL AY GÜN formatında giriniz")

        while True:
            Sayfa_Sayisi = input("Sayfa Sayısı: ")
            if Sayfa_Sayisi.isdigit():
                break
            else:
                print("Sayfa sayısı sadece rakamlardan oluşmalıdır")

        book_info = f"{Baslik},{Yazar},{Yayin_Tarihi},{Sayfa_Sayisi}\n"
        self.file.write(book_info)
        print(f"{Baslik} isimli kitap eklendi")

    def remove_book(self):
        Baslik = input("Silmek istediğiniz kitabın adını giriniz: ")
        self.file.seek(0)
        books = self.file.readlines()
        found = False
        for book in books:
            if Baslik in book:
                books.remove(book)
                found = True
                break
        if found:
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(books)
            print(f"{Baslik} isimli kitap silindi")
        else:
            print(f"{Baslik} isimli kitap yoktur")

lib = Library()

while True:
    print("\n--- MENU ---")
    print("1) Kitapları Listelemek için (1)")
    print("2) Kitap Eklemek için (2)")
    print("3) Kitap Silmek için (3)")
    print("4) Çıkmak için (q) değerini giriniz")

    Secenek = input("Bir seçenek seçiniz: ")

    if Secenek == '1':
        lib.list_books()
    elif Secenek == '2':
        lib.add_book()
    elif Secenek == '3':
        lib.remove_book()
    elif Secenek.lower() == 'q':
        del lib
        print("Programdan çıkılıyor..")
        break
    else:
        print("Geçersiz seçenek lütfen geçerli bir seçenek giriniz")
