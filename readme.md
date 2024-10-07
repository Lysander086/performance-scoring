# performance scoring
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Main",
            "type": "debugpy",
            "request": "launch",
            "module": "app.main",
            "cwd": "${workspaceFolder}/src"
        }, 
        {
            "name": "Python Debugger: Current file",
            "type": "debugpy",
            "request": "launch",
            "module": "app.${fileBasenameNoExtension}",
            "cwd": "${workspaceFolder}/src"
        }, 
        {
            "name": "Run all tests",
            "type": "debugpy",
            "request": "launch",
            "module": "unittest", 
            "cwd": "${workspaceFolder}/src/",
            "args": [
                "discover",
                "-p",
                "*_test.py"
            ]
        },
    ]
}
```
# anchor log 
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Run all tests",
            "type": "debugpy",
            "request": "launch",
            "module": "unittest", 
            "cwd": "${workspaceFolder}/src/",
            "args": [
                "discover",
                "-p",
                "*_test.py"
            ]
        },
        {
            "name": "TestConfiguration.test_init",
            "type": "debugpy",
            "request": "launch",
            "module": "unittest",
            "cwd": "${workspaceFolder}/src/",
            "envFile": "${workspaceFolder}/.env",
            "python": "${workspaceFolder}/venv/Scripts/python.exe",
            "args": [
                "tests.config.configuration_test"
            ]
        },
    ]
}
```