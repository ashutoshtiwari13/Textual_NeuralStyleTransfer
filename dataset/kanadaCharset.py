import io

text_string= "ಅ ಆ ಇ ಈ ಉ ಊ ಋ ಌ ಎ ಏ ಐ ಒ ಓ ಔ ೠ"

chars=['ಅ','ಆ','ಇ','ಈ','ಉ','ಊ','ಋ','ಌ','ಎ','ಏ','ಐ','ಒ','ಓ','ಔ','ೠ']

with io.open("kanadaCharset.txt", "w", encoding="utf-8") as f:
    for x in range(len(chars)):
        f.write(chars[x])
        f.write("\n")


    for x in range(len(chars)):
        for y in range(len(chars)):
            f.write(chars[x]+chars[y])
            f.write("\n")
