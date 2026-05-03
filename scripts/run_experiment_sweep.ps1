Write-Host "Starting MLflow experiment sweep..."

# Activate virtual environment
if (Test-Path ".\.venv\Scripts\Activate.ps1") {
    .\.venv\Scripts\Activate.ps1
} else {
    Write-Host "Virtual environment not found!"
    exit 1
}

# Check MLflow server
Write-Host "Checking MLflow server..."

try {
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:5001/health" -UseBasicParsing -TimeoutSec 3
    Write-Host "MLflow server is running"
}
catch {
    Write-Host "MLflow server not running!"
    Write-Host "Start it using:"
    Write-Host "mlflow server --host 127.0.0.1 --port 5001"
    exit 1
}

# Run Python script
python scripts/run_experiment_sweep.py

Write-Host "Sweep complete!"