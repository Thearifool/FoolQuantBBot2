Write-Host 'Deploying FoolQuantBot2...'
Start-Process -FilePath 'python' -ArgumentList '-m bot.core.hft_execution --mode auto'
