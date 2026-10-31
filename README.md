# Apna Git khud banao 🔥 (build-your-own-x)

Git har file ko ek **blob** ki tarah store karta hai. Uska ID (hash) aise banta hai:

```
SHA-1( "blob " + size + "\0" + content )
```

Ye repo 7 lines ke Python code se wahi hash banata hai jo asli Git banata hai.

## Run karo

```bash
python git_hash.py
# ce013625030ba8dba906f756967f9e9ca394464a
```

Asli Git se check karo:

```bash
echo hello | git hash-object --stdin
# ce013625030ba8dba906f756967f9e9ca394464a  (same!)
```

Ab `"hello\n"` ko `"hello!\n"` karo: poora hash badal jayega (4effa19f…). Isi tarah Git har chhota change pakad leta hai.

💻 Browser mein chalao (free editor): https://techbroz-code.sites.tab.bot/#l=python&c=ZnJvbSBoYXNobGliIGltcG9ydCBzaGExCgpkZWYgZ2l0X2hhc2godGV4dCk6CiAgICBkYXRhID0gdGV4dC5lbmNvZGUoKQogICAgaGVhZCA9IGYiYmxvYiB7bGVuKGRhdGEpfVwwIgogICAgZnVsbCA9IGhlYWQuZW5jb2RlKCkgKyBkYXRhCiAgICByZXR1cm4gc2hhMShmdWxsKS5oZXhkaWdlc3QoKQoKcHJpbnQoZ2l0X2hhc2goImhlbGxvXG4iKSkK

📚 Full tutorial: https://github.com/codecrafters-io/build-your-own-x#build-your-own-git

🎬 YouTube video: https://www.youtube.com/shorts/aNwJ96VqTqA

Made by Tech Bro Z — YouTube @techbrozdeveloper, Instagram @tech_bro_z_1
