import base64

if __name__ == "__main__":
    file_name = input("输入要混淆的文件名: ")
    output_name = input("输入要混淆的文件名: ")
    with open(file_name, mode="r", encoding="utf-8") as f:
        text = f.read().encode("utf-8")
    b = base64.b64encode(text)
    code = f"exec(\"import base64\\nb = {b}\\nexec(base64.b64decode(b.decode('utf-8')).decode('utf-8'))\")"
    with open(output_name, mode="w", encoding="utf-8") as f:
        f.write(code)
