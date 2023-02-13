import dropbox

# Inicia sesión en Dropbox
dbx = dropbox.Dropbox("YOUR_ACCESS_TOKEN")

# Obtiene la información de un archivo en particular
file = dbx.files_get_metadata("/path/to/file.ext")

# Imprime la información del archivo
print(file.name)
print(file.client_modified)
print(file.server_modified)