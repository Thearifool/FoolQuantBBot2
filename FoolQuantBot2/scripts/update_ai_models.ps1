Write-Host 'Updating AI models...'
Start-Process -FilePath 'python' -ArgumentList '-m scripts.update_ai_models'
