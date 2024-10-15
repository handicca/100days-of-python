Berikut adalah tipe data dalam Python:

### 1. **Tipe Data Numerik**
   - **Integer (`int`)**: Bilangan bulat, baik positif maupun negatif, tanpa desimal.
     - Contoh: `10`, `-5`
   - **Float (`float`)**: Bilangan desimal (floating point).
     - Contoh: `3.14`, `-0.5`
   - **Complex (`complex`)**: Bilangan kompleks dengan bagian nyata dan imajiner.
     - Contoh: `3 + 4j`, `2 - 1j`

### 2. **Tipe Data Boolean (`bool`)**
   - Tipe data yang hanya memiliki dua nilai: `True` atau `False`.
     - Contoh: `is_valid = True`

### 3. **Tipe Data Teks**
   - **String (`str`)**: Urutan karakter yang diapit tanda kutip tunggal (`'`) atau ganda (`"`).
     - Contoh: `"Hello, World!"`, `'Python'`

### 4. **Tipe Data Urutan (Sequence)**
   - **List (`list`)**: Koleksi item yang terurut dan bisa diubah (mutable), diapit oleh tanda kurung siku `[]`.
     - Contoh: `[1, 2, 3, 'apple']`
   - **Tuple (`tuple`)**: Mirip dengan list, tetapi tidak bisa diubah (immutable), diapit oleh tanda kurung biasa `()`.
     - Contoh: `(1, 2, 3, 'banana')`
   - **Range (`range`)**: Digunakan untuk merepresentasikan urutan angka, umumnya dalam loop.
     - Contoh: `range(0, 10)`

### 5. **Tipe Data Set**
   - **Set (`set`)**: Koleksi item yang tidak terurut, unik, dan bisa diubah (mutable), diapit oleh tanda kurung kurawal `{}`.
     - Contoh: `{1, 2, 3, 'orange'}`
   - **Frozen Set (`frozenset`)**: Mirip dengan set, tetapi tidak bisa diubah (immutable).
     - Contoh: `frozenset([1, 2, 3])`

### 6. **Tipe Data Mapping**
   - **Dictionary (`dict`)**: Koleksi pasangan kunci-nilai yang tidak terurut, diapit oleh tanda kurung kurawal `{}`, dengan format `key: value`.
     - Contoh: `{'name': 'Alice', 'age': 25}`

### 7. **Tipe Data None (`NoneType`)**
   - **None**: Tipe data khusus yang merepresentasikan ketiadaan nilai.
     - Contoh: `x = None`

Tipe data ini memungkinkan Python untuk bekerja dengan berbagai jenis nilai dengan cara yang efisien dan fleksibel.