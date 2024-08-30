import os
from dotenv import load_dotenv

# .envを環境変数として読み込む
# .envが存在しない場合でもエラーにはならない
load_dotenv(override=True)

print(os.environ.get("PWD"))
# print(os.environ["SECRET"])  # 存在しなかった場合はKeyErrorになる
print(os.environ.get("SECRET"))  # 存在しなかった場合はNoneが取得される