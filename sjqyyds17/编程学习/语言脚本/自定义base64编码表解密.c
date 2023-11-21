
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 自定义Base64编码表
const char base64_table[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
// 解码函数
void base64_decode(const char* input, char* output) {
    int i, j;
    int index = 0;
    int len = strlen(input);

    for (i = 0; i < len; i += 4) {
        unsigned char values[4];
        memset(values, 0xFF, sizeof(values));

        for (j = 0; j < 4 && i + j < len; j++) {
            // 在自定义Base64编码表中查找对应的值
            const char* pos = strchr(base64_table, input[i + j]);
            if (pos != NULL) {
                values[j] = pos - base64_table;
            }
        }

        // 解码为原始数据
        output[index++] = (values[0] << 2) | (values[1] >> 4);
        output[index++] = (values[1] << 4) | (values[2] >> 2);
        output[index++] = (values[2] << 6) | values[3];
    }

    output[index] = '\0';
}

int main() {
    const char* encoded_data = "SGVsbG8gV29ybGQh";  // 要解码的Base64字符串
    char decoded_data[100];  // 解码后的原始数据

    base64_decode(encoded_data, decoded_data);

    printf("Decoded Data: %s\n", decoded_data);

    return 0;
}