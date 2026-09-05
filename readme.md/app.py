import customtkinter as ctk

ctk.set_appearance_mode("dark")

fator_atividade = {
    "Sedentário": 1.2,
    "Levemente ativo": 1.375,
    "Moderadamente ativo": 1.55,
    "Altamente ativo": 1.725,
    "Extremamente ativo": 1.9
}

def calcular_tmb():
    try:
        peso = float(campo_peso.get())
        altura = float(campo_altura.get())
        idade = int(campo_idade.get())
        sexo = sexo_segmented.get()  # retorna "M" ou "F"

        if sexo == "M":
            for1 = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
        else:
            for1 = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)

        atividade = atividade_menu.get()          # texto escolhido no menu
        fator = fator_atividade[atividade]         # busca o número no dicionário
        gct = for1 * fator                         # gasto calórico total

        resultado_tmb.configure(
            text=f"TMB: {for1:.2f} kcal/dia\nGasto Total: {gct:.2f} kcal/dia"
        )
    except ValueError:
        resultado_tmb.configure(text="Preencha todos os campos corretamente.")


app = ctk.CTk()
app.title("Calculadora de TMB e GCT")
app.geometry("600x600")

label_peso = ctk.CTkLabel(app, text="peso em kg:")
label_peso.pack(pady=0)

campo_peso = ctk.CTkEntry(app, placeholder_text="Digite seu peso")
campo_peso.pack(pady=10)

label_altura = ctk.CTkLabel(app, text="altura em cm:")
label_altura.pack(pady=0)

campo_altura = ctk.CTkEntry(app, placeholder_text="Digite sua altura")
campo_altura.pack(pady=10)

label_idade = ctk.CTkLabel(app, text="idade:")
label_idade.pack(pady=0)

campo_idade = ctk.CTkEntry(app, placeholder_text="Digite sua idade")
campo_idade.pack(pady=10)

label_sexo = ctk.CTkLabel(app, text="sexo:")
label_sexo.pack(pady=0)

sexo_segmented = ctk.CTkSegmentedButton(app, values=["M", "F"])
sexo_segmented.set("M")
sexo_segmented.pack(pady=10)

label_atividade = ctk.CTkLabel(app, text="nível de atividade:")
label_atividade.pack(pady=0)

atividade_menu = ctk.CTkOptionMenu(app, values=list(fator_atividade.keys()))
atividade_menu.set("Sedentário")
atividade_menu.pack(pady=10)

botao_calcular = ctk.CTkButton(app, text="Calcular TMB", command=calcular_tmb)
botao_calcular.pack(pady=10)

resultado_tmb = ctk.CTkLabel(app, text='Sua TMB é: 0.00 kcal/dia', text_color="white")
resultado_tmb.pack(pady=10)
text='sua tmb é: 0.00 kcal/dia\nGasto Total: 0.00 kcal/dia'
font = ctk.CTkFont(size=12)

app.mainloop()