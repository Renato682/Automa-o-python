import pyautogui as pag
import openpyxl 
import pyperclip
from time import sleep

# Tempo de espera entre cada comando do pyautogui (em segundos)
pag.PAUSE = 2

# Carregar a planilha de dados
workbook = openpyxl.load_workbook('dados.xlsx')
sheet_produtos = workbook['Produtos']

# Pequena pausa para dar tempo de você abrir a tela do sistema após rodar o código
print("Iniciando a automação em 5 segundos... Abra a janela do formulário!")
sleep(5)

# Iterar sobre as linhas a partir da segunda (ignorando o cabeçalho)
for i in sheet_produtos.iter_rows(min_row=2):
    cliente = i[0].value 
    produto = i[1].value 
    quantidade = i[2].value 
    categoria = i[3].value 
    # data_hora = i[4].value -> Não é necessário preencher no formulário
    
    # Condição de parada: se a coluna Cliente estiver vazia, encerra o loop
    if cliente is None:
        break

    # 1. Preencher Cliente
    pyperclip.copy(str(cliente))
    pag.click(626,460)
    pag.hotkey('ctrl', 'v')

    # 2. Preencher Produto
    pyperclip.copy(str(produto))
    pag.click(605,590)
    pag.hotkey('ctrl', 'v')

    # 3. Preencher Quantidade
    pyperclip.copy(str(quantidade))
    pag.click(585,716)
    pag.hotkey('ctrl', 'v')

    # 4. Preencher Categoria (Menu Dropdown)
   # 4. Selecionar Categoria (Menu Dropdown)
    pag.click(538, 913) # Clica para abrir a lista de categorias
    sleep(0.5) # Pequena pausa para garantir que o menu abriu
    
    # Digita o nome da categoria para que o navegador selecione a opção correta
    pag.write(str(categoria)) 
    sleep(0.5) # Pausa rápida para o navegador processar a seleção
    
    pag.press('enter') # Confirma a seleção
    # 5. Clicar no botão Salvar
    pag.click(586,923)
    
    # Pausa extra para garantir que o site registre o salvamento e recarregue os campos
    sleep(6)

