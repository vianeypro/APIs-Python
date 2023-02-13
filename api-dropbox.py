import dropbox

# Inicia sesi�n en Dropbox
dbx = dropbox.Dropbox("YOUR_ACCESS_TOKEN")

# Obtiene la informaci�n de un archivo en particular
file = dbx.files_get_metadata("/path/to/file.ext")

# Imprime la informaci�n del archivo
print(file.name)
print(file.client_modified)
print(file.server_modified)