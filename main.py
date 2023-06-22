import customtkinter as ctk
from pytube import YouTube

def baixar_video():
    url = entrada.get("1.0", "end-1c") 

    try:
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download()
        resultado_label.configure(text="Vídeo baixado com sucesso!")

    except Exception as e:
        resultado_label.configure(text="Erro ao baixar o vídeo: " + str(e))


janela = ctk.CTk()
janela.iconbitmap("ytlogo.ico")
janela.geometry("500x150")
janela.title("Youtube Download")
janela.resizable(False, False)

rotulo = ctk.CTkLabel(janela, text="URL do vídeo:")
rotulo.pack()

entrada = ctk.CTkTextbox(janela, width=490, height=5)
entrada.pack()

botao = ctk.CTkButton(janela, text="Baixar Vídeo", command=baixar_video,hover_color="red",fg_color="black")
botao.pack()

resultado_label = ctk.CTkLabel(janela, text="")
resultado_label.pack()

janela.mainloop()
