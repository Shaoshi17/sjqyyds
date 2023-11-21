import base64
import base64
import codecs

# 读取文件中的密文
with open("code.txt", "r") as file:
    ciphertext = file.read().strip()

# 循环解密 Base64 和 Base32 编码数据
while True:
    try:
        # 尝试使用 Base64 解码
        decoded_data = base64.b64decode(ciphertext)
        ciphertext = decoded_data.decode()
        print("Base64 Decoded:", decoded_data)
    except:
        try:
            # 尝试使用 Base32 解码
            decoded_data = base64.b32decode(ciphertext)
            ciphertext = decoded_data.decode()
            print("Base32 Decoded:", decoded_data)
        except:
            # 解密完成或无法解码时退出循环
            break

# 将解密后的数据写入文件
with open("decrypted_code.txt", "w") as file:
    file.write(ciphertext)

print("解密完成，解密后的数据已保存到 decrypted_code.txt 文件中。")