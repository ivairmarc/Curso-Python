
import math

volume_deslocamento = 0
volume_comprimento = 0


def calc_volume_cilindro(diamentro_cilindro):
    pi = 3.14
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

# vcab volume da camara de combustão
# vdeck
# vcam
def volume_camara(area, alt, vcab):
    v = area * alt
    numero_formatado = f"{v:,.1f}"
    remove_pos_virgula = str(numero_formatado).split('.')[0]
    numero_sem_virgula = remove_pos_virgula.replace(",",".")
    vdeck = f'{float(numero_sem_virgula):.1f}'
    vcam = float(vdeck) + float(vcab)

    return vcam

def cal_taxa_compressao(vcil, vcam):
    t = (vcil + vcam)/vcam
    return t

diametro_cilindro = 90.45
altura_curso_cilindro  = 69
altura_cilindro_ponto_morto_superior = 1.30
volume_camara_combustao = 58

area = calc_volume_cilindro(diametro_cilindro)

volume = calc_volume_altura(area, altura_curso_cilindro)

vcam = volume_camara(area, altura_cilindro_ponto_morto_superior, volume_camara_combustao)

taxa = cal_taxa_compressao(volume, vcam)

print(taxa)