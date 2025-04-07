# Chemin d'AxProtector
$axProtectorPath = "C:\AxProtector\axprotector.exe"

# Dossier contenant le fichier .whl
$extractedFolder = "C:\Users\User\OneDrive\Bureau\Pycharm\PackageTag\whl_extracted"

# Vérifications
if (-Not (Test-Path $axProtectorPath)) {
    Write-Error "AxProtector introuvable : $axProtectorPath"
    exit 1
}

if (-Not (Test-Path $extractedFolder)) {
    Write-Error "Dossier inexistant : $extractedFolder"
    exit 1
}
# Récupère tous les fichiers .whl dans le dossier
$whlFiles = Get-ChildItem -Path $extractedFolder -Filter "*.whl" -File

if ($whlFiles.Count -ne 1) {
    Write-Error "Il doit y avoir exactement un seul fichier .whl dans le dossier."
    exit 1
}
# Lancer la protection du fichier .whl
$whlFile = $whlFiles[0].FullName
Write-Host "Protection du fichier : $whlFile"

try {
# Exécution de AxProtector
    $process = Start-Process -FilePath $axProtectorPath -ArgumentList "/protect `"$whlFile`"" -Wait -NoNewWindow -PassThru
 # Vérifie le code de sortie
    if ($process.ExitCode -ne 0) {
        Write-Error "Échec de la protection. Code : $($process.ExitCode)"
        exit $process.ExitCode
    }
    Write-Host "Protection terminée avec succès."
} catch {
    Write-Error "Erreur lors de l'exécution : $_"
    exit 1
}