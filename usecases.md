# AI Use Cases in Software Engineering & Support

## 10 Distinct AI Use Cases

| # | Use Case | Capability | Concrete Input $\rightarrow$ Concrete Output |
| :--- | :--- | :--- | :--- |
| **1** | **Customer Tone De-escalator** | Text / Extraction | **Input:** Profanity-laced user complaint message ("YOUR APP CHARGED ME TWICE I WANT A REFUND NOW!!!") <br> **Output:** JSON object: `{"sentiment": "furious", "core_issue": "double billed", "suggested_reply": "I sincerely apologize for the billing error. I have initiated a refund..."}` |

| **2** | **Automated Unit Test Generation** | Code Generation | **Input:** `user_auth.py` source file containing a login function. <br> **Output:** `test_user_auth.py` file containing 15 PyTest functions covering edge cases and null inputs. |

| **3** | **UI Mockup to React Components** | Vision | **Input:** High-resolution PNG screenshot of a Figma dashboard design. <br> **Output:** Executable React/Tailwind `.jsx` component code replicating the visual layout. |

| **4** | **Log Analysis Root Cause Extraction** | Extraction | **Input:** 10,000 lines of raw AWS CloudWatch error logs from a server crash. <br> **Output:** A 2-sentence summary identifying the specific Database Timeout exception that triggered the cascade failure. |

| **5** | **Knowledge-Base Support Chatbot** | RAG / Embeddings | **Input:** User string ("How to reset API key") + Top 3 retrieved markdown chunks from the internal developer wiki. <br> **Output:** A 3-step instructional text block citing the specific URL of the wiki chunk used. |

| **6** | **Pull Request Reviewer** | Text / Code | **Input:** `git diff` string containing 250 added and 40 removed lines of code. <br> **Output:** Markdown-formatted comment highlighting 2 unescaped SQL variables (security risks) and 1 missing docstring. |

| **7** | **Legacy Code Migration** | Code Translation | **Input:** 500-line legacy COBOL batch processing script. <br> **Output:** Refactored Python 3 script using `pandas` with equivalent business logic and inline comments. |

| **8** | **Support Ticket Intent Routing** | Extraction | **Input:** User message: "My dashboard is completely blank on Chrome." <br> **Output:** JSON object: `{"category": "frontend_bug", "priority": "high", "browser_context": "chrome", "assigned_queue": "tier_2_support"}` |

| **9** | **Autonomous Bug Fixing** | Agentic Execution | **Input:** GitHub Issue URL complaining about a broken shopping cart + repository access token. <br> **Output:** A submitted Pull Request containing the specific `.js` file patch that resolves the state management bug. |

| **10** | **Database Schema Drafting** | Text Generation | **Input:** Requirements string: "I need an e-commerce backend with users, orders, and products." <br> **Output:** Raw SQL script containing `CREATE TABLE` statements with primary keys, foreign key relationships, and data types. |

---

## The First Build: The Customer Tone De-escalator

**Why I would build this first:**
I would build the Customer Tone De-escalator first because it delivers immediate, measurable value to support teams without requiring the complex infrastructure of a vector database or document chunking pipeline. It perfectly scopes down the technical learning curve to focus entirely on mastering fundamental prompt engineering and enforcing strict JSON API outputs. This ensures a stable, stateless "quick win" that builds foundational skills before tackling the heavy lifting of a full RAG architecture.