function Initialize-Log {
    param (
        
    )
    # sqlite3 task-log.db ".exit"
    $local_path = "C:\Users\jacob.pavelka\Documents\PowerShell\Modules"
    $python_path = $local_path + "\time_management\.venv\Scripts\python.exe"
    Start-Process $python_path "-m test.py task-log.db"
}