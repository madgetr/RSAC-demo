import inspect
import torch._inductor.codecache as codecache

getsource = inspect.getsource(codecache.compile_file())
print(getsource)

dangerous_imports = {"subprocess", "exec", "eval"}

for line in getsource.split("\n"):
    for dangerous_import in dangerous_imports:
        if dangerous_import in line:
            print("Dangerous import found:", dangerous_import)
            break
