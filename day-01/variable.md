Aturan penamaan variabel dalam Python mengikuti pedoman tertentu agar kode lebih mudah dibaca dan dipahami. Berikut adalah beberapa aturan dan praktik terbaik dalam menamai variabel di Python:

### Aturan Dasar:
1. **Karakter Awal:** Nama variabel harus dimulai dengan huruf (A-Z, a-z) atau garis bawah (_), tetapi **tidak boleh** dimulai dengan angka.
   - Contoh benar: `nama`, `_angka`
   - Contoh salah: `1nilai`, `2buah`

2. **Karakter Lainnya:** Setelah karakter pertama, variabel dapat berisi huruf, angka, atau garis bawah (_).
   - Contoh: `nilai_1`, `nama_mahasiswa`

3. **Peka Huruf Besar-Kecil:** Python **membedakan** huruf besar dan kecil, sehingga `Nilai` dan `nilai` adalah dua variabel yang berbeda.
   - Contoh: `nilai`, `Nilai` (berbeda)

4. **Tidak Menggunakan Kata Kunci Python:** Nama variabel **tidak boleh** sama dengan kata kunci yang sudah digunakan dalam Python (seperti `if`, `else`, `for`, dll.).
   - Untuk mengecek kata kunci yang ada di Python, bisa menggunakan:
     ```python
     import keyword
     print(keyword.kwlist)
     ```

5. **Spasi Tidak Diperbolehkan:** Spasi tidak diperbolehkan dalam nama variabel. Gunakan garis bawah (_) sebagai pengganti spasi.
   - Contoh benar: `nama_mahasiswa`
   - Contoh salah: `nama mahasiswa`

### Praktik Terbaik:
1. **Gunakan Nama yang Deskriptif:** Beri nama variabel yang sesuai dengan fungsinya agar kode lebih mudah dipahami.
   - Contoh: `jumlah_siswa`, `total_harga`

2. **Snake Case:** Konvensi penamaan variabel pada Python umumnya menggunakan **snake_case** (kata-kata dipisahkan dengan garis bawah).
   - Contoh: `total_biaya`, `panjang_benda`

3. **Jangan Gunakan Nama Variabel Terlalu Pendek:** Hindari menamai variabel dengan satu huruf kecuali untuk variabel sementara dalam loop atau pemakaian yang sangat lokal.
   - Contoh: `i`, `j` (umum digunakan dalam loop), tetapi hindari untuk kasus-kasus lainnya.

4. **Gunakan Huruf Besar untuk Konstanta:** Biasanya, variabel yang nilainya tetap atau tidak berubah sepanjang program menggunakan huruf besar semua.
   - Contoh: `PI = 3.14`, `MAX_LIMIT = 100`

Dengan mengikuti aturan dan praktik ini, penamaan variabel akan lebih terstruktur dan mudah dipahami oleh tim pengembang lainnya atau diri sendiri di masa depan.