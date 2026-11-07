from PIL import Image
import sys
import os

def recortar_icone(caminho_entrada, caminho_saida):
    try:
        img = Image.open(caminho_entrada)
        bbox = img.getbbox()
        if bbox is None:
            print("Aviso: A imagem está totalmente transparente!")
            return
        img_cropped = img.crop(bbox)
        img_cropped.save(caminho_saida, "PNG")
        print(f"Sucesso! Imagem salva como '{caminho_saida}' com dimensões ajustadas.")
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

if __name__ == "__main__":
    arquivo_entrada = "a.png"
    arquivo_saida = "fertilizante_ajustado.png"
    recortar_icone(arquivo_entrada, arquivo_saida)