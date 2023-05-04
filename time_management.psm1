function Initialize-Log {
    param (
        
    )
    # get location is not saving to string
    $local_path = (get-item .).fullname
    $module_path = "C:\Users\jacob.pavelka\Documents\PowerShell\Modules"
    $python_path = $module_path + "\time_management\.venv\Scripts\python.exe"
    Start-Process $python_path "$PSScriptRoot\test.py $local_path\task-log.db" -RedirectStandardOutput "out.txt" -RedirectStandardError "error.txt"
}