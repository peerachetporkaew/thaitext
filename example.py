from pythainlp.tokenize import subword_tokenize
import re 


text = ("พระราชบัญญัติธรรมนูญการปกครองแผ่นดินสยามชั่วคราว พุทธศักราช ๒๔๗๕ "
        "เป็นรัฐธรรมนูญฉบับชั่วคราว ซึ่งถือว่าเป็นรัฐธรรมนูญฉบับแรกแห่งราชอาณาจักรสยาม "
        "ประกาศใช้เมื่อวันที่ 27 มิถุนายน พ.ศ. 2475 Mancity Co.,LTD 20:43 12_2 นายประยุทธ์ จันทร์โอชา"
        "โดยเป็นผลพวงหลังการปฏิวัติเมื่อวันที่ 24 มิถุนายน พ.ศ. 2475 โดยคณะราษฎร 3,4,5 ฉันเป็นหวัด 12-000 บาท")

out = subword_tokenize(text,engine="dict",keep_whitespace=True)
print(out)

out = "|".join(out)


def convert_num(match_obj):
    if match_obj.group(0) is not None:
        return match_obj.group(0).replace("|","") + "|"

text = out
numRegex = re.sub(r'([\d]\|)+',convert_num,text)

output = numRegex.replace("_","[!und:]").replace(" ","_")
print(output.split("|"))
