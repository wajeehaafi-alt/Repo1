# SEO Audit Workflow - Test Cases

## 🔧 Setup
Replace `YOUR_WEBHOOK_URL` with your actual n8n webhook URL:
```
http://your-n8n-server:5678/webhook/seo-audit
```

---

## ✅ TEST CASE 1: Happy Path - Complete Valid Input
**Purpose:** Test normal workflow execution with all required fields

```bash
curl -X POST "YOUR_WEBHOOK_URL" ^
  -H "Content-Type: application/json" ^
  -d "{\"target_url\": \"bfss.co.uk\", \"email\": \"test@example.com\", \"report_type\": \"onboarding\", \"location\": \"United Kingdom\"}"
```

**Expected Result:**
- ✅ Workflow executes successfully
- ✅ All DataForSEO API calls return data
- ✅ LLM generates comprehensive report
- ✅ Google Doc created
- ✅ Email sent to test@example.com

---

## ✅ TEST CASE 2: Minimal Input (Only Required Fields)
**Purpose:** Test with minimum required parameters

```bash
curl -X POST "YOUR_WEBHOOK_URL" ^
  -H "Content-Type: application/json" ^
  -d "{\"target_url\": \"example.com\", \"email\": \"minimal@test.com\"}"
```

**Expected Result:**
- ✅ Workflow uses defaults (report_type: "onboarding", location: "United Kingdom")
- ✅ Report generated successfully

---

## ✅ TEST CASE 3: URL with HTTPS prefix
**Purpose:** Test URL cleaning functionality

```bash
curl -X POST "YOUR_WEBHOOK_URL" ^
  -H "Content-Type: application/json" ^
  -d "{\"target_url\": \"https://www.searchhounds.com/\", \"email\": \"url-test@example.com\"}"
```

