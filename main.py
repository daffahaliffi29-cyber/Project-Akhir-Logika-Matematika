#file main sementara
def input_kriteria(pertanyaan):
    while True:
        jawaban = input(pertanyaan + " (ya/tidak): ").lower().strip()

        if jawaban == "ya":
            return True
        elif jawaban == "tidak":
            return False
        else:
            print("Input tidak valid! Masukkan ya atau tidak.")


def main():

    print("================================")
    print("     PROPOSAL APPROVAL SYSTEM")
    print("================================")

    nama = input("\nNama kegiatan: ")

    print("\n--- INPUT KRITERIA PROPOSAL ---")

    # Input empat variabel proposisi
    K = input_kriteria("Apakah proposal sudah lengkap?")
    B = input_kriteria("Apakah pembina menyetujui?")
    D = input_kriteria("Apakah dana mencukupi?")
    J = input_kriteria("Apakah jadwal tersedia?")

    print("\n--- DATA BERHASIL DICATAT ---")
    print("Nama kegiatan:", nama)
    print("Kelengkapan proposal:", K)
    print("Persetujuan pembina:", B)
    print("Ketersediaan dana:", D)
    print("Ketersediaan jadwal:", J)

    print("\nEvaluasi keputusan belum diimplementasikan.")


if __name__ == "__main__":
    main()
