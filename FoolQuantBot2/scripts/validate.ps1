Write-Host 'Validating FoolQuantBot2...'
if (!(Test-Path 'B:\FoolQuantBot2\bot\core\hft_execution.py')) {
    Write-Error 'Core execution engine missing'
}
Write-Host 'Validation Complete!'
