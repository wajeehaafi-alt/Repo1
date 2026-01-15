# How to Add a Test Data Node in n8n

## Step-by-Step Instructions

### Step 1: Add a New Code Node
1. Right-click on the canvas between **Merge2** and **Aggregate Data**
2. Click **Add node**
3. Search for **"Code"** and select it
4. Name it **"Test Data"** or **"Mock Data"**

### Step 2: Configure the Code Node
1. Click on the new Code node to open it
2. Set **Mode** to: `Run Once for All Items`
3. Delete the default code and paste the code below

### Step 3: Connect the Nodes
1. **Disconnect** the connection from Merge2 → Aggregate Data
2. **Connect** Merge2 → Test Data (optional, or leave it disconnected for pure testing)
3. **Connect** Test Data → Aggregate Data

### Step 4: Toggle Between Test/Production
- **For Testing:** Disable the Merge2 → Test Data connection, just use Test Data → Aggregate Data
- **For Production:** Disable Test Data node and reconnect Merge2 → Aggregate Data

---

## Code for Test Data Node

Paste this JavaScript code into the Code node:

```javascript
// Test Data Node - Mock API responses for testing
// This bypasses the API calls and provides static data

const testData = [
  {
    "success": true,
    "status": "complete",
    "onPage": {
      "crawlProgress": "in_progress",
      "pagesCrawled": 0,
      "pagesInQueue": 0,
      "issues": {
        "critical": 0,
        "warnings": 0,
        "notices": 0
      },
      "pageMetrics": {
        "brokenLinks": 14,
        "brokenResources": 0,
        "duplicateTitle": 0,
        "duplicateDescription": 0,
        "duplicateContent": 0
      },
      "performance": {
        "avgPageLoadTime": 0,
        "https": 0,
        "mobileUsability": false
      }
    }
  },
  {
    "success": true,
    "domainRank": {
      "target": "www.croydonathletic.com",
      "location": 2826,
      "language": "en",
      "dateFrom": "2025-10-01",
      "dateTo": "2026-01-07",
      "dataPoints": 3,
      "positions": {
        "top3": 7,
        "top10": 27,
        "page2": 15,
        "page3": 16,
        "page4Plus": 60
      },
      "estimatedTrafficValue": 3818,
      "totalKeywords": 118,
      "periodChanges": {
        "keywordsChange": -8,
        "trafficValueChange": 1910,
        "keywordsStart": 126,
        "keywordsEnd": 118,
        "trafficStart": 1908,
        "trafficEnd": 3818
      },
      "movement": {
        "newKeywords": 37,
        "improved": 22,
        "declined": 49,
        "lost": 40
      }
    }
  },
  {
    "success": true,
    "keywords": {
      "summary": {
        "totalKeywords": 118,
        "totalSearchVolume": 57870,
        "totalETV": 3818.05,
        "brandedCount": 0,
        "unbrandedCount": 118,
        "brandedPercent": 0,
        "unbrandedPercent": 100
      },
      "distribution": {
        "top3Count": 6,
        "top10Count": 23,
        "page2Count": 12,
        "page3Count": 18,
        "deepCount": 65
      },
      "topPerformers": [
        {
          "keyword": "afc croydon athletic",
          "rank": 1,
          "searchVolume": 4400,
          "etv": 1337.6,
          "cpc": 1.2,
          "difficulty": 3,
          "intent": "navigational",
          "url": "https://www.croydonathletic.com/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "croydon athletic",
          "rank": 1,
          "searchVolume": 4400,
          "etv": 1337.6,
          "cpc": 1.2,
          "difficulty": 8,
          "intent": "navigational",
          "url": "https://www.croydonathletic.com/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "croydon athletic fc",
          "rank": 1,
          "searchVolume": 320,
          "etv": 97.28,
          "cpc": 0,
          "difficulty": 1,
          "intent": "navigational",
          "url": "https://www.croydonathletic.com/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "afc croydon",
          "rank": 2,
          "searchVolume": 4400,
          "etv": 712.8,
          "cpc": 1.2,
          "difficulty": 0,
          "intent": "informational",
          "url": "https://www.croydonathletic.com/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "croydon athletic football club",
          "rank": 2,
          "searchVolume": 320,
          "etv": 51.84,
          "cpc": 0,
          "difficulty": 2,
          "intent": "navigational",
          "url": "https://www.croydonathletic.com/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "croydon athletics",
          "rank": 2,
          "searchVolume": 210,
          "etv": 34.02,
          "cpc": 0,
          "difficulty": 13,
          "intent": "navigational",
          "url": "https://www.croydonathletic.com/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "afc croydon athletic twitter",
          "rank": 4,
          "searchVolume": 90,
          "etv": 8.76,
          "cpc": 0,
          "difficulty": 5,
          "intent": "navigational",
          "url": "https://www.croydonathletic.com/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "croydon football club fixtures",
          "rank": 4,
          "searchVolume": 140,
          "etv": 9.23,
          "cpc": 0,
          "difficulty": 0,
          "intent": "informational",
          "url": "https://www.croydonathletic.com/fixtures-results/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "preston kedwell",
          "rank": 4,
          "searchVolume": 90,
          "etv": 5.93,
          "cpc": 0,
          "difficulty": 0,
          "intent": "commercial",
          "url": "https://www.croydonathletic.com/preston-kedwell-joins-on-loan/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "the mayfield stadium",
          "rank": 4,
          "searchVolume": 50,
          "etv": 3.3,
          "cpc": 0,
          "difficulty": 0,
          "intent": "informational",
          "url": "https://www.croydonathletic.com/",
          "isBranded": false,
          "isNew": true
        }
      ],
      "quickWinOpportunities": [
        {
          "keyword": "croydon football",
          "rank": 20,
          "searchVolume": 2400,
          "etv": 14.16,
          "cpc": 1.2,
          "difficulty": 0,
          "intent": "informational",
          "url": "https://www.croydonathletic.com/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "charlie colkett",
          "rank": 11,
          "searchVolume": 880,
          "etv": 9.94,
          "cpc": 0,
          "difficulty": 0,
          "intent": "commercial",
          "url": "https://www.croydonathletic.com/charlie-colkett-signs-for-croydon-athletic/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "nya kirby",
          "rank": 17,
          "searchVolume": 590,
          "etv": 4.43,
          "cpc": 0,
          "difficulty": 0,
          "intent": "commercial",
          "url": "https://www.croydonathletic.com/player/nya-kirby/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "football teams croydon",
          "rank": 11,
          "searchVolume": 320,
          "etv": 4.8,
          "cpc": 1.55,
          "difficulty": 6,
          "intent": "informational",
          "url": "https://www.croydonathletic.com/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "football team in croydon",
          "rank": 14,
          "searchVolume": 320,
          "etv": 6.3,
          "cpc": 1.55,
          "difficulty": 1,
          "intent": "informational",
          "url": "https://www.croydonathletic.com/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "mayfield stadium",
          "rank": 14,
          "searchVolume": 140,
          "etv": 1.58,
          "cpc": 0,
          "difficulty": 0,
          "intent": "informational",
          "url": "https://www.croydonathletic.com/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "cian mccarthy",
          "rank": 15,
          "searchVolume": 110,
          "etv": 0.82,
          "cpc": 0,
          "difficulty": 0,
          "intent": "informational",
          "url": "https://www.croydonathletic.com/player/cian-mccarthy/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "jermaine mcglashan",
          "rank": 19,
          "searchVolume": 110,
          "etv": 0.47,
          "cpc": 0,
          "difficulty": 0,
          "intent": "informational",
          "url": "https://www.croydonathletic.com/jermaine-mcglashan-steps-down-as-manager/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "croydon football academy",
          "rank": 17,
          "searchVolume": 90,
          "etv": 0.5,
          "cpc": 1.72,
          "difficulty": 0,
          "intent": "navigational",
          "url": "https://www.croydonathletic.com/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "ibby akanbi",
          "rank": 13,
          "searchVolume": 70,
          "etv": 0.64,
          "cpc": 0,
          "difficulty": 0,
          "intent": "transactional",
          "url": "https://www.croydonathletic.com/club-news-new-signing-ibby-akanbi-joins-the-rams/",
          "isBranded": false,
          "isNew": false
        }
      ],
      "allKeywords": [
        {
          "keyword": "afc croydon athletic",
          "rank": 1,
          "searchVolume": 4400,
          "etv": 1337.6,
          "cpc": 1.2,
          "difficulty": 3,
          "intent": "navigational",
          "url": "https://www.croydonathletic.com/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "croydon athletic",
          "rank": 1,
          "searchVolume": 4400,
          "etv": 1337.6,
          "cpc": 1.2,
          "difficulty": 8,
          "intent": "navigational",
          "url": "https://www.croydonathletic.com/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "croydon athletic fc",
          "rank": 1,
          "searchVolume": 320,
          "etv": 97.28,
          "cpc": 0,
          "difficulty": 1,
          "intent": "navigational",
          "url": "https://www.croydonathletic.com/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "afc croydon",
          "rank": 2,
          "searchVolume": 4400,
          "etv": 712.8,
          "cpc": 1.2,
          "difficulty": 0,
          "intent": "informational",
          "url": "https://www.croydonathletic.com/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "croydon athletic football club",
          "rank": 2,
          "searchVolume": 320,
          "etv": 51.84,
          "cpc": 0,
          "difficulty": 2,
          "intent": "navigational",
          "url": "https://www.croydonathletic.com/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "croydon athletics",
          "rank": 2,
          "searchVolume": 210,
          "etv": 34.02,
          "cpc": 0,
          "difficulty": 13,
          "intent": "navigational",
          "url": "https://www.croydonathletic.com/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "afc croydon athletic twitter",
          "rank": 4,
          "searchVolume": 90,
          "etv": 8.76,
          "cpc": 0,
          "difficulty": 5,
          "intent": "navigational",
          "url": "https://www.croydonathletic.com/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "croydon football club fixtures",
          "rank": 4,
          "searchVolume": 140,
          "etv": 9.23,
          "cpc": 0,
          "difficulty": 0,
          "intent": "informational",
          "url": "https://www.croydonathletic.com/fixtures-results/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "preston kedwell",
          "rank": 4,
          "searchVolume": 90,
          "etv": 5.93,
          "cpc": 0,
          "difficulty": 0,
          "intent": "commercial",
          "url": "https://www.croydonathletic.com/preston-kedwell-joins-on-loan/",
          "isBranded": false,
          "isNew": false
        },
        {
          "keyword": "the mayfield stadium",
          "rank": 4,
          "searchVolume": 50,
          "etv": 3.3,
          "cpc": 0,
          "difficulty": 0,
          "intent": "informational",
          "url": "https://www.croydonathletic.com/",
          "isBranded": false,
          "isNew": true
        }
      ]
    }
  },
  {
    "success": true,
    "backlinks": {
      "dateFrom": "N/A",
      "dateTo": "N/A",
      "dataPoints": 0,
      "totalBacklinks": 0,
      "referringDomains": 0,
      "rank": 0,
      "periodChanges": {
        "backlinksChange": 0,
        "domainsChange": 0,
        "backlinksStart": 0,
        "backlinksEnd": 0,
        "domainsStart": 0,
        "domainsEnd": 0
      }
    }
  }
];

// Return each item as a separate output item
return testData.map(item => ({ json: item }));
```

