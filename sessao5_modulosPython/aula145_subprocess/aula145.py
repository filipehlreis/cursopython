import subprocess

# Windows - ping IP 127.0.0.1
# Linux - ping IP 127.0.0.1 -c 4


proc = subprocess.run(
    # ['ping', '127.0.0.1']
    ['ping', '177.76.176.208'],
    capture_output=True,
    text=True
)

saida = proc.stdout
# saida = saida.replace('tempo', 'filipe')
print(saida)
