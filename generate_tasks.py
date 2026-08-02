"""
Script to generate task markdown files for the 6 missing domains:
uiux, dsa, blockchain, android, sql, genai
Each domain gets 4 weeks × 3 tasks.
"""
import os

BASE = r"c:\Users\saksh\Desktop\skill-me\SkillMe-Intern-Tasks"

TASKS = {
    "uiux": {
        1: [
            {
                "title": "Figma Fundamentals & UI Audit",
                "difficulty": "easy",
                "labels": ["week-1", "figma", "ui"],
                "body": """## Task Description
Get hands-on with Figma and perform a UI audit on a real-world app of your choice.

## Requirements
- Create a free Figma account and explore the interface
- Pick any popular mobile/web app (e.g., Swiggy, Notion, Spotify)
- Identify and document **5 UI problems** (poor contrast, misaligned elements, confusing navigation, etc.)
- Create a simple wireframe mockup of ONE improved screen in Figma

## Acceptance Criteria
- [ ] Figma file shared with view-only link
- [ ] 5 problems documented with screenshots in `PROGRESS.md`
- [ ] At least 1 improved wireframe created in Figma
- [ ] PR submitted with your Figma link and notes

## Resources
- [Figma for Beginners](https://www.figma.com/resources/learn-design/)
- [Laws of UX](https://lawsofux.com/)"""
            },
            {
                "title": "Design a Color System & Typography Scale",
                "difficulty": "easy",
                "labels": ["week-1", "design-system", "typography"],
                "body": """## Task Description
Build a foundational design system with a color palette and typography scale in Figma.

## Requirements
- Define a **primary, secondary, and neutral** color palette (with shades 50–900)
- Ensure WCAG AA contrast compliance for all text/background combinations
- Create a typography scale (H1–H6, body, caption) using a Google Font of your choice
- Document your choices in a Figma page called "Design Tokens"

## Acceptance Criteria
- [ ] Figma file with color styles and text styles defined
- [ ] Color contrast ratios documented (use Figma's contrast checker or Coolors)
- [ ] Typography scale applied to a sample "hero section" mockup
- [ ] PR with Figma link

## Resources
- [Material Design Color System](https://m3.material.io/styles/color)
- [WCAG Contrast Checker](https://webaim.org/resources/contrastchecker/)"""
            },
            {
                "title": "Low-Fidelity Wireframe for a Dashboard",
                "difficulty": "medium",
                "labels": ["week-1", "wireframe", "ux"],
                "body": """## Task Description
Create a low-fidelity wireframe for a student internship dashboard.

## Requirements
- Design 3 screens: Dashboard Home, Task List, Profile Page
- Use only grayscale — focus on layout, not aesthetics
- Include navigation, content areas, and interactive elements
- Add annotations explaining UX decisions

## Acceptance Criteria
- [ ] 3 wireframe screens in Figma
- [ ] Annotations/notes on at least 5 UX decisions
- [ ] Prototype links between screens (clickable)
- [ ] PR with Figma prototype link

## Resources
- [UX Wireframing Best Practices](https://www.nngroup.com/articles/wireframing-guide/)"""
            },
        ],
        2: [
            {
                "title": "High-Fidelity UI Design — Dashboard Home",
                "difficulty": "medium",
                "labels": ["week-2", "figma", "hi-fi"],
                "body": """## Task Description
Convert your Week 1 low-fidelity wireframe into a polished high-fidelity design for the Dashboard Home screen.

## Requirements
- Apply your Week 1 color system and typography scale
- Use auto-layout and components (cards, buttons, badges)
- Add realistic placeholder data (progress bars, task counts, etc.)
- Design both light and dark mode variants

## Acceptance Criteria
- [ ] Hi-fi Dashboard Home screen (light + dark mode)
- [ ] Uses Figma Components for at least 3 reusable elements
- [ ] Auto-layout used throughout
- [ ] PR with Figma file"""
            },
            {
                "title": "Component Library — Buttons, Inputs & Cards",
                "difficulty": "medium",
                "labels": ["week-2", "components", "design-system"],
                "body": """## Task Description
Build a reusable component library in Figma for your design system.

## Requirements
- **Buttons**: Primary, Secondary, Danger, Ghost — in Default, Hover, Disabled states
- **Inputs**: Text, Password, Dropdown — with Default, Focus, Error states
- **Cards**: Task card, Stat card, Profile card
- All components must use Figma Variants

## Acceptance Criteria
- [ ] Component page in Figma with all variants
- [ ] At least 3 component types with all states
- [ ] Components used in at least one full-screen mockup
- [ ] PR with Figma link"""
            },
            {
                "title": "Usability Testing Plan",
                "difficulty": "easy",
                "labels": ["week-2", "ux-research", "testing"],
                "body": """## Task Description
Write a usability testing plan for your internship dashboard design.

## Requirements
- Define 3–5 user tasks to test (e.g., "Find your Week 2 tasks")
- Write a test script with introduction, tasks, and debrief questions
- Conduct at least 1 mock usability test with a friend/peer
- Document findings and proposed changes

## Acceptance Criteria
- [ ] Test plan document in `PROGRESS.md`
- [ ] At least 3 test tasks defined
- [ ] Mock test conducted and findings documented
- [ ] PR with notes"""
            },
        ],
        3: [
            {
                "title": "Responsive Design — Mobile Adaptation",
                "difficulty": "medium",
                "labels": ["week-3", "responsive", "mobile"],
                "body": """## Task Description
Adapt your dashboard design for mobile (375px width).

## Requirements
- Create mobile versions of all 3 screens from Week 1
- Use a bottom navigation bar instead of sidebar
- Ensure touch targets are at least 44×44px
- Use Figma's responsive constraints properly

## Acceptance Criteria
- [ ] Mobile designs for all 3 screens
- [ ] Bottom navigation implemented
- [ ] Touch targets verified (use Figma's inspect panel)
- [ ] PR with Figma link"""
            },
            {
                "title": "Micro-interactions & Animation Prototype",
                "difficulty": "hard",
                "labels": ["week-3", "animation", "prototype"],
                "body": """## Task Description
Add micro-interactions and animations to your Figma prototype.

## Requirements
- Button hover/press states with transitions
- Page transitions between screens (slide, fade)
- Loading skeleton state for the dashboard
- Animated progress bar for task completion

## Acceptance Criteria
- [ ] Figma prototype with at least 4 micro-interactions
- [ ] Loading skeleton screen designed
- [ ] Smooth page transitions implemented
- [ ] PR with shareable prototype link"""
            },
            {
                "title": "Accessibility Audit",
                "difficulty": "medium",
                "labels": ["week-3", "accessibility", "a11y"],
                "body": """## Task Description
Audit your design for accessibility compliance.

## Requirements
- Check all text/background color combinations for WCAG AA compliance
- Ensure focus states are visible for all interactive elements
- Add alt text descriptions for all icons/images
- Check touch target sizes on mobile designs

## Acceptance Criteria
- [ ] Accessibility audit checklist completed in `PROGRESS.md`
- [ ] All contrast ratios documented (pass/fail)
- [ ] At least 3 issues found and fixed
- [ ] PR with updated designs"""
            },
        ],
        4: [
            {
                "title": "Final Design System Documentation",
                "difficulty": "hard",
                "labels": ["week-4", "documentation", "design-system"],
                "body": """## Task Description
Document your complete design system as a handoff-ready Figma file.

## Requirements
- Cover page with project overview
- Color tokens, typography scale, spacing system
- Full component library with usage guidelines
- Design principles and do/don't examples

## Acceptance Criteria
- [ ] Complete design system Figma file
- [ ] Usage guidelines for all components
- [ ] At least 5 do/don't examples
- [ ] PR with Figma link"""
            },
            {
                "title": "Clickable Prototype & User Flow",
                "difficulty": "hard",
                "labels": ["week-4", "prototype", "user-flow"],
                "body": """## Task Description
Build a fully clickable end-to-end prototype of your dashboard.

## Requirements
- All 3 screens linked and navigable
- Covers the complete user journey: Login → Dashboard → Task Detail → Profile
- Includes error states and empty states
- Shareable prototype link

## Acceptance Criteria
- [ ] Complete clickable prototype (no dead ends)
- [ ] Error and empty states included
- [ ] User flow diagram in `PROGRESS.md`
- [ ] PR with prototype link"""
            },
            {
                "title": "Case Study Write-Up",
                "difficulty": "medium",
                "labels": ["week-4", "case-study", "portfolio"],
                "body": """## Task Description
Write a design case study documenting your internship project.

## Requirements
- Problem statement and research insights
- Design process: research → wireframe → hi-fi → prototype
- Key design decisions and trade-offs
- Final design screenshots and Figma links
- Lessons learned

## Acceptance Criteria
- [ ] Case study written in `PROGRESS.md` (min 500 words)
- [ ] All design stages documented with screenshots
- [ ] Figma links included
- [ ] PR submitted"""
            },
        ],
    },

    "dsa": {
        1: [
            {
                "title": "Arrays & Strings — Sliding Window",
                "difficulty": "easy",
                "labels": ["week-1", "arrays", "sliding-window"],
                "body": """## Task Description
Implement classic sliding window problems on arrays and strings.

## Problems to Solve
1. **Maximum Sum Subarray of Size K** — Find the maximum sum of any contiguous subarray of size k
2. **Longest Substring Without Repeating Characters** — [LeetCode #3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
3. **Minimum Window Substring** — [LeetCode #76](https://leetcode.com/problems/minimum-window-substring/)

## Requirements
- Solve all 3 problems in your preferred language (Python/C++/Java)
- Write brute-force first, then optimize
- Add time/space complexity analysis as comments
- Push solutions to `week-1/sliding-window/` folder

## Acceptance Criteria
- [ ] All 3 problems solved and pushed
- [ ] LeetCode submission screenshots in `PROGRESS.md`
- [ ] Complexity analysis added for each solution
- [ ] PR submitted"""
            },
            {
                "title": "Two Pointers & Binary Search",
                "difficulty": "medium",
                "labels": ["week-1", "two-pointers", "binary-search"],
                "body": """## Task Description
Master the two pointers technique and binary search pattern.

## Problems to Solve
1. **3Sum** — [LeetCode #15](https://leetcode.com/problems/3sum/)
2. **Container With Most Water** — [LeetCode #11](https://leetcode.com/problems/container-with-most-water/)
3. **Search in Rotated Sorted Array** — [LeetCode #33](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## Requirements
- Solve using the specific pattern (two pointers or binary search)
- Comment each solution explaining the pointer/binary logic
- Include test cases in a separate test file

## Acceptance Criteria
- [ ] All 3 problems solved
- [ ] Approach explained in comments
- [ ] At least 3 test cases per problem
- [ ] PR submitted"""
            },
            {
                "title": "Recursion & Backtracking",
                "difficulty": "medium",
                "labels": ["week-1", "recursion", "backtracking"],
                "body": """## Task Description
Solve problems using recursion and backtracking.

## Problems to Solve
1. **Subsets** — [LeetCode #78](https://leetcode.com/problems/subsets/)
2. **Permutations** — [LeetCode #46](https://leetcode.com/problems/permutations/)
3. **N-Queens** — [LeetCode #51](https://leetcode.com/problems/n-queens/)

## Requirements
- Draw the recursion tree for at least one problem in `PROGRESS.md`
- Implement with memoization where applicable

## Acceptance Criteria
- [ ] All 3 problems solved
- [ ] Recursion tree diagram for 1 problem
- [ ] PR submitted"""
            },
        ],
        2: [
            {
                "title": "Linked Lists & Stacks",
                "difficulty": "medium",
                "labels": ["week-2", "linked-list", "stack"],
                "body": """## Task Description
Implement linked list and stack-based problems.

## Problems to Solve
1. **Reverse Linked List** — [LeetCode #206](https://leetcode.com/problems/reverse-linked-list/)
2. **LRU Cache** — [LeetCode #146](https://leetcode.com/problems/lru-cache/)
3. **Valid Parentheses** — [LeetCode #20](https://leetcode.com/problems/valid-parentheses/)
4. **Daily Temperatures** — [LeetCode #739](https://leetcode.com/problems/daily-temperatures/)

## Acceptance Criteria
- [ ] All 4 problems solved
- [ ] LRU Cache implemented from scratch
- [ ] PR submitted"""
            },
            {
                "title": "Trees — BFS & DFS",
                "difficulty": "medium",
                "labels": ["week-2", "trees", "bfs", "dfs"],
                "body": """## Task Description
Solve tree traversal and path problems.

## Problems to Solve
1. **Binary Tree Level Order Traversal** — [LeetCode #102](https://leetcode.com/problems/binary-tree-level-order-traversal/)
2. **Maximum Depth of Binary Tree** — [LeetCode #104](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
3. **Path Sum II** — [LeetCode #113](https://leetcode.com/problems/path-sum-ii/)
4. **Lowest Common Ancestor** — [LeetCode #236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

## Acceptance Criteria
- [ ] All 4 problems solved
- [ ] Both iterative and recursive solutions for at least 1 problem
- [ ] PR submitted"""
            },
            {
                "title": "Heaps & Priority Queues",
                "difficulty": "hard",
                "labels": ["week-2", "heap", "priority-queue"],
                "body": """## Task Description
Implement heap-based problems and understand priority queues.

## Problems to Solve
1. **Kth Largest Element in Array** — [LeetCode #215](https://leetcode.com/problems/kth-largest-element-in-an-array/)
2. **Top K Frequent Elements** — [LeetCode #347](https://leetcode.com/problems/top-k-frequent-elements/)
3. **Merge K Sorted Lists** — [LeetCode #23](https://leetcode.com/problems/merge-k-sorted-lists/)

## Acceptance Criteria
- [ ] All 3 problems solved using heap/priority queue
- [ ] Implement a MinHeap from scratch in `week-2/minheap.py` (or `.cpp`/`.java`)
- [ ] PR submitted"""
            },
        ],
        3: [
            {
                "title": "Dynamic Programming — 1D",
                "difficulty": "medium",
                "labels": ["week-3", "dp", "memoization"],
                "body": """## Task Description
Solve 1D dynamic programming problems.

## Problems to Solve
1. **Climbing Stairs** — [LeetCode #70](https://leetcode.com/problems/climbing-stairs/)
2. **House Robber** — [LeetCode #198](https://leetcode.com/problems/house-robber/)
3. **Longest Increasing Subsequence** — [LeetCode #300](https://leetcode.com/problems/longest-increasing-subsequence/)
4. **Coin Change** — [LeetCode #322](https://leetcode.com/problems/coin-change/)

## Requirements
- Solve using both top-down (memoization) and bottom-up (tabulation) for at least 2 problems

## Acceptance Criteria
- [ ] All 4 problems solved
- [ ] Both approaches shown for at least 2 problems
- [ ] PR submitted"""
            },
            {
                "title": "Dynamic Programming — 2D & Grids",
                "difficulty": "hard",
                "labels": ["week-3", "dp", "grid"],
                "body": """## Task Description
Solve 2D DP and grid-based dynamic programming problems.

## Problems to Solve
1. **Unique Paths** — [LeetCode #62](https://leetcode.com/problems/unique-paths/)
2. **Longest Common Subsequence** — [LeetCode #1143](https://leetcode.com/problems/longest-common-subsequence/)
3. **Edit Distance** — [LeetCode #72](https://leetcode.com/problems/edit-distance/)

## Acceptance Criteria
- [ ] All 3 problems solved
- [ ] 2D DP table visualization in `PROGRESS.md` for 1 problem
- [ ] PR submitted"""
            },
            {
                "title": "Graphs — BFS/DFS & Shortest Paths",
                "difficulty": "hard",
                "labels": ["week-3", "graphs", "dijkstra"],
                "body": """## Task Description
Implement graph traversal and shortest path algorithms.

## Problems to Solve
1. **Number of Islands** — [LeetCode #200](https://leetcode.com/problems/number-of-islands/)
2. **Clone Graph** — [LeetCode #133](https://leetcode.com/problems/clone-graph/)
3. **Course Schedule** — [LeetCode #207](https://leetcode.com/problems/course-schedule/) (Topological Sort)
4. Implement **Dijkstra's Algorithm** from scratch

## Acceptance Criteria
- [ ] All 3 LeetCode problems solved
- [ ] Dijkstra implemented and tested on a sample graph
- [ ] PR submitted"""
            },
        ],
        4: [
            {
                "title": "Competitive Programming Contest Simulation",
                "difficulty": "hard",
                "labels": ["week-4", "competitive", "contest"],
                "body": """## Task Description
Simulate a competitive programming contest by solving a Codeforces/AtCoder round.

## Requirements
- Pick any Codeforces Div 2 round (A–D problems)
- Solve at least **3 problems** within a 2-hour time limit
- Document your approach, where you got stuck, and time taken per problem

## Acceptance Criteria
- [ ] At least 3 accepted solutions pushed to `week-4/contest/`
- [ ] Contest report in `PROGRESS.md` (approach + time breakdown)
- [ ] PR submitted"""
            },
            {
                "title": "Trie, Segment Tree & Advanced DS",
                "difficulty": "hard",
                "labels": ["week-4", "trie", "segment-tree"],
                "body": """## Task Description
Implement advanced data structures: Trie and Segment Tree.

## Requirements
1. **Implement a Trie** — with insert, search, and startsWith
2. Solve **Word Search II** — [LeetCode #212](https://leetcode.com/problems/word-search-ii/) using your Trie
3. **Implement a Segment Tree** — with range sum query and point update

## Acceptance Criteria
- [ ] Trie implemented from scratch
- [ ] Word Search II solved using Trie
- [ ] Segment Tree implemented and tested
- [ ] PR submitted"""
            },
            {
                "title": "DSA Interview Mock — 5 Mixed Problems",
                "difficulty": "hard",
                "labels": ["week-4", "interview", "mock"],
                "body": """## Task Description
Solve 5 mixed-difficulty problems as a mock technical interview.

## Problems to Solve (pick 5 from this list)
- Median of Two Sorted Arrays — [LeetCode #4](https://leetcode.com/problems/median-of-two-sorted-arrays/)
- Regular Expression Matching — [LeetCode #10](https://leetcode.com/problems/regular-expression-matching/)
- Trapping Rain Water — [LeetCode #42](https://leetcode.com/problems/trapping-rain-water/)
- Largest Rectangle in Histogram — [LeetCode #84](https://leetcode.com/problems/largest-rectangle-in-histogram/)
- Word Ladder — [LeetCode #127](https://leetcode.com/problems/word-ladder/)
- Alien Dictionary — [LeetCode #269](https://leetcode.com/problems/alien-dictionary/)

## Acceptance Criteria
- [ ] 5 problems solved
- [ ] Solutions pushed to `week-4/mock-interview/`
- [ ] Time complexity for each solution documented
- [ ] PR submitted"""
            },
        ],
    },

    "blockchain": {
        1: [
            {
                "title": "Blockchain Fundamentals & Ethereum Setup",
                "difficulty": "easy",
                "labels": ["week-1", "ethereum", "setup"],
                "body": """## Task Description
Set up your Ethereum development environment and understand core blockchain concepts.

## Requirements
- Install Node.js, Hardhat, and MetaMask
- Create a Hardhat project (`npx hardhat init`)
- Write a summary of: blocks, transactions, gas, consensus mechanisms in `PROGRESS.md`
- Connect MetaMask to Hardhat's local network

## Acceptance Criteria
- [ ] Hardhat project initialized and pushed
- [ ] `PROGRESS.md` with blockchain concepts summary (min 300 words)
- [ ] MetaMask setup screenshot in `PROGRESS.md`
- [ ] PR submitted"""
            },
            {
                "title": "Your First Smart Contract — Storage & Counter",
                "difficulty": "easy",
                "labels": ["week-1", "solidity", "smart-contract"],
                "body": """## Task Description
Write your first Solidity smart contracts.

## Requirements
1. **SimpleStorage**: Store and retrieve a number, with an event emitted on change
2. **Counter**: Increment, decrement, and reset — with access control (only owner can reset)
3. Write unit tests for both contracts using Hardhat + ethers.js

## Acceptance Criteria
- [ ] Both contracts written in Solidity (^0.8.0)
- [ ] Unit tests written (at least 3 per contract)
- [ ] All tests passing (`npx hardhat test`)
- [ ] PR submitted"""
            },
            {
                "title": "ERC-20 Token — Mint & Transfer",
                "difficulty": "medium",
                "labels": ["week-1", "erc20", "token"],
                "body": """## Task Description
Build a custom ERC-20 token using OpenZeppelin.

## Requirements
- Create an ERC-20 token: `SkillToken (SKL)`
- Use OpenZeppelin's ERC20 base contract
- Add mint (only owner), burn, and transfer functionality
- Deploy to Hardhat local network and interact via script

## Acceptance Criteria
- [ ] ERC-20 contract written and tested
- [ ] Deploy script written (`scripts/deploy.js`)
- [ ] README documenting token name, symbol, supply
- [ ] PR submitted"""
            },
        ],
        2: [
            {
                "title": "NFT Collection — ERC-721 Mint",
                "difficulty": "medium",
                "labels": ["week-2", "nft", "erc721"],
                "body": """## Task Description
Build an NFT collection using ERC-721.

## Requirements
- Create an ERC-721 contract using OpenZeppelin
- Implement: mint (public, max supply cap), tokenURI (returns IPFS metadata)
- Upload sample metadata to IPFS via Pinata
- Write tests for minting and metadata

## Acceptance Criteria
- [ ] ERC-721 contract written with max supply
- [ ] Metadata uploaded to IPFS (Pinata link in README)
- [ ] Tests passing
- [ ] PR submitted"""
            },
            {
                "title": "Decentralized Voting Smart Contract",
                "difficulty": "hard",
                "labels": ["week-2", "voting", "solidity"],
                "body": """## Task Description
Build a decentralized voting system on Ethereum.

## Requirements
- Voters can register with their address
- Owner creates proposals
- Each address can vote once
- Results are publicly readable after voting ends
- Include time-based voting window

## Acceptance Criteria
- [ ] Voting contract with all functions
- [ ] At least 5 unit tests (including edge cases)
- [ ] PR submitted"""
            },
            {
                "title": "Web3.js / ethers.js Frontend Integration",
                "difficulty": "medium",
                "labels": ["week-2", "frontend", "ethers"],
                "body": """## Task Description
Build a simple frontend to interact with your Week 1 or Week 2 contracts.

## Requirements
- Connect MetaMask wallet on button click
- Read contract state (e.g., current count, token balance)
- Write transactions (e.g., increment, mint token)
- Display transaction hash and status

## Acceptance Criteria
- [ ] HTML/JS frontend that connects to MetaMask
- [ ] Can read and write to contract
- [ ] Transaction feedback shown to user
- [ ] PR submitted"""
            },
        ],
        3: [
            {
                "title": "DeFi — Simple AMM / Swap Contract",
                "difficulty": "hard",
                "labels": ["week-3", "defi", "amm"],
                "body": """## Task Description
Implement a basic Automated Market Maker (AMM) like Uniswap V1.

## Requirements
- Two ERC-20 tokens (TokenA, TokenB)
- Liquidity pool: add/remove liquidity
- Swap: TokenA → TokenB and vice versa using constant product formula (x * y = k)
- Emit events for all operations

## Acceptance Criteria
- [ ] AMM contract implemented
- [ ] Liquidity add/remove working
- [ ] Swap with slippage tolerance
- [ ] Tests passing for all operations
- [ ] PR submitted"""
            },
            {
                "title": "IPFS & Decentralized Storage",
                "difficulty": "medium",
                "labels": ["week-3", "ipfs", "storage"],
                "body": """## Task Description
Store and retrieve data using IPFS via Pinata.

## Requirements
- Upload a JSON file to IPFS using Pinata SDK
- Retrieve and display the file via an IPFS gateway
- Store the IPFS CID on-chain in a smart contract
- Build a simple UI to upload, store, and retrieve

## Acceptance Criteria
- [ ] Pinata upload working (Node.js script)
- [ ] CID stored on-chain
- [ ] Retrieval working via gateway URL
- [ ] PR submitted"""
            },
            {
                "title": "Deploy to Sepolia Testnet",
                "difficulty": "medium",
                "labels": ["week-3", "deployment", "testnet"],
                "body": """## Task Description
Deploy your contracts to the Ethereum Sepolia testnet.

## Requirements
- Get Sepolia test ETH from a faucet
- Configure Hardhat for Sepolia
- Deploy your Week 1 ERC-20 and Week 2 voting contract
- Verify contracts on Etherscan

## Acceptance Criteria
- [ ] Both contracts deployed to Sepolia
- [ ] Etherscan verified links in `PROGRESS.md`
- [ ] Deploy scripts pushed
- [ ] PR submitted"""
            },
        ],
        4: [
            {
                "title": "Complete DApp — End-to-End",
                "difficulty": "hard",
                "labels": ["week-4", "dapp", "fullstack"],
                "body": """## Task Description
Build a complete DApp combining your work from Weeks 1–3.

## Requirements
- Frontend: React or plain HTML/JS
- Features: Wallet connect, read/write contract, transaction history
- Deploy frontend to Vercel/Netlify
- Smart contract on Sepolia testnet

## Acceptance Criteria
- [ ] Full DApp running (frontend + contract)
- [ ] Deployed frontend URL in `PROGRESS.md`
- [ ] Sepolia contract address documented
- [ ] PR submitted"""
            },
            {
                "title": "Smart Contract Security Audit",
                "difficulty": "hard",
                "labels": ["week-4", "security", "audit"],
                "body": """## Task Description
Audit one of your smart contracts for common vulnerabilities.

## Requirements
- Run Slither static analysis (`pip install slither-analyzer`)
- Check for: reentrancy, integer overflow, access control issues, front-running
- Document all findings with severity (High/Medium/Low/Info)
- Fix at least 2 issues found

## Acceptance Criteria
- [ ] Slither report generated and pushed
- [ ] Audit findings documented in `PROGRESS.md`
- [ ] At least 2 fixes implemented with explanation
- [ ] PR submitted"""
            },
            {
                "title": "Web3 Project Presentation",
                "difficulty": "medium",
                "labels": ["week-4", "presentation", "portfolio"],
                "body": """## Task Description
Prepare a final project write-up and demonstration for your Web3 internship work.

## Requirements
- Write a project summary covering all 4 weeks (min 400 words)
- Include all contract addresses, Etherscan links, and frontend URLs
- Record a 2–3 minute Loom video demo of your DApp
- Add to your GitHub profile README

## Acceptance Criteria
- [ ] Project summary in `PROGRESS.md`
- [ ] Loom video link included
- [ ] All contract/frontend links working
- [ ] PR submitted"""
            },
        ],
    },

    "android": {
        1: [
            {
                "title": "Android Setup & First App — Hello SkillMe",
                "difficulty": "easy",
                "labels": ["week-1", "kotlin", "setup"],
                "body": """## Task Description
Set up Android Studio and build your first Android app in Kotlin.

## Requirements
- Install Android Studio and create a new project (Empty Activity)
- App name: "SkillMe"
- Add a TextView with "Hello, SkillMe!" and a Button that changes the text when clicked
- Use ViewBinding (not findViewByID)
- Run on an emulator or physical device

## Acceptance Criteria
- [ ] App builds and runs without errors
- [ ] Button click changes the text
- [ ] ViewBinding used
- [ ] Screenshot in `PROGRESS.md`
- [ ] PR submitted"""
            },
            {
                "title": "Layouts & UI — RecyclerView Task List",
                "difficulty": "easy",
                "labels": ["week-1", "recyclerview", "xml"],
                "body": """## Task Description
Build a task list app using RecyclerView.

## Requirements
- List of 10 hardcoded tasks with title and status (done/pending)
- RecyclerView with a custom item layout
- Clicking a task toggles its status (struck-through text)
- Use ConstraintLayout for item layout

## Acceptance Criteria
- [ ] RecyclerView with 10 tasks
- [ ] Click toggles task status visually
- [ ] Clean item layout using ConstraintLayout
- [ ] PR submitted"""
            },
            {
                "title": "Kotlin Fundamentals — OOP & Coroutines",
                "difficulty": "medium",
                "labels": ["week-1", "kotlin", "coroutines"],
                "body": """## Task Description
Practice Kotlin fundamentals: OOP and coroutines.

## Requirements
1. Create a `Student` data class with: name, domain, progress (0–100)
2. Implement a `TaskManager` singleton with functions: addTask, removeTask, getAll
3. Write a coroutine that simulates fetching tasks from a "network" (delay 2s) and updates the UI

## Acceptance Criteria
- [ ] Student data class and TaskManager implemented
- [ ] Coroutine demo working (no ANR)
- [ ] Unit tests for TaskManager
- [ ] PR submitted"""
            },
        ],
        2: [
            {
                "title": "MVVM Architecture & LiveData",
                "difficulty": "medium",
                "labels": ["week-2", "mvvm", "livedata"],
                "body": """## Task Description
Refactor your task list app to use MVVM architecture.

## Requirements
- ViewModel to hold task list (LiveData<List<Task>>)
- Repository pattern for data access
- UI observes LiveData and auto-updates
- Add functionality: Add task (dialog), Delete task (swipe)

## Acceptance Criteria
- [ ] MVVM architecture implemented
- [ ] LiveData observer in Fragment/Activity
- [ ] Add and delete working
- [ ] PR submitted"""
            },
            {
                "title": "Jetpack Compose — UI Rebuild",
                "difficulty": "hard",
                "labels": ["week-2", "compose", "jetpack"],
                "body": """## Task Description
Rebuild your task list UI using Jetpack Compose.

## Requirements
- LazyColumn for task list
- Custom Composable for task item
- State management with `remember` and `mutableStateOf`
- Material3 theme with dark mode support

## Acceptance Criteria
- [ ] Task list built in Compose
- [ ] Dark mode working
- [ ] State updates correctly on click
- [ ] PR submitted"""
            },
            {
                "title": "Navigation Component & Multi-Screen App",
                "difficulty": "medium",
                "labels": ["week-2", "navigation", "fragments"],
                "body": """## Task Description
Add multi-screen navigation using Navigation Component.

## Requirements
- 3 screens: Task List, Task Detail, Add Task
- Bottom navigation bar
- Safe Args for passing data between screens
- Back stack handled correctly

## Acceptance Criteria
- [ ] 3 screens with Navigation Component
- [ ] Bottom navigation working
- [ ] Data passed via Safe Args
- [ ] PR submitted"""
            },
        ],
        3: [
            {
                "title": "Room Database — Local Persistence",
                "difficulty": "medium",
                "labels": ["week-3", "room", "database"],
                "body": """## Task Description
Add local data persistence using Room database.

## Requirements
- Room Entity: `Task(id, title, description, isDone, createdAt)`
- DAO with: insert, update, delete, getAll, getById
- Repository wraps DAO
- ViewModel updated to read from Room

## Acceptance Criteria
- [ ] Room database set up
- [ ] CRUD operations working
- [ ] Data persists after app restart
- [ ] PR submitted"""
            },
            {
                "title": "Retrofit — REST API Integration",
                "difficulty": "hard",
                "labels": ["week-3", "retrofit", "api"],
                "body": """## Task Description
Fetch data from a REST API using Retrofit and display in RecyclerView.

## Requirements
- Use the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/todos)
- Retrofit + OkHttp + Gson
- Show loading indicator while fetching
- Handle errors gracefully (no crash)

## Acceptance Criteria
- [ ] API data displayed in RecyclerView
- [ ] Loading state shown during fetch
- [ ] Error state handled
- [ ] PR submitted"""
            },
            {
                "title": "Push Notifications with FCM",
                "difficulty": "medium",
                "labels": ["week-3", "fcm", "notifications"],
                "body": """## Task Description
Integrate Firebase Cloud Messaging for push notifications.

## Requirements
- Set up Firebase project and add google-services.json
- Implement FCM service to receive messages
- Show notification with title and body when app is in background
- Handle notification click to open a specific screen

## Acceptance Criteria
- [ ] FCM integrated and working
- [ ] Background notification received and shown
- [ ] Click opens correct screen
- [ ] PR submitted"""
            },
        ],
        4: [
            {
                "title": "Final App — Complete Feature Set",
                "difficulty": "hard",
                "labels": ["week-4", "final", "fullstack"],
                "body": """## Task Description
Build a complete Android app combining all skills from Weeks 1–3.

## Requirements
- **App**: Student Task Tracker
- Features: Task CRUD, API sync, Room persistence, push notifications
- MVVM + Compose UI
- Material3 design with dark mode

## Acceptance Criteria
- [ ] Full app with all features
- [ ] APK built and uploaded to `week-4/`
- [ ] README with screenshots
- [ ] PR submitted"""
            },
            {
                "title": "Unit & UI Testing",
                "difficulty": "hard",
                "labels": ["week-4", "testing", "espresso"],
                "body": """## Task Description
Add unit tests and UI tests to your Android app.

## Requirements
- Unit tests for ViewModel and Repository (JUnit + MockK)
- UI tests for 2 key user flows (Espresso)
- At least 80% test pass rate

## Acceptance Criteria
- [ ] Unit tests for ViewModel/Repository
- [ ] Espresso UI tests for 2 flows
- [ ] Test run screenshot in `PROGRESS.md`
- [ ] PR submitted"""
            },
            {
                "title": "Publish to Google Play (Internal Testing)",
                "difficulty": "medium",
                "labels": ["week-4", "publish", "play-store"],
                "body": """## Task Description
Prepare your app for Google Play Store submission.

## Requirements
- Generate a signed APK/AAB
- Write a Play Store listing: description, screenshots, icon
- Upload to Google Play Console (Internal Testing track)
- Ensure app meets Play Store policies

## Acceptance Criteria
- [ ] Signed APK generated
- [ ] Play Store listing written (in `PROGRESS.md` if not actually uploaded)
- [ ] App icon and screenshots prepared
- [ ] PR submitted"""
            },
        ],
    },

    "sql": {
        1: [
            {
                "title": "SQL Basics — SELECT, WHERE, JOINs",
                "difficulty": "easy",
                "labels": ["week-1", "sql", "select"],
                "body": """## Task Description
Practice fundamental SQL queries on a sample database.

## Setup
Use the [W3Schools SQL Tryit Editor](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all) or SQLite locally.

## Problems to Solve
Write SQL queries for:
1. Find all customers from Germany
2. List all products with price > 50, ordered by price DESC
3. Count orders per customer (GROUP BY + COUNT)
4. JOIN: Show each order with customer name and order date
5. Find customers who have never placed an order (LEFT JOIN + NULL check)

## Acceptance Criteria
- [ ] All 5 queries written in `week-1/queries.sql`
- [ ] Results/screenshots for each query in `PROGRESS.md`
- [ ] PR submitted"""
            },
            {
                "title": "Database Design — Schema & ERD",
                "difficulty": "medium",
                "labels": ["week-1", "erd", "schema"],
                "body": """## Task Description
Design a relational database schema for a student internship platform.

## Requirements
- Design tables for: Students, Batches, Enrollments, Tasks, Submissions
- Define primary keys, foreign keys, and constraints (NOT NULL, UNIQUE)
- Draw an ERD using [dbdiagram.io](https://dbdiagram.io) or draw.io
- Write CREATE TABLE SQL statements

## Acceptance Criteria
- [ ] ERD shared (dbdiagram.io link or image)
- [ ] CREATE TABLE statements in `week-1/schema.sql`
- [ ] At least 5 tables with proper relationships
- [ ] PR submitted"""
            },
            {
                "title": "Aggregate Functions & Subqueries",
                "difficulty": "medium",
                "labels": ["week-1", "aggregates", "subqueries"],
                "body": """## Task Description
Write advanced SQL queries using aggregates and subqueries.

## Problems to Solve
1. Find the top 3 most popular products by order count
2. Find customers whose total order value exceeds the average
3. Rank employees by salary within each department (use RANK())
4. Find the second-highest salary using a subquery
5. Monthly revenue trend (GROUP BY year-month)

## Acceptance Criteria
- [ ] All 5 queries in `week-1/advanced-queries.sql`
- [ ] Window function (RANK/ROW_NUMBER) used in at least 1 query
- [ ] PR submitted"""
            },
        ],
        2: [
            {
                "title": "Indexing & Query Optimization",
                "difficulty": "medium",
                "labels": ["week-2", "indexing", "performance"],
                "body": """## Task Description
Understand and apply database indexing for query performance.

## Requirements
- Create a table with 10,000+ rows (use a script to insert)
- Run EXPLAIN/EXPLAIN ANALYZE on a slow query
- Add appropriate index and compare performance
- Document before/after query times

## Acceptance Criteria
- [ ] Data generation script in `week-2/seed.sql`
- [ ] EXPLAIN output before and after index in `PROGRESS.md`
- [ ] At least 3 indexes created with justification
- [ ] PR submitted"""
            },
            {
                "title": "Stored Procedures & Triggers",
                "difficulty": "hard",
                "labels": ["week-2", "stored-procedures", "triggers"],
                "body": """## Task Description
Implement stored procedures and triggers in PostgreSQL or MySQL.

## Requirements
1. **Stored Procedure**: `enroll_student(student_id, batch_id)` — checks capacity, inserts enrollment, returns status
2. **Trigger**: `after_submission_insert` — automatically updates progress table when a submission is added
3. **Function**: `get_student_score(student_id)` — returns total score

## Acceptance Criteria
- [ ] All 3 implemented and tested
- [ ] Test cases in `week-2/test_procedures.sql`
- [ ] PR submitted"""
            },
            {
                "title": "Transactions & ACID Properties",
                "difficulty": "medium",
                "labels": ["week-2", "transactions", "acid"],
                "body": """## Task Description
Implement database transactions and understand ACID properties.

## Requirements
- Write a transaction for: Enrolling a student (check capacity → insert → update count)
- Simulate a failure mid-transaction and verify rollback works
- Demonstrate isolation levels: READ COMMITTED vs SERIALIZABLE
- Document all 4 ACID properties with examples in `PROGRESS.md`

## Acceptance Criteria
- [ ] Transaction script with rollback handling
- [ ] Isolation level demo
- [ ] ACID documentation in `PROGRESS.md`
- [ ] PR submitted"""
            },
        ],
        3: [
            {
                "title": "PostgreSQL with Python (psycopg2 / SQLAlchemy)",
                "difficulty": "medium",
                "labels": ["week-3", "postgresql", "python"],
                "body": """## Task Description
Connect PostgreSQL to a Python application.

## Requirements
- Set up PostgreSQL locally (or use Supabase free tier)
- Use `psycopg2` or `SQLAlchemy` to connect
- CRUD operations: insert, fetch, update, delete students
- Build a simple CLI: list students, add student, update status

## Acceptance Criteria
- [ ] Connection working
- [ ] CRUD operations implemented
- [ ] CLI working (`python app.py`)
- [ ] PR submitted"""
            },
            {
                "title": "Data Analysis with SQL + Pandas",
                "difficulty": "hard",
                "labels": ["week-3", "analytics", "pandas"],
                "body": """## Task Description
Perform data analysis by combining SQL and Pandas.

## Requirements
- Load the [Kaggle Titanic dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset) into SQLite
- Write SQL queries to answer: survival rate by class, avg age by survival, top 10 fare payers
- Pull data into Pandas and create 3 visualizations (matplotlib/seaborn)

## Acceptance Criteria
- [ ] Data loaded into SQLite
- [ ] SQL queries in `week-3/analysis.sql`
- [ ] 3 charts generated and saved as images
- [ ] PR submitted"""
            },
            {
                "title": "NoSQL vs SQL — Redis Integration",
                "difficulty": "medium",
                "labels": ["week-3", "redis", "nosql"],
                "body": """## Task Description
Understand NoSQL by integrating Redis as a cache layer alongside PostgreSQL.

## Requirements
- Implement a caching layer: check Redis first, fall back to PostgreSQL
- Cache student profiles with TTL of 60 seconds
- Invalidate cache on update
- Compare query times with and without cache

## Acceptance Criteria
- [ ] Redis cache working
- [ ] Cache hit/miss logic implemented
- [ ] Performance comparison in `PROGRESS.md`
- [ ] PR submitted"""
            },
        ],
        4: [
            {
                "title": "Full Database-Backed REST API",
                "difficulty": "hard",
                "labels": ["week-4", "api", "postgresql"],
                "body": """## Task Description
Build a REST API fully backed by PostgreSQL.

## Requirements
- FastAPI or Flask + SQLAlchemy
- Endpoints: GET /students, POST /students, PATCH /students/{id}, DELETE /students/{id}
- Pagination (limit/offset) and filtering (by domain/status)
- Use Alembic for migrations

## Acceptance Criteria
- [ ] API running with all endpoints
- [ ] Pagination and filtering working
- [ ] Alembic migration file included
- [ ] PR submitted"""
            },
            {
                "title": "Database Backup, Replication & Monitoring",
                "difficulty": "hard",
                "labels": ["week-4", "backup", "monitoring"],
                "body": """## Task Description
Set up database backup and monitoring best practices.

## Requirements
- Write a backup script using `pg_dump` (cron-schedulable)
- Set up pgBadger or pg_stat_statements to identify slow queries
- Create a monitoring dashboard using Grafana + Prometheus (or just document the setup)
- Document a disaster recovery plan

## Acceptance Criteria
- [ ] Backup script in `week-4/backup.sh`
- [ ] Slow query report generated
- [ ] DR plan documented in `PROGRESS.md`
- [ ] PR submitted"""
            },
            {
                "title": "SQL Interview Prep — 20 Classic Questions",
                "difficulty": "medium",
                "labels": ["week-4", "interview", "prep"],
                "body": """## Task Description
Solve 20 classic SQL interview questions.

## Problems to Solve (from LeetCode SQL)
1. [Combine Two Tables](https://leetcode.com/problems/combine-two-tables/)
2. [Employees Earning More Than Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/)
3. [Duplicate Emails](https://leetcode.com/problems/duplicate-emails/)
4. [Department Highest Salary](https://leetcode.com/problems/department-highest-salary/)
5. [Rank Scores](https://leetcode.com/problems/rank-scores/)
...and 15 more from LeetCode SQL problems (Easy + Medium)

## Acceptance Criteria
- [ ] 20 queries in `week-4/interview-prep.sql`
- [ ] LeetCode submission links in `PROGRESS.md`
- [ ] PR submitted"""
            },
        ],
    },

    "genai": {
        1: [
            {
                "title": "LLM Fundamentals & OpenAI API Setup",
                "difficulty": "easy",
                "labels": ["week-1", "openai", "llm"],
                "body": """## Task Description
Understand how LLMs work and set up the OpenAI API.

## Requirements
- Read and summarize (in `PROGRESS.md`): What are transformers, tokens, embeddings?
- Set up OpenAI API key (or use Groq's free tier)
- Write a Python script that takes user input and returns a GPT response
- Experiment with temperature (0, 0.5, 1.0) and document observations

## Acceptance Criteria
- [ ] API setup working
- [ ] Python script with user input → GPT response
- [ ] Temperature experiment documented
- [ ] LLM fundamentals summary in `PROGRESS.md`
- [ ] PR submitted"""
            },
            {
                "title": "Prompt Engineering — 5 Techniques",
                "difficulty": "easy",
                "labels": ["week-1", "prompting", "llm"],
                "body": """## Task Description
Practice 5 core prompt engineering techniques.

## Techniques to Demonstrate
1. **Zero-shot** — Ask directly, no examples
2. **Few-shot** — Provide 2–3 examples before the question
3. **Chain-of-Thought** — Ask the model to "think step by step"
4. **Role Prompting** — Assign a persona ("You are an expert...")
5. **Self-Consistency** — Ask the same question 3 times with temperature > 0 and compare

## Requirements
- Demonstrate each technique with a concrete example
- Document results in `PROGRESS.md` (prompt in, response out)

## Acceptance Criteria
- [ ] 5 techniques demonstrated with real prompts + responses
- [ ] Python script for the 5 examples
- [ ] Observations documented
- [ ] PR submitted"""
            },
            {
                "title": "Build a CLI Chatbot",
                "difficulty": "medium",
                "labels": ["week-1", "chatbot", "python"],
                "body": """## Task Description
Build a command-line chatbot with conversation history.

## Requirements
- Maintain conversation history (system + user + assistant messages)
- Support at least 2 personas via system prompt (e.g., "tutor", "code reviewer")
- Allow user to switch persona with a command (e.g., `/persona tutor`)
- Add `/clear` to reset history and `/quit` to exit

## Acceptance Criteria
- [ ] CLI chatbot with history
- [ ] 2 personas switchable
- [ ] `/clear` and `/quit` commands working
- [ ] PR submitted"""
            },
        ],
        2: [
            {
                "title": "RAG — Retrieval Augmented Generation",
                "difficulty": "hard",
                "labels": ["week-2", "rag", "embeddings"],
                "body": """## Task Description
Build a basic RAG pipeline to answer questions from a document.

## Requirements
- Use LangChain or plain Python
- Load a PDF or text file (e.g., your resume or a Wikipedia article)
- Split into chunks, generate embeddings (OpenAI or free: sentence-transformers)
- Store in a vector store (ChromaDB or FAISS)
- Ask questions about the document — retrieve top-k chunks and generate answer

## Acceptance Criteria
- [ ] RAG pipeline working
- [ ] Can answer 5 sample questions from the document
- [ ] PR submitted"""
            },
            {
                "title": "LangChain Agents & Tools",
                "difficulty": "hard",
                "labels": ["week-2", "langchain", "agents"],
                "body": """## Task Description
Build an LLM agent that can use tools to answer questions.

## Requirements
- Build a LangChain agent with at least 3 tools:
  1. Calculator (math operations)
  2. Web search (use Serper or DuckDuckGo API)
  3. Python REPL (execute code)
- Agent should decide which tool to use based on the query

## Acceptance Criteria
- [ ] Agent with 3 working tools
- [ ] Demo of agent using each tool in `PROGRESS.md`
- [ ] PR submitted"""
            },
            {
                "title": "Fine-tuning vs Prompting — Experiment",
                "difficulty": "medium",
                "labels": ["week-2", "fine-tuning", "research"],
                "body": """## Task Description
Compare prompt engineering vs fine-tuning for a specific task.

## Requirements
- Pick a task: sentiment analysis, code generation, or question answering
- Approach A: Pure prompt engineering (few-shot, CoT)
- Approach B: Fine-tune a small model (use Hugging Face + a small dataset)
- Evaluate both on 20 test examples and compare accuracy

## Acceptance Criteria
- [ ] Both approaches implemented
- [ ] Evaluation on 20 test cases
- [ ] Comparison table in `PROGRESS.md`
- [ ] PR submitted"""
            },
        ],
        3: [
            {
                "title": "Build a AI-Powered REST API",
                "difficulty": "hard",
                "labels": ["week-3", "api", "fastapi"],
                "body": """## Task Description
Build a FastAPI service wrapping your LLM functionality.

## Endpoints to Implement
- `POST /chat` — Sends a message, returns AI response (with history support)
- `POST /summarize` — Summarizes provided text
- `POST /embed` — Returns embedding vector for text
- `GET /health` — Health check

## Requirements
- Async endpoints
- Input validation with Pydantic
- Rate limiting (max 10 req/min per IP)

## Acceptance Criteria
- [ ] All endpoints working
- [ ] Postman/Thunder Client collection in `week-3/`
- [ ] PR submitted"""
            },
            {
                "title": "Image Generation & Multimodal AI",
                "difficulty": "medium",
                "labels": ["week-3", "dalle", "vision"],
                "body": """## Task Description
Explore multimodal AI: image generation and vision.

## Requirements
1. Generate 5 images using DALL-E 3 or Stable Diffusion with varied prompts
2. Use GPT-4 Vision (or LLaVA) to describe an image
3. Build a simple app: user uploads image → AI describes it

## Acceptance Criteria
- [ ] 5 generated images saved in `week-3/images/`
- [ ] Image captioning working
- [ ] Prompts documented with results
- [ ] PR submitted"""
            },
            {
                "title": "Evaluation & Guardrails",
                "difficulty": "hard",
                "labels": ["week-3", "evaluation", "safety"],
                "body": """## Task Description
Evaluate your LLM app and add safety guardrails.

## Requirements
- Evaluate chatbot on 20 test prompts (accuracy, relevance, hallucination)
- Add guardrails: content moderation (OpenAI Moderation API), prompt injection detection
- Implement output validation: ensure responses are within expected length/format

## Acceptance Criteria
- [ ] 20-prompt evaluation documented
- [ ] Content moderation integrated
- [ ] Prompt injection test cases
- [ ] PR submitted"""
            },
        ],
        4: [
            {
                "title": "Complete GenAI Application",
                "difficulty": "hard",
                "labels": ["week-4", "final", "fullstack"],
                "body": """## Task Description
Build a complete GenAI application combining your work from Weeks 1–3.

## Suggested App Ideas
- **StudyBuddy**: RAG chatbot that answers questions from your study PDFs
- **Code Reviewer**: Paste code, get line-by-line review and suggestions
- **Resume Analyzer**: Upload resume + job description, get match score and feedback

## Requirements
- Frontend: React or Streamlit
- Backend: FastAPI
- Features: Chat, history, file upload (if applicable)
- Deploy to Render or Hugging Face Spaces

## Acceptance Criteria
- [ ] Full app deployed and accessible
- [ ] Live URL in `PROGRESS.md`
- [ ] PR submitted"""
            },
            {
                "title": "LLM Cost Optimization",
                "difficulty": "medium",
                "labels": ["week-4", "optimization", "cost"],
                "body": """## Task Description
Analyze and reduce LLM API costs in your application.

## Requirements
- Log all API calls: tokens used, cost per call, response time
- Implement caching: same prompt → return cached response (Redis or dict)
- Compare: GPT-4o vs GPT-4o-mini vs Claude Haiku for your use case
- Document cost savings

## Acceptance Criteria
- [ ] Logging implemented
- [ ] Caching reducing costs (show before/after token counts)
- [ ] Cost comparison table in `PROGRESS.md`
- [ ] PR submitted"""
            },
            {
                "title": "GenAI Project Presentation",
                "difficulty": "medium",
                "labels": ["week-4", "presentation", "portfolio"],
                "body": """## Task Description
Document and present your GenAI internship project.

## Requirements
- Project write-up: problem, solution, tech stack, challenges (min 500 words)
- Architecture diagram of your application
- Record a 3–5 minute Loom demo
- Add to your LinkedIn/GitHub portfolio

## Acceptance Criteria
- [ ] Write-up in `PROGRESS.md`
- [ ] Architecture diagram included
- [ ] Loom demo link included
- [ ] PR submitted"""
            },
        ],
    },
}


def write_task(domain, week, task_num, task):
    folder = os.path.join(BASE, domain, f"week-{week}")
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, f"task-{task_num}.md")
    
    if os.path.exists(filepath):
        print(f"  SKIP (exists): {filepath}")
        return
    
    labels_str = str(task['labels']).replace("'", '"')
    content = f"""---
title: "{task['title']}"
difficulty: "{task['difficulty']}"
labels: {labels_str}
---

{task['body']}
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  CREATED: {domain}/week-{week}/task-{task_num}.md")


total = 0
for domain, weeks in TASKS.items():
    print(f"\n=== {domain.upper()} ===")
    for week, task_list in weeks.items():
        for i, task in enumerate(task_list, 1):
            write_task(domain, week, i, task)
            total += 1

print(f"\nDone! Created {total} task files.")
