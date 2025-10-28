import fitz  # PyMuPDF

pdf_path = "schematic.pdf"
doc = fitz.open(pdf_path)

for page in doc:
    # Obtenir tous les blocs de texte et images
    blocks = page.get_text("blocks")  # [(x0, y0, x1, y1, "text", ...), ...]
    
    if blocks:
        # Créer un rectangle englobant tous les blocs
        x0 = min(b[0] for b in blocks)
        y0 = min(b[1] for b in blocks)
        x1 = max(b[2] for b in blocks)
        y1 = max(b[3] for b in blocks)
        rect = fitz.Rect(x0, y0, x1, y1)
        
        # Appliquer le crop
        page.set_cropbox(rect)

# Sauvegarder le PDF recadré
doc.save("pdf_recadre.pdf")
