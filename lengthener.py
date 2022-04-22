import re
import base64

if __name__ == "__main__":
    file_name = input("输入要解密的文件名: ")
    output_name = input("输出的文件名: ")
    with open(file_name, mode="r", encoding="utf-8") as f:
        text = f.read()
    b = re.finditer(r"\".+?b[ ]+=[ ]+b'(.+?)'", text).__next__().group(1)
    code = base64.b64decode(b).decode("utf-8")
    with open(output_name, "w") as f:
        f.write(code)
