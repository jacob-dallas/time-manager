function Initialize-Project {
    $project_name = (get-item .).fullname
    Invoke-Python "$PSScriptRoot\lib\init_project.py" "$PSScriptRoot $project_name"
}

function Add-Log {
    param (
        $activity
    )
}
function End-Log {
    param (
    )
}
function Out-Log {
    param (
        $num_entries
    )
}

function Initialize-Timesheet {
    Invoke-Python "$PSScriptRoot\timesheet.py"
}

function Configure-Activity {
    param (
        $activity_name
    )

    Invoke-Python "$PSScriptRoot\lib\init_activity.py" "$PSScriptRoot $activity_name"
}



function Invoke-Python {
    param (
        [Parameter(Mandatory=$true)][string]$script,
        [string] $args
    )

    $exestr = $script+" "+$args

    $python_path = "$PSScriptRoot\.venv\Scripts\python.exe"

    Start-Process $python_path $exestr -NoNewWindow
}