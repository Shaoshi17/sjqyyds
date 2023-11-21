
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// �Զ���Base64�����
const char base64_table[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
// ���뺯��
void base64_decode(const char* input, char* output) {
    int i, j;
    int index = 0;
    int len = strlen(input);

    for (i = 0; i < len; i += 4) {
        unsigned char values[4];
        memset(values, 0xFF, sizeof(values));

        for (j = 0; j < 4 && i + j < len; j++) {
            // ���Զ���Base64������в��Ҷ�Ӧ��ֵ
            const char* pos = strchr(base64_table, input[i + j]);
            if (pos != NULL) {
                values[j] = pos - base64_table;
            }
        }

        // ����Ϊԭʼ����
        output[index++] = (values[0] << 2) | (values[1] >> 4);
        output[index++] = (values[1] << 4) | (values[2] >> 2);
        output[index++] = (values[2] << 6) | values[3];
    }

    output[index] = '\0';
}

int main() {
    const char* encoded_data = "SGVsbG8gV29ybGQh";  // Ҫ�����Base64�ַ���
    char decoded_data[100];  // ������ԭʼ����

    base64_decode(encoded_data, decoded_data);

    printf("Decoded Data: %s\n", decoded_data);

    return 0;
}