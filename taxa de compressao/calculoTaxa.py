
import math


def calc_volume_cilindro(diamentro_cilindro):
    resultado_divisao = diamentro_cilindro/2

    parte_decimal = str(resultado_divisao).split('.')[1][:2]
    parte_inteira_str = str(resultado_divisao).split('.')[0]

    raio = f'{parte_inteira_str}.{parte_decimal}'
    resultado_arre = float(raio) * 2
    resto = diamentro_cilindro - resultado_arre

    valor = round(float(raio) + resto,2)

    area = math.pi * (valor**2)
    area = round(area)

    print(f'divisão: {resultado_divisao}, ao quadrado: {round(valor)**2}, area: {round(area)}')
    
    return area

def calc_volume_altura(area, altura):
    numero_formatado = f"{area:,.1f}"
    remove_pos_virgula = str(numero_formatado).split('.')[0]
    numero_sem_virgula = remove_pos_virgula.replace(",",".")
    v = float(numero_sem_virgula) * altura
    print(f'Area: {area}, altura: {remove_pos_virgula}, resultado {numero_sem_virgula}')
    v = round(v)
    return v

def volume_camara(area, alt, vcab):
    v = area * alt
    numero_formatado = f"{v:,.1f}"
    remove_pos_virgula = str(numero_formatado).split('.')[0]
    numero_sem_virgula = remove_pos_virgula.replace(",",".")
    vdeck = f'{float(numero_sem_virgula):.2f}'
    vcam = float(vdeck) + float(vcab)

    return vcam, vdeck

def cal_taxa_compressao(vcil, vcam):
    t = (vcil + vcam)/vcam
    return t

def alterar_volume_deck(taxa_ideal, vcil, vdeck):
    # taxa = vcil + vdeck + vcab/ vdeck + vcab
    taxa = taxa_ideal
    vdeck = float(vdeck)
    vcil = float(vcil)
    vcab = taxa * vdeck
    r = vcil + vdeck
    v = r - vcab
    print(f'alterar: {vcil}, {vcab}, {r}, {v}')
    vcab = taxa - 1
    resultado = v/vcab

    return resultado

   


diametro_cilindro = 85.5
altura_curso_cilindro  = 69
altura_cilindro_ponto_morto_superior =2
volume_camara_combustao = 34
taxa_ideal = 9.5

area = calc_volume_cilindro(diametro_cilindro)

volume = calc_volume_altura(area, altura_curso_cilindro)

vcam, vdeck = volume_camara(area, altura_cilindro_ponto_morto_superior, volume_camara_combustao)

taxa = cal_taxa_compressao(volume, vcam)

alterar = alterar_volume_deck(taxa_ideal, volume, vdeck)

print(f'Volume cilindro: {volume}, Volume Camera: {vcam}, vdeck: {vdeck}')
print(f'Taxa: {taxa}\n')
print(f'Precisa alterar {alterar}')