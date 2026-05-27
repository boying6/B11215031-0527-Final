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

1. AI 在撰寫過程中有出錯，主要是前幾次版本還停留在舊的 `lib_data.txt` 與 `@@`、`##` 儲存方式，沒有完全切換成 `books.json`。另外，`borrow` 功能一開始也沒有在找不到 ISBN 時印出 `Book Not Found`。

2. 發現的問題：
   - 儲存格式還是舊的文字檔格式，和題目要求不一致。
   - `borrow` 找不到對應 ISBN 時沒有提示，使用者不知道是否操作成功。
   - 後來再補強時，`load_books()` 對 JSON 格式錯誤的處理還不夠明確。

3. 修正的對話：
   - 我告訴它「請繼續重構 modern_library.py，把原本使用 lib_data.txt 與 @@、## 分隔的儲存方式，改成使用 books.json 儲存資料。」
   - 接著我補充「請加強 modern_library.py 的錯誤處理與輸入驗證，讀取 books.json 時若檔案不存在就回傳空清單；若 JSON 格式錯誤要提示並回傳空清單；borrow 找不到 ISBN 要印出 Book Not Found。」

---

## 三、 成果驗證與測試  (共2小題，每小題10分，總共20分)

確保你的 `modern_library.py` 功能正確。

### 3.1 測試結果驗證 (Terminal)

請貼上執行程式並輸入 show 後，顯示資料清單。(請從呼叫執行程式到結束程式完整的把操作對話複製到下框)

```log
PS C:\Users\pclab\Desktop\B11215031_李柏穎\NTUST-0527-Final-master> python modern_library.py
=== 圖書管理系統 v0.1 (Modern) ===
> add 深入淺出Python/978001/available
Success
> add 資料結構理論/978002/available
Success
> add 演算法實作/978003/available
Success
> add 重複測試書/978001/available
ISBN Exist
> borrow 978002
Updated
> show      
書名: 深入淺出Python, ISBN: 978001, 狀態: available
書名: 資料結構理論, ISBN: 978002, 狀態: borrowed
書名: 演算法實作, ISBN: 978003, 狀態: available
> exit
系統關閉
```

### 3.2 產出的資料檔案格式

請貼上重構後生成的 `books.json` 前幾行內容：

```json
[
  {
    "title": "深入淺出Python",
    "isbn": "978001",
    "status": "available"
  },
  {
    "title": "資料結構理論",
    "isbn": "978002",
    "status": "borrowed"
  },
  {
    "title": "演算法實作",
    "isbn": "978003",
    "status": "available"
  }
]
```

---

## 四、 Git 提交紀錄 (Commit History)  (共2小題，總共13分)

### 4.1. 請執行 `git log --oneline` 並將 Commit 紀錄貼在此處，以證明你的開發流程(此小題6分)


```log
ed60201 (HEAD -> master, origin/master) Add test results and books json
7f14146 Finish modern_library.py
8c3cc73 Create modern_library.py
```

### 4.2. GitHub Repository 連結(此小題7分)

將專案推送到 GitHub (Public) 若提交到 Private 連結不給分。 請設定 Repository 名稱為 `學號-0527-Final` Ex: B11526748-0527-Final **請用 - 不是 _**

```log
https://github.com/boying6/B11215031-0527-Final
```

希望這兩份 Markdown 格式能幫你省下不少排版時間！祝你的考試順利舉行！

最後請保留整份專案資料夾歐！
