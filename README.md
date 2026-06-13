# TUGAS METODE NUMERIK BAB 11
## Penyelesaian Sistem Persamaan Linear dan Aplikasinya

---

# Gambaran Umum Bab

Bab 11 membahas berbagai metode numerik untuk menyelesaikan Sistem Persamaan Linear (SPL), baik secara langsung (direct methods) maupun iteratif (iterative methods).

Metode yang dipelajari meliputi:

- Eliminasi Gauss
- Invers Matriks
- LU Decomposition
- Cholesky Decomposition
- Thomas Algorithm
- Jacobi Iteration
- Gauss-Seidel Iteration
- Relaxation Method
- Condition Number
- Hilbert Matrix
- Vandermonde Matrix
- Finite Difference Method
- Pentadiagonal System Solver

---

# Soal 11.1
## Sistem Tridiagonal

### Konsep
Matriks tridiagonal adalah matriks yang hanya memiliki elemen nonnol pada:

- diagonal utama
- diagonal atas
- diagonal bawah

Bentuk umum:

| b₁ c₁ 0 0 |
| a₁ b₂ c₂ 0 |
| 0 a₂ b₃ c₃ |
| 0 0 a₃ b₄ |

### Tujuan
Menyelesaikan sistem linear tridiagonal secara efisien.

### Metode
- Thomas Algorithm
- Eliminasi Gauss khusus

---

# Soal 11.2
## Invers Matriks

### Konsep
Jika:

A x = b

maka:

x = A⁻¹ b

### Tujuan
Menentukan invers matriks dan memverifikasi hasilnya.

### Materi yang Dipelajari

- Invers Matriks
- Verifikasi A·A⁻¹ = I

---

# Soal 11.3
## Thomas Algorithm

### Konsep

Thomas Algorithm adalah bentuk khusus Eliminasi Gauss untuk matriks tridiagonal.

Kompleksitas:

O(n)

lebih cepat dibanding Eliminasi Gauss:

O(n³)

### Langkah

1. Forward Elimination
2. Back Substitution

---

# Soal 11.4
## Verifikasi Cholesky Decomposition

### Konsep

Jika matriks simetris positif definit:

A = LLᵀ

dengan:

L = matriks segitiga bawah

### Tujuan

Memverifikasi:

A = LLᵀ

---

# Soal 11.5
## Penyelesaian SPL dengan Cholesky

### Konsep

Setelah:

A = LLᵀ

maka sistem:

Ax = b

diselesaikan melalui:

Ly = b

kemudian:

Lᵀx = y

### Keunggulan

- Stabil
- Cepat
- Efisien

---

# Soal 11.6
## Cholesky Decomposition Manual

### Konsep

Menghitung elemen-elemen L secara langsung menggunakan rumus:

Lii = √(Aii − ΣLik²)

Lij = (Aij − ΣLikLjk)/Ljj

---

# Soal 11.7
## Cholesky pada Matriks Diagonal

### Konsep

Untuk matriks diagonal:

A = diag(a₁,a₂,a₃)

maka:

L = diag(√a₁,√a₂,√a₃)

### Tujuan

Memahami kasus khusus Cholesky.

---

# Soal 11.8
## Gauss-Seidel dengan Overrelaxation

### Konsep

Gauss-Seidel:

menggunakan nilai terbaru yang tersedia.

Overrelaxation:

x(new) = λx(GS)+(1−λ)x(old)

dengan:

λ > 1

### Tujuan

Mempercepat konvergensi.

---

# Soal 11.9
## Gauss-Seidel pada Sistem Reaktor

### Konsep

Sistem linear digunakan untuk memodelkan perpindahan massa dalam reaktor kimia.

### Materi

- Iterasi Gauss-Seidel
- Error Relatif

---

# Soal 11.10
## Metode Jacobi

### Konsep

Semua variabel menggunakan nilai iterasi sebelumnya.

Rumus:

xᵢ(k+1) = (bᵢ − Σaᵢⱼxⱼ(k))/aᵢᵢ

### Perbandingan

Jacobi lebih sederhana tetapi biasanya lebih lambat dibanding Gauss-Seidel.

---

# Soal 11.11
## Gauss-Seidel 3×3

### Konsep

Penerapan metode Gauss-Seidel pada SPL berukuran 3×3.

### Tujuan

Mencari solusi hingga memenuhi toleransi error tertentu.

---

# Soal 11.12
## Underrelaxation

### Konsep

Jika:

0 < λ < 1

maka disebut:

Underrelaxation

### Fungsi

Mengurangi osilasi dan meningkatkan stabilitas.

---

