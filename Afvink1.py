#Afvinkopdracht 1 #
#Built-in Errors  #
#Gerben Schreuders#
###################

from time import sleep
#Except ImportError

def main():
    #try:
        bestand = "alpaca_beest.fna"     
        headers_line, seqs_line = lees_inhoud(bestand)
    #except IOError:
     #   print("Het programma kan niet uitgevoerd worden. ► Bestand niet gevonden. ")
    #except:
     #   print("Onbekende fout!")
              
        code = input("Als je het programma wilt gebruiken, typ dan ❞Doorgaan.❝ ► ")
        if code == "Doorgaan":
            print(60*'─')
            sleep(1)
            print("Met dit propgramma kan je een aantal sequenties analyseren...")
            sleep(1.5)
            print("• Kies uit: DNA & knip_sequentie.")
            sleep(1.5)
            print("• Om DNA & knip_sequentie beide te analyseren »»» typ dan allebij.")
            sleep(1.5)
            PR0_INPUT = input("░░░░░⌠► ")
        
            if PR0_INPUT == "DNA":
                try:
                    print("■ Voer je aantal in.")
                    aantal=int(input("░░░░░⌠► "))
                    is_dna(seqs_line, headers_line, aantal)
                except ValueError:
                    print("⌠Jouw invoer is geen getal. Probeer opnieuw!⌡")
                    quit()
                
            elif PR0_INPUT == "knip_sequentie":
                try:
                    print("■ Voer je aantal in.")
                    aantal=int(input("░░░░░⌠► "))
                    knipt(seqs_line, headers_line, aantal)
                except ValueError:
                    print("⌠Jouw invoer is geen getal. Probeer opnieuw!⌡")
                    quit()
        
            
            elif PR0_INPUT == "allebij":
                try:
                    print("■ Voer je aantal in.")
                    aantal=int(input("░░░░░⌠► "))
                    is_dna(seqs_line, headers_line, aantal)                             
                    knipt(seqs_line, headers_line, aantal)
                except ValueError:
                    print("⌠Jouw invoer is geen getal. Probeer opnieuw!⌡")
                except ValueError:
                    print("Conversie getal mislukt")
                    quit()
            
            elif PR0_INPUT != "dna" and PR0_INPUT != "knip_sequentie" and PR0_INPUT5 !="allebij":
                print("⌠¿Heb je misschien een typfout gemaakt?⌡ (Verkeerde input)")
                quit()
        else:
            print("⌠¿Heb je misschien een typfout gemaakt? (Vekeerde Input)⌡")
            quit()
   
    
def lees_inhoud(bestands_naam):
     bestand = open(bestands_naam)
     headers = []
     seqs = []
     seq = ""
     for line in bestand:
         line=line.strip()
         if ">" in line:
             if seq != "":
                 seqs.append(seq)
                 seq = ""
             headers.append(line)
         else:
             seq += line.strip()
     seqs.append(seq)
     return headers, seqs

    
    

            
def knipt(seqs_line, headers_line, aantal):

    #try:
            ENZYM_BESTAND =   open("enzymen.txt")
    # except IOError:
     #           print("Het bestand 'enzymen.txt' is niet gevonden...")
            list1   =   []
            i2      =   0
            i3      =   0
            while i2 < aantal:                          
                i2 += 1
                for line in ENZYM_BESTAND:
                    enzym, seq = line.split()               
                    seq = seq.replace("^","")
                    list1.append(seq)
            
                    for l in seqs_line[:50]:
                        x = seqs_line[i3].find(seq)              
                        i3 += 1
                        if x > 0:
                            print("Match → ",enzym, "met Sequentie:")
                            print(headers_line[i3])
                            print("op de positie → ",x)    
                            print(seqs_line[i3])
                            print((x-1)*"─",seq)
                            print(50*"─")

                    

def is_dna(seqs_line, headers_line, aantal):

    line_a=[]                        
    line_t=[]                     
    line_c=[]
    line_g=[]
    line_u=[]
    totaal=[]

    for line in seqs_line:
        
        a=line.count("A")        
        line_a.append(a)

        t=line.count("T")
        line_t.append(t)

        c=line.count("C")
        line_c.append(c)

        g=line.count("G")
        line_g.append(g)

        tot = line.count("")
        totaal.append(tot)

    i = 0
    while i < aantal  :                      
        i += 1
        if line_a[i]+line_t[i]+line_c[i]+line_g[i] == (totaal[i] -2):
            print(headers_line[i],"• = √ mRNA")  
            print(65*"─")
        else:
            print(headers_line[i],"• = × mRNA")
            print(65*"─")

'''
def check(seq):
        try:
seq = seq.upper()
seq = invoer() for x in seq:
print("Dit is de sequentie:", seq) if x in
except TypeError:
["B","J","O","U","X","Z"]:
print("Deze invoer bestaat niet uit
nucleotiden.")
def invoer():
return False
return True
'''               
        

main()




