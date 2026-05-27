# 台科大資管 Python 考試作答區

---

## 基本資料

**學號：** B11215031  
**系級：** 資工系大三  
**姓名：** 李柏穎  

---

## 一、 原始碼分析報告 (Static Analysis) (共8小題，每小題3分，總共24分)

### 1.1 變數與邏輯對照表

| 原始變數名稱 | 代表意義 (Business Logic) | 建議修正名稱 |
|---|---|---|
| Q1 l1 (in load_proc) | 從檔案讀出來的每一行資料清單 | lines |
| Q2 d2 (in main) | 儲存所有書籍資料的清單，每筆資料是一個 dict | book_list |
| Q3 c_res (in check) | 檢查某個 ISBN 是否已經存在 | is_isbn_exists |

### 1.2 壞味道 (Code Smells) 診斷

請列出原程式碼中至少 5 個嚴重的設計問題，並說明為什麼不好：

- **Q1：** 變數命名不清楚，例如 d2、l1、p、p2，看不出實際用途，降低可讀性。
- **Q2：** 資料格式依賴 @@、##、/ 分隔，若資料本身包含這些符號，可能解析錯誤。
- **Q3：** 讀檔時沒有檢查格式，若檔案內容錯誤，可能造成 IndexError。
- **Q4：** borrow 找不到 ISBN 時沒有提示，使用者不知道操作失敗。
- **Q5：** 新增書籍時沒有驗證狀態，可能輸入不合理的狀態資料。

---

## 二、 Vibe-Coding 協作紀錄 (共6小題，每小題3分，總共18分)

請記錄你如何引導 GitHub Copilot 進行重構。
重構的要求，請根據題目卷以及你發現的 Code Smells 來進行。

### 2.1 關鍵 Prompt 紀錄

請貼出你對 AI 下達過最有效的 3 個 Prompt：

```log
Prompt A：
請根據 legacy_lib.py 的功能，建立一個新的 modern_library.py。請保留原本的指令介面：add 書名/ISBN/狀態、show、borrow ISBN、exit。請將原本不清楚的變數命名改成清楚名稱，並把主要功能拆成多個函式。請輸出完整的 modern_library.py 程式碼。

Prompt B： 請繼續重構 modern_library.py，把原本使用 lib_data.txt 與 @@、## 分隔的儲存方式，改成使用 books.json 儲存資料。資料格式請使用 list of dict，每本書包含 title、isbn、status 三個欄位。請加入 load_books() 與 save_books() 函式，並輸出完整程式碼。

Prompt C：
請加強 modern_library.py 的錯誤處理與輸入驗證。要求如下：讀取 books.json 時若檔案不存在就回傳空清單；若 JSON 格式錯誤要提示並回傳空清單；add 指令格式錯誤要印出 Format Error；ISBN 重複要印出 ISBN Exist；status 只能是 available 或 borrowed；borrow 找不到 ISBN 要印出 Book Not Found；exit 時才儲存檔案。請保持程式碼適合初學者閱讀，並輸出完整程式碼。
```

### 2.2 AI 錯誤處理

1. AI 在撰寫過程中是否有出錯？（例如：漏寫了某個功能、語法錯誤）你是如何發現並請它修正的？

2. 發現的問題： (範例：AI 漏掉了 exit 時要印出分類統計的功能)

3. 修正的對話： (範例：我告訴它「請在結束前迴圈遍歷 JSON 資料並計算分類總額」)

---

## 三、 成果驗證與測試  (共2小題，每小題10分，總共20分)

確保你的 `modern_library.py` 功能正確。

### 3.1 測試結果驗證 (Terminal)

請貼上執行程式並輸入 show 後，顯示資料清單。(請從呼叫執行程式到結束程式完整的把操作對話複製到下框)

```log

```

### 3.2 產出的資料檔案格式

請貼上重構後生成的 `books.json` 前幾行內容：

```json
[
  {
    "title": "XXX",
    "isbn": "XXX",
    "status": "XXX"
  }
]
```

---

## 四、 Git 提交紀錄 (Commit History)  (共2小題，總共13分)

### 4.1. 請執行 `git log --oneline` 並將 Commit 紀錄貼在此處，以證明你的開發流程(此小題6分)


```log
# 請在此處貼上 git log 內容
```

### 4.2. GitHub Repository 連結(此小題7分)

將專案推送到 GitHub (Public) 若提交到 Private 連結不給分。 請設定 Repository 名稱為 `學號-0527-Final` Ex: B11526748-0527-Final **請用 - 不是 _**

```log
# 請貼上你的 Repo 網址
```

希望這兩份 Markdown 格式能幫你省下不少排版時間！祝你的考試順利舉行！

最後請保留整份專案資料夾歐！
