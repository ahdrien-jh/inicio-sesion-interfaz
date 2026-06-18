# ==========================================
#        PROYECTO NEXUS -inicio sesion
# ==========================================

import customtkinter as ctk

# 1. CONFIGURACION VISUAL 
# Activamos el modo oscuro y el tema azul estándar
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Creamos la ventana principal del Login
ventana = ctk.CTk()
ventana.title("NEXUS - Inicio de Sesión")
ventana.geometry("400x520")
ventana.resizable(False, False) # Evita que deformen la interfaz al maximizar
ventana.configure(fg_color="#1d2be0")

# 2. LOGICA DE AUTENTICACION (FRONTEND)
def iniciar_sesion():
    # Extraemos el usuario y la clave que escribieron en pantalla
    usuario = txt_usuario.get()
    clave = txt_contrasena.get()
    
    # Estructuramos las credenciales en un paquete listo para validar con el backend
    credenciales = {
        "usuario": usuario,
        "contrasena": clave
    }
    
    # Verificacion en consola para asegurar que el Frontend empaqueto todo antes de ir al servidor
    print("\n--- [FRONTEND] ENVIANDO CREDENCIALES AL BACKEND PARA VALIDAR ---")
    print(credenciales)

# 3. Contenedor central
frame_central = ctk.CTkFrame(ventana, fg_color="#1A1C23", corner_radius=15)
frame_central.pack(padx=25, pady=25, fill="both", expand=True)

# Título de la interfaz
lbl_titulo = ctk.CTkLabel(frame_central, text="Iniciar Sesión", font=("Arial", 24, "bold"), text_color="white")
lbl_titulo.pack(pady=25)

# Campo 1: Usuario
lbl1 = ctk.CTkLabel(frame_central, text="Correo:", anchor="w", text_color="#A0AEC0", font=("Arial", 12, "bold"))
lbl1.pack(fill="x", padx=25, pady=2)

txt_usuario = ctk.CTkEntry(frame_central, placeholder_text="Ej. usuario@correo.com", height=38, fg_color="#2D3748", text_color="white")
txt_usuario.pack(fill="x", padx=25, pady=5)

# Campo 2: Contraseña
lbl2 = ctk.CTkLabel(frame_central, text="Contraseña:", anchor="w", text_color="#A0AEC0", font=("Arial", 12, "bold"))
lbl2.pack(fill="x", padx=25, pady=2)

txt_contrasena = ctk.CTkEntry(frame_central, placeholder_text="••••••••", show="*", height=38, fg_color="#2D3748", text_color="white")
txt_contrasena.pack(fill="x", padx=25, pady=5)

# Boton principal de acceso
btn_ingresar = ctk.CTkButton(
    frame_central, 
    text="INGRESAR", 
    fg_color="#1d2be0", 
    hover_color="#151FA3", 
    text_color="white", 
    height=42, 
    font=("Arial", 13, "bold"), 
    command=iniciar_sesion
)
btn_ingresar.pack(fill="x", padx=25, pady=20)

# Texto de ayuda para navegacion
lbl_registro = ctk.CTkLabel(frame_central, text="¿No tienes una cuenta de técnico?", text_color="#718096", font=("Arial", 11))
lbl_registro.pack(pady=5)

# Boton secundario de registro
btn_ir_registro = ctk.CTkButton(
    frame_central, 
    text="Registrarse", 
    fg_color="#4A5568", 
    hover_color="#2D3748", 
    text_color="white", 
    height=35
)
btn_ir_registro.pack(fill="x", padx=25, pady=5)

# 4. ACTIVACION DE LA INTERFAZ
ventana.mainloop()