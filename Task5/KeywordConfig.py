#Keyword configuration system

def system_config(**settings):
    print("=== Task 3: Keyword Config System ===")
    for key, value in settings.items():
        print(f"{key}: {value}")

system_config(mode="debug", version="1.0", port=8080)