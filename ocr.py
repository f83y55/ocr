import sys, os, re, pytesseract
from PIL import Image
""" $ sudo apt install tesseract-ocr
    $ pip install pytesseract
    """


def write_text(filename:str, st:str) :
    with open(filename, 'w') as file :
        file.write(st)

def traite_fichier(filename:str, display:bool=False) -> str :
    os.system('cls' if os.name == 'nt' else 'clear')
    input(f"Convert {filename} : Press enter")
    st = pytesseract.image_to_string(Image.open(filename))
    return st

if __name__ == "__main__" :
    MAINROOT = "."
    INPUT = "input"        
    OUTPUT = "output"      
    DISPLAY = True         # affiche le nom des fichiers traités 1 à 1
    try :
        os.makedirs(os.path.join(MAINROOT, OUTPUT), exist_ok=True)
    except Exception as e :
        print(f"Exception : {e}")
    if len(sys.argv)>1 :               # les fichiers à traiter sont en argument
        filenames = sys.argv[1:]
    else :                             # sinon tous les fichiers .tex sont traités
        filenames = [el for el in os.listdir(os.path.join(MAINROOT, INPUT))]
    for filename in filenames :
        st = traite_fichier(os.path.join(MAINROOT, INPUT, filename), display=DISPLAY)
        write_text(os.path.join(MAINROOT, OUTPUT, f"{filename[:-4]}.txt"), st)