---

## Visual Workflow Setup

```
                                    ┌─────────────┐
                                    │  Test Data  │ (for testing)
                                    │   (Code)    │
                                    └──────┬──────┘
                                           │
┌─────────┐                                │
│ Merge2  │ ───────────────────────────────┼───────> [Aggregate Data]
└─────────┘                                │
     │                                     │
     └─────────── (disable for testing) ───┘
```

---

## Quick Toggle Method

### Option A: Use a Switch
Add an **IF** node after Merge2:
- Condition: Check for a test flag in the webhook payload
- True branch → Test Data node
- False branch → Aggregate Data directly

### Option B: Disable Nodes
1. **For Testing:** 
   - Right-click on all API nodes (OnPage, Domain Rank, Keywords, Backlinks) 
   - Click "Disable"
   - Enable only: Webhook → Validate Input → Test Data → Aggregate Data → onwards

2. **For Production:**
   - Disable Test Data node
   - Enable all API nodes

---

## Alternative: Use "Edit Fields (Set)" Node

If you prefer a simpler approach:

1. Add **Edit Fields (Set)** node
2. Switch to **JSON** mode
3. Paste the test data array directly
4. This works but Code node gives more flexibility

---

## Pro Tip: Add Test Mode to Webhook

You can also modify your **Validate Input** node to check for a `test_mode` parameter:

```javascript
// Add this at the end of Validate Input node
const testMode = $input.first().json.test_mode || $input.first().json.body?.test_mode || false;

return {
  json: {
    // ... existing fields ...
    test_mode: testMode
  }
};
```

Then use an **IF** node to route:
- `test_mode = true` → Test Data node
- `test_mode = false` → Continue with API calls

