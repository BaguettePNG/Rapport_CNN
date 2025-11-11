from PyPDF2 import PdfReader, PdfWriter

def split_single_page_pdf(input_pdf, output_top, output_bottom):
    reader = PdfReader(input_pdf)
    page = reader.pages[0]

    width = float(page.mediabox.width)
    height = float(page.mediabox.height)

    # --- Partie haute ---
    top_writer = PdfWriter()
    top_page = reader.pages[0]  # on réutilise la page originale
    top_page.mediabox.lower_left = (0, height / 2)
    top_page.mediabox.upper_right = (width, height)
    top_writer.add_page(top_page)

    # --- Partie basse ---
    bottom_writer = PdfWriter()
    bottom_page = reader.pages[0]
    bottom_page.mediabox.lower_left = (0, 0)
    bottom_page.mediabox.upper_right = (width, height / 2)
    bottom_writer.add_page(bottom_page)

    # Écriture dans les fichiers
    with open(output_top, "wb") as f_top:
        top_writer.write(f_top)

    with open(output_bottom, "wb") as f_bottom:
        bottom_writer.write(f_bottom)

    print(f"✅ Page divisée en deux :")
    print(f" - Haut : {output_top}")
    print(f" - Bas : {output_bottom}")

# Exemple d'utilisation
if __name__ == "__main__":
    split_single_page_pdf(
        r"C:\Users\bnola\Documents\Polytech\ETN4\Rapport_CNN\RapportFinal\images\inter\Automate_Reception_trame.pdf",
        "document_part1.pdf",
        "document_part2.pdf"
    )
