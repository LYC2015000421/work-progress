from Bio import SeqIO
import pandas as pd

meta = []
sequence = []
label = []
i = 0
seq = ('F:\Python\PythonProject\sequence.fasta')  # 转换的文件
for seq_record in SeqIO.parse(seq, "fasta"):
    meta.append(str(seq_record.id))
    sequence.append(str(seq_record.seq))
    i = 1 + i
    label.append(int(i))
    # print(sequence)
df = pd.DataFrame(data={'Meta': meta, 'SequenceID': sequence, 'Label': label})  # 转换后的文件的表头

print(df)

    # 数据存入csv
df.to_csv("sequence.csv", sep=',', index=False)  # 转换后的文件

