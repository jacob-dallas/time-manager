function Initialize-Log {
    param (
        
    )
    # sqlite3 task-log.db ".exit"
    $local_path = Get-Location
    $module_path = "C:\Users\jacob.pavelka\Documents\PowerShell\Modules"
    $python_path = $module_path + "\time_management\.venv\Scripts\python.exe"
    Start-Process $python_path "-m test.py $localpath\task-log.db"
}