# Soal 11.13
## Overrelaxation

### Konsep

Jika:

λ > 1

maka disebut:

Overrelaxation

### Fungsi

Mempercepat konvergensi.

---

# Soal 11.14
## Analisis Konvergensi Gauss-Seidel

### Konsep

Tidak semua SPL dapat diselesaikan secara konvergen.

Konvergensi bergantung pada:

- Dominasi diagonal
- Radius spektral

---

# Soal 11.15
## Sistem yang Tidak Konvergen

### Konsep

Gauss-Seidel umumnya memerlukan:

|aii| > Σ|aij|

untuk setiap baris.

### Tujuan

Mengidentifikasi sistem yang divergen.

---

# Soal 11.16
## Condition Number

### Konsep

Mengukur sensitivitas solusi terhadap error.

Rumus:

cond(A)=||A|| ||A⁻¹||

### Interpretasi

Condition Number kecil:
- stabil

Condition Number besar:
- tidak stabil

---

# Soal 11.17
## Sistem Nonlinear Dua Variabel

### Konsep

Menyelesaikan:

f(x,y)=0

g(x,y)=0

secara simultan.

### Metode

- Substitusi
- Newton-Raphson Multivariabel
- fsolve

---

# Soal 11.18
## Pemodelan Produksi Elektronik

### Konsep

Masalah dunia nyata diterjemahkan menjadi:

Ax=b

### Tujuan

Menentukan jumlah produksi optimal.

---

# Soal 11.19
## Matriks Hilbert

### Konsep

Elemen:

Hij = 1/(i+j−1)

### Karakteristik

- Simetris
- Positif definit
- Sangat ill-conditioned

### Tujuan

Mempelajari pengaruh error pembulatan.

---

# Soal 11.20
## Matriks Vandermonde

### Konsep

Bentuk umum:

Vij = xi^(n−j)

### Aplikasi

- Interpolasi Polinomial
- Curve Fitting

---

# Soal 11.21
## Matriks Augmented

### Konsep

Gabungan:

[A | I]

digunakan dalam:

Gauss-Jordan Inverse

---

# Soal 11.22
## Bentuk Matriks, Transpose, dan Invers

### Konsep

Transformasi sistem persamaan ke bentuk:

Ax=b

Kemudian menentukan:

- Solusi
- Transpose
- Invers

---

# Soal 11.23
## Kompleksitas Thomas vs Gauss

### Konsep

Thomas:

O(n)

Gauss:

O(n³)

### Tujuan

Membandingkan efisiensi algoritma.

---

# Soal 11.24
## Program Umum Thomas Algorithm

### Konsep

Implementasi algoritma Thomas untuk sembarang matriks tridiagonal.

### Tujuan

Membuat solver yang dapat digunakan ulang.

---

# Soal 11.25
## Program Umum Cholesky

### Konsep

Membuat fungsi umum:

solve_cholesky(A,b)

untuk menyelesaikan berbagai SPL.

---

# Soal 11.26
## Program Umum Gauss-Seidel

### Konsep

Implementasi generik metode iteratif Gauss-Seidel.

### Input

- Matriks A
- Vektor b
- Toleransi

---

# Soal 11.27
## Finite Difference Method pada PDE

### Konsep

Persamaan diferensial:

D d²c/dx² − U dc/dx − kc = 0

diubah menjadi SPL menggunakan:

Finite Difference Method (FDM)

### Tujuan

Menentukan distribusi konsentrasi.

---

# Soal 11.28
## Sistem Pentadiagonal

### Konsep

Matriks memiliki:

- 2 sub-diagonal
- diagonal utama
- 2 super-diagonal

### Aplikasi

- Persamaan Diferensial Parsial (PDE)
- Simulasi aliran fluida
- Transfer panas 2D

### Keunggulan

Algoritma khusus pentadiagonal dapat mencapai kompleksitas:

O(n)

dibanding Eliminasi Gauss:

O(n³)

---

# Kesimpulan

Bab 11 memperkenalkan berbagai teknik numerik untuk menyelesaikan sistem persamaan linear dan nonlinear. Metode langsung seperti Cholesky dan Thomas memberikan solusi cepat dan akurat untuk struktur matriks tertentu, sedangkan metode iteratif seperti Jacobi dan Gauss-Seidel lebih cocok untuk sistem berukuran besar. Selain itu, konsep Condition Number menunjukkan pentingnya stabilitas numerik, sedangkan Finite Difference Method memperlihatkan bagaimana masalah fisika dan teknik dapat diubah menjadi sistem persamaan linear yang dapat diselesaikan secara komputasi.
