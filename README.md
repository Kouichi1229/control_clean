# 專利名稱資料清理工具

這是一個以 Python、Pandas 與 Streamlit 製作的名稱資料清理工具，主要處理專利資料中的申請人／權利人名稱及發明人名稱等文字欄位。

工具讓使用者選擇待清理欄位、統計方式與名稱正規化規則，再將正規化後的名稱映射回原始名稱，協助整理因公司組織型態、標點、括號、國家名稱或拼寫差異而產生的重複資料。

## 主要功能

- 支援 CSV 與 XLSX 檔案讀取。
- 讓使用者選擇待清理的欄位。
- 可選擇是否依「核准專利數」排序，或依名稱彙總筆數。
- 使用 Unicode NFKD 正規化並轉為 ASCII，降低部分字元差異。
- 可選擇移除公司組織型態、有限合夥型態、機構單位、國家名稱、常見錯字及 HTML entity 等詞彙。
- 可選擇截取逗號前字串、移除括號內容、標點符號、數字及空格。
- 將正規化名稱建立成字典，映射回原始名稱，產生清理後欄位。
- CSV 流程提供結果下載。

## 技術組成

| 技術 | 用途 |
|---|---|
| Python | 主要開發語言 |
| Streamlit | 互動式資料清理介面 |
| Pandas | CSV／Excel 讀取、分組、排序、清理及映射 |
| Unicode NFKD | 名稱字元正規化 |
| Dictionary | 以正規化名稱映射回原始名稱 |
| OpenPyXL | Excel 讀取支援 |
| XlsxWriter | Excel 輸出輔助函式所使用的引擎 |

## 資料處理流程

1. 上傳 CSV 或 Excel 檔案。
2. 選擇要清理的欄位。
3. 選擇是否使用核准專利數排序，或先彙總相同名稱。
4. 將名稱進行 Unicode 正規化與字元轉換。
5. 依使用者選擇套用公司型態、機構、國家、錯字及其他文字清理規則。
6. 視需要移除括號內容、符號、數字及空格。
7. 對正規化後的空字串回填原始名稱，避免清理規則將整個名稱移除。
8. 建立正規化名稱到原始名稱的字典，產生清理後欄位。
9. CSV 流程提供下載結果。

## 專案檔案

| 檔案 | 說明 |
|---|---|
| `app.py` | Streamlit 主介面與 CSV／Excel 資料處理流程 |
| `TAKE_OUT_TYPE.py` | 公司型態、機構、國家、發明人名稱及錯字規則 |
| `action.py` | CSV 轉換、Excel 輸出輔助函式及介面選項 |
| `Company_take_out_Words.py` | 另一份公司組織型態分類清單 |
| `Disrance_algorithm.py` | Levenshtein distance／ratio 演算法實驗程式 |
| `BeforeTestCode.py` | 前期測試程式 |
| `requirements.txt` | Python 套件清單 |

## 實作範圍與注意事項

- CSV 流程可確認包含清理、字典映射及 CSV 下載。
- Excel 流程可確認包含讀取、欄位選擇、名稱正規化及清理結果顯示；目前程式末段未看到與 CSV 相同的下載流程。
- 目前主要名稱映射使用正規化字典與精確查找，不是以 Levenshtein 或 Jaro-Winkler 執行模糊比對。
- `Disrance_algorithm.py` 定義 Levenshtein distance／ratio 函式，但目前主程式沒有呼叫它。
- `action.py` 有 Excel 輸出函式，但目前主程式沒有呼叫該函式。
- 本文件依照版本庫中的程式進行靜態整理，沒有宣稱目前環境已重新部署或完成端到端測試。

## 技術回顧

開發脈絡、能力盤點、設計取捨與程式限制請參閱 [PROJECT_RETROSPECTIVE.md](PROJECT_RETROSPECTIVE.md)。
