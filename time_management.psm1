function Initialize-Log {
    param (
        
    )
    sqlite3 "task-log.db"
    $local_path = "C:\Users\jacob.pavelka\Documents\PowerShell\Modules"
    $python_path = $local_path + "\time_management\.venv\python.exe"
    $python_path -m test.py "task-log.db"
}