<#
PowerShell helper: installs Python (if missing), creates a venv,
installs requirements, and launches the Streamlit app.

Run as Administrator when installing Python.
Usage:
  Open PowerShell as Administrator
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  .\setup_and_run.ps1
#>

Set-StrictMode -Version Latest

function Test-PythonLauncher {
    param($cmd)
    try {
        & $cmd -c "import sys;print(sys.version)" > $null 2>&1
        return $true
    } catch {
        return $false
    }
}

# Prefer 'py' then 'python'
$candidates = @('py','python')
$pythonCmd = $null
foreach ($c in $candidates) {
    if (Get-Command $c -ErrorAction SilentlyContinue) {
        if (Test-PythonLauncher -cmd $c) {
            $pythonCmd = $c
            break
        }
    }
}

if (-not $pythonCmd) {
    Write-Output "Valid Python launcher not found. Downloading and installing Python 3.11 (silent)..."
    $installer = Join-Path $env:TEMP "python-installer.exe"
    $url = "https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe"
    Invoke-WebRequest -Uri $url -OutFile $installer -UseBasicParsing
    Start-Process -FilePath $installer -ArgumentList '/quiet','InstallAllUsers=1','PrependPath=1' -Wait
    Remove-Item $installer -Force

    # re-detect
    foreach ($c in $candidates) {
        if (Get-Command $c -ErrorAction SilentlyContinue) {
            if (Test-PythonLauncher -cmd $c) {
                $pythonCmd = $c
                break
            }
        }
    }

    if (-not $pythonCmd) {
        Write-Error "Python installation failed or Python not available on PATH. Please install manually from https://www.python.org/downloads/windows/ and re-run this script."
        exit 1
    }
}

Write-Output "Using Python launcher: $pythonCmd"

# Create venv
$venvPath = Join-Path (Get-Location) ".venv"
if (-not (Test-Path $venvPath)) {
    & $pythonCmd -m venv $venvPath
}

$pip = Join-Path $venvPath "Scripts\python.exe"
& $pip -m pip install --upgrade pip
& $pip -m pip install -r "requirements.txt"

Write-Output "Starting Streamlit app..."
Start-Process -FilePath $pip -ArgumentList '-m','streamlit','run','app.py' -WorkingDirectory (Get-Location)

Write-Output "Streamlit launched. Visit http://localhost:8501 in your browser."
