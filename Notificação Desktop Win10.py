from win10toast import ToastNotifier

#Inicializa#
toaster = ToastNotifier()

toaster.show_toast(
    "Notificação","Olá Iago bem vindo ao Python :)",
    threaded=True,
    icon_path=None,
    duration=3 #segundos
)