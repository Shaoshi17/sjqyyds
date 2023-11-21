import zlib
import struct
import argparse
import itertools


parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, default=None, required=True,
                    help="����ͬ��Ŀ¼��ͼƬ������")
args  = parser.parse_args()


bin_data = open(args.f, 'rb').read()
crc32key = zlib.crc32(bin_data[12:29]) # ����crc
original_crc32 = int(bin_data[29:33].hex(), 16) # ԭʼcrc


if crc32key == original_crc32: # ����crc�Ա�ԭʼcrc
    print('���û������!')
else:
    input_ = input("��߱�����, �Ƿ�CRC���ƿ��? (Y/n):")
    if input_ not in ["Y", "y", ""]:
        exit()
    else: 
        for i, j in itertools.product(range(4095), range(4095)): # ������0x FF FF FF FF�������ǵ���Ļʵ��/cpu��0x 0F FF�Ͳ���ˣ�Ҳ����4095��Ⱥ͸߶�
            data = bin_data[12:16] + struct.pack('>i', i) + struct.pack('>i', j) + bin_data[24:29]
            crc32 = zlib.crc32(data)
            if(crc32 == original_crc32): # ���㵱ͼƬ��СΪi:jʱ��CRCУ��ֵ����ͼƬ�е�CRC�Ƚϣ�����ͬ����ͼƬ��С�Ѿ�ȷ��
                print(f"\nCRC32: {hex(original_crc32)}")
                print(f"���: {i}, hex: {hex(i)}")
                print(f"�߶�: {j}, hex: {hex(j)}")
                exit(0)