**Expected Result:**
- ✅ URL cleaned to: `www.searchhounds.com` (no https://, no trailing /)
- ✅ API calls work correctly

---

## ✅ TEST CASE 4: URL with HTTP prefix
**Purpose:** Test HTTP URL cleaning

```bash
curl -X POST "YOUR_WEBHOOK_URL" ^
  -H "Content-Type: application/json" ^
  -d "{\"target_url\": \"http://testsite.co.uk\", \"email\": \"http-test@example.com\"}"
```

**Expected Result:**
- ✅ URL cleaned to: `testsite.co.uk`

---

## ✅ TEST CASE 5: Different Location (USA)
**Purpose:** Test with different geographic location

```bash
curl -X POST "YOUR_WEBHOOK_URL" ^
  -H "Content-Type: application/json" ^
  -d "{\"target_url\": \"hubspot.com\", \"email\": \"usa-test@example.com\", \"location\": \"United States\"}"
```

**Expected Result:**
- ✅ DataForSEO APIs use US location data
- ✅ Report reflects US market context

---

## ✅ TEST CASE 6: Large Website (Many Pages)
**Purpose:** Test with a larger, well-established website

```bash
curl -X POST "YOUR_WEBHOOK_URL" ^
  -H "Content-Type: application/json" ^
  -d "{\"target_url\": \"moz.com\", \"email\": \"large-site@example.com\"}"
```

**Expected Result:**
- ✅ More keyword data returned
- ✅ Higher domain rank shown
- ✅ More backlinks data
- ✅ Comprehensive report generated

---

## ✅ TEST CASE 7: Small/New Website
**Purpose:** Test with a newer website with less data

```bash
curl -X POST "YOUR_WEBHOOK_URL" ^
  -H "Content-Type: application/json" ^
  -d "{\"target_url\": \"small-business-example.co.uk\", \"email\": \"small-site@example.com\"}"
```

**Expected Result:**
- ✅ Handles limited data gracefully
- ✅ Report acknowledges limited history
- ✅ No errors even with sparse data

---

## ✅ TEST CASE 8: E-commerce Website
**Purpose:** Test with different industry type

```bash
curl -X POST "YOUR_WEBHOOK_URL" ^
  -H "Content-Type: application/json" ^
  -d "{\"target_url\": \"asos.com\", \"email\": \"ecommerce@example.com\", \"location\": \"United Kingdom\"}"
```

**Expected Result:**
- ✅ Report reflects e-commerce context
- ✅ Keywords show commercial intent

---

## ❌ TEST CASE 9: Missing Required Field (No URL)
**Purpose:** Test error handling for missing target_url

```bash
curl -X POST "YOUR_WEBHOOK_URL" ^
  -H "Content-Type: application/json" ^
  -d "{\"email\": \"no-url@example.com\", \"report_type\": \"onboarding\"}"
```

**Expected Result:**
- ❌ Workflow fails with error
- ❌ Error message: "target_url is required"

---

## ❌ TEST CASE 10: Missing Email
**Purpose:** Test behavior when email is not provided

```bash
curl -X POST "YOUR_WEBHOOK_URL" ^
  -H "Content-Type: application/json" ^
  -d "{\"target_url\": \"test.com\"}"
```

**Expected Result:**
- ⚠️ Either uses default email OR fails gracefully
- Check how Send Email node handles missing email

---

## ❌ TEST CASE 11: Invalid URL Format
**Purpose:** Test with malformed URL

```bash
curl -X POST "YOUR_WEBHOOK_URL" ^
  -H "Content-Type: application/json" ^
  -d "{\"target_url\": \"not a valid url!!!\", \"email\": \"invalid@example.com\"}"
```

**Expected Result:**
- ❌ DataForSEO APIs return error
- ❌ Workflow handles error gracefully

---

## ❌ TEST CASE 12: Non-existent Domain
**Purpose:** Test with domain that doesn't exist

```bash
curl -X POST "YOUR_WEBHOOK_URL" ^
  -H "Content-Type: application/json" ^
  -d "{\"target_url\": \"thisdomaindoesnotexist12345xyz.com\", \"email\": \"nonexistent@example.com\"}"
```

**Expected Result:**
- ⚠️ DataForSEO returns empty/null data
- ⚠️ LLM handles missing data gracefully
- ⚠️ Report indicates insufficient data

---

## ✅ TEST CASE 13: Empty Request Body
**Purpose:** Test completely empty input

```bash
curl -X POST "YOUR_WEBHOOK_URL" ^
  -H "Content-Type: application/json" ^
  -d "{}"
```

**Expected Result:**
- ❌ Error: "target_url is required"

---

## ✅ TEST CASE 14: Report Type - Update
**Purpose:** Test update report type (if implemented)

```bash
curl -X POST "YOUR_WEBHOOK_URL" ^
  -H "Content-Type: application/json" ^
  -d "{\"target_url\": \"bfss.co.uk\", \"email\": \"update@example.com\", \"report_type\": \"update\"}"
```

**Expected Result:**
- ✅ is_update flag set to true
- ✅ Different report template used (if applicable)

---

## ✅ TEST CASE 15: Special Characters in Email
**Purpose:** Test email with special but valid characters

```bash
curl -X POST "YOUR_WEBHOOK_URL" ^
  -H "Content-Type: application/json" ^
  -d "{\"target_url\": \"test.com\", \"email\": \"user+seo@example.com\"}"
```

**Expected Result:**
- ✅ Email handled correctly
- ✅ Email sent to user+seo@example.com

---

## ✅ TEST CASE 16: Subdomain URL
**Purpose:** Test with subdomain

```bash
curl -X POST "YOUR_WEBHOOK_URL" ^
  -H "Content-Type: application/json" ^
  -d "{\"target_url\": \"blog.hubspot.com\", \"email\": \"subdomain@example.com\"}"
```

**Expected Result:**
- ✅ Subdomain analyzed separately
- ✅ Data reflects subdomain metrics

---

## ✅ TEST CASE 17: Multiple Emails (if supported)
**Purpose:** Test sending to multiple recipients

```bash
curl -X POST "YOUR_WEBHOOK_URL" ^
  -H "Content-Type: application/json" ^
  -d "{\"target_url\": \"test.com\", \"email\": \"user1@example.com, user2@example.com\"}"
```

**Expected Result:**
- Check if multiple emails supported
- Either sends to both OR uses first email

---

## ✅ TEST CASE 18: Company Name Field
**Purpose:** Test with company name for personalization

```bash
curl -X POST "YOUR_WEBHOOK_URL" ^
  -H "Content-Type: application/json" ^
  -d "{\"target_url\": \"bfss.co.uk\", \"email\": \"company@example.com\", \"company_name\": \"BFSS Security Ltd\"}"
```

**Expected Result:**
- ✅ Company name used in report personalization
- ✅ Email subject includes company name

---

## ✅ TEST CASE 19: Very Long URL
**Purpose:** Test URL length handling

```bash
curl -X POST "YOUR_WEBHOOK_URL" ^
  -H "Content-Type: application/json" ^
  -d "{\"target_url\": \"verylongdomainname-with-many-hyphens-and-words.co.uk\", \"email\": \"long@example.com\"}"
```

**Expected Result:**
- ✅ URL handled without truncation
- ✅ Workflow processes normally

---

## ✅ TEST CASE 20: Concurrent Requests
**Purpose:** Test workflow under load (run in separate terminals)

**Terminal 1:**
```bash
curl -X POST "YOUR_WEBHOOK_URL" -H "Content-Type: application/json" -d "{\"target_url\": \"site1.com\", \"email\": \"test1@example.com\"}"
```

**Terminal 2:**
```bash
curl -X POST "YOUR_WEBHOOK_URL" -H "Content-Type: application/json" -d "{\"target_url\": \"site2.com\", \"email\": \"test2@example.com\"}"
```

**Expected Result:**
- ✅ Both workflows execute independently
- ✅ No data mixing between requests
- ✅ Both emails sent correctly

---

## 📊 Test Results Template

| Test Case | Description | Status | Notes |
|-----------|-------------|--------|-------|
| TC1 | Happy Path | ⬜ | |
| TC2 | Minimal Input | ⬜ | |
| TC3 | HTTPS URL | ⬜ | |
| TC4 | HTTP URL | ⬜ | |
| TC5 | USA Location | ⬜ | |
| TC6 | Large Website | ⬜ | |
| TC7 | Small Website | ⬜ | |
| TC8 | E-commerce | ⬜ | |
| TC9 | Missing URL | ⬜ | |
| TC10 | Missing Email | ⬜ | |
| TC11 | Invalid URL | ⬜ | |
| TC12 | Non-existent Domain | ⬜ | |
| TC13 | Empty Body | ⬜ | |
| TC14 | Update Report | ⬜ | |
| TC15 | Special Email | ⬜ | |
| TC16 | Subdomain | ⬜ | |
| TC17 | Multiple Emails | ⬜ | |
| TC18 | Company Name | ⬜ | |
| TC19 | Long URL | ⬜ | |
| TC20 | Concurrent | ⬜ | |

**Status Legend:** ✅ Pass | ❌ Fail | ⬜ Not Tested | ⚠️ Partial

---

## 🔍 What to Check for Each Test

### 1. Validate Input Node
- [ ] URL cleaned correctly (no https://, no trailing /)
- [ ] Email captured
- [ ] Defaults applied for missing fields

### 2. DataForSEO API Calls
- [ ] OnPage Task Post returns task_id
- [ ] Domain Rank Overview returns data
- [ ] Ranked Keywords returns keyword list
- [ ] Backlinks Summary returns backlink data

### 3. Wait for OnPage Analysis
- [ ] Sufficient wait time (5 minutes)
- [ ] OnPage Summary returns crawled pages > 0

### 4. Parse Nodes
- [ ] All 4 parse nodes output structured data
- [ ] No null/undefined errors

### 5. Merge Nodes
- [ ] All 4 data sources combined
- [ ] 4 items visible after Merge2

### 6. Aggregate Data
- [ ] Single object with onPage, domainRank, keywords, backlinks

### 7. Generate Prompt
- [ ] systemPrompt and userPrompt generated
- [ ] Contains actual data from analysis

### 8. LLM (GPT-4.1 mini)
- [ ] Response contains complete report
- [ ] Uses actual data (not placeholders)
- [ ] Professional tone

### 9. Clean Text
- [ ] Emojis removed (if configured)
- [ ] Format preserved

### 10. Create Document
- [ ] Google Doc created successfully
- [ ] Returns docId and webViewLink

### 11. Add Text
- [ ] Content added to Google Doc
- [ ] Formatting preserved

### 12. Send Email
- [ ] Email sent successfully
- [ ] Contains Google Doc link
- [ ] Sent to correct recipient

---

## 🚀 Quick Test Script (PowerShell)

Save this as `run_tests.ps1`:

```powershell
$webhook = "YOUR_WEBHOOK_URL"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  SEO Audit Workflow Test Suite" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# Test 1: Happy Path
Write-Host "`nTest 1: Happy Path..." -ForegroundColor Yellow
$body1 = @{
    target_url = "bfss.co.uk"
    email = "test@example.com"
    report_type = "onboarding"
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri $webhook -Method Post -Body $body1 -ContentType "application/json"
    Write-Host "✅ Test 1 PASSED" -ForegroundColor Green
} catch {
    Write-Host "❌ Test 1 FAILED: $_" -ForegroundColor Red
}

# Test 2: Missing URL (should fail)
Write-Host "`nTest 2: Missing URL (expecting error)..." -ForegroundColor Yellow
$body2 = @{
    email = "test@example.com"
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri $webhook -Method Post -Body $body2 -ContentType "application/json"
    Write-Host "❌ Test 2 FAILED - Should have thrown error" -ForegroundColor Red
} catch {
    Write-Host "✅ Test 2 PASSED - Error caught as expected" -ForegroundColor Green
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Tests Complete!" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
```

---

## 📝 Notes

1. **DataForSEO Credits:** Each test consumes API credits. Use test mode or budget accordingly.
2. **Email Testing:** Use a test email address to avoid spam.
3. **Wait Times:** OnPage analysis takes 5+ minutes. Be patient.
4. **Google Drive:** Check your ProgrammX folder for created documents.
5. **Error Logs:** Check n8n execution history for detailed error info.

