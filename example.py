#from pythainlp.tokenize import subword_tokenize
import re 


text = ("พระราชบัญญัติธรรมนูญการปกครองแผ่นดินสยามชั่วคราว พุทธศักราช ๒๔๗๕ "
        "เป็นรัฐธรรมนูญฉบับชั่วคราว ซึ่งถือว่าเป็นรัฐธรรมนูญฉบับแรกแห่งราชอาณาจักรสยาม "
        "ประกาศใช้เมื่อวันที่ 27 มิถุนายน พ.ศ. 2475 Mancity 20:43 "
        "โดยเป็นผลพวงหลังการปฏิวัติเมื่อวันที่ 24 มิถุนายน พ.ศ. 2475 โดยคณะราษฎร")

out = subword_tokenize(text,engine="dict",keep_whitespace=True)
print(out)


def convert_num(match_obj):
    print("MATCH",match_obj.group(0))
    if match_obj.group(0) is not None:
        return match_obj.group(0).replace("|","") + "|"

text = "a|b|c|1|.|2|2|e|1|2|"
numRegex = re.sub(r'([\d.]\|)+',convert_num,text)
print(numRegex)

