# Language in Multicultural — revised study edition

A static, offline-capable study website based on five supplied lecture decks (103 slides). This edition includes 839 explained MCQs, 238 comparative glossary entries, five expanded essays totaling 5,759 words, ten written-answer models and a traceable slide coverage map. Practical examples include hypothetical Pakistani families, classrooms and clinical encounters alongside global illustrations.

## Start or deploy

Open `index.html` directly, or serve this directory using `python -m http.server 8000`. No installation, API key, account or build is needed. For GitHub Pages, upload the contents to the repository root, then choose Settings → Pages → Deploy from a branch → main → / (root). The ZIP includes `.nojekyll`. This package does not itself publish a live website.

## Learning route

1. Read a module essay and attempt its written-answer prompts before opening the models.
2. Open Key concepts for definitions, worked examples, explanation of why each example fits, related-concept comparisons and retrieval practice.
3. Use Practice MCQs for instant feedback. Read the explanation and option reasoning before continuing.
4. Return to wrong answers and bookmarks; use topic and difficulty filters as needed.
5. Use Mock exam for 25, 50 or 100 questions with answers withheld until submission. Review the result by module, then return to the relevant concepts.

Ordinary practice supports 10/20/50/100 items per page, smooth question/page navigation, direct links, search and saved resume position. A final page can contain fewer items. The website has day/night themes, distinct module colors, local colorful vector icons, readable controls, essay text-size adjustment and responsive layouts.

## The exam bank

The bank contains 714 concept-focused items and 125 newly authored exam-style cases. The concept items support recall, application and misconception recognition. The case pool includes profile interpretation, scoring, evidence appraisal, clinical reasoning, comparisons and a contextualized statement-pair item. Questions progress by editorial difficulty within each module. Difficulty labels have not been calibrated through student performance data.

Mock exams draw equal numbers from all five modules, using only the 125 case questions. They are untimed. Each correct answer earns one point; wrong or unanswered questions earn zero. Selected answers enter saved course progress once on submission. Unanswered items do not count as attempted in course progress. Test lengths and scores do not predict the format or pass mark of a particular institution. These are original learning items, not official past-paper or endorsed professional-board questions.

## What was revised

The repeated two-statement template and earlier integrated-case set were retired. The revised edition adds focused cases, stronger rationale, comparisons and 83 expanded worked examples. Four clarifying concepts address language choice, multiple levels of language, semantics and regional labels within Hindko. Essays now connect labels to practical reasoning and written examination answers. Every supplied slide is accounted for in the website's coverage map and `SLIDE_AUDIT.md`, including notes, images, orientation and closing material.

## Progress and upgrades

Course progress remains browser-local and separate from the Speech and Language Sciences and Research Methodology websites. Retained question IDs keep their canonical option indices. Answers and bookmarks for retained items remain usable; retired questions are omitted from current scoring and queues. Export an old-edition backup before replacing your deployed files if you want to retain that earlier history separately. There is no automatic cross-device sync. Clear browser data only after exporting any progress you need.

Mock-exam drafts save separately on this browser; they are not part of the ordinary progress export. Changing answers is allowed before submission. Submission locks the test and prevents repeated scoring. A new test may include previously encountered cases. Clearing browser storage removes both course progress and local test drafts.

## Sources and coverage

See the Reading guide, `COVERAGE.md` and `SLIDE_AUDIT.md`. Simplified and unsupported slide claims are explicitly qualified. Recommended book editions were verified through publisher or bibliographic records and accessible descriptions; complete copyrighted books were not claimed as read. All teaching scenarios are hypothetical. Original slide decks, photographs and copyrighted graphics are not redistributed.

## Rebuild and check

The website is already built. To regenerate its original study data using Python's standard library:

```
python tools/build_all.py
node tests/check.js
node tests/interface.js
node --check app.js
node --check exam.js
```

`tools/base_content.json` and `tools/base_essays.json` retain the authored starting material; the other scripts apply the revised cases, examples, comparisons, slide audit and essay extensions. Keep these together for reproducibility. `data.js`, `essays.js` and `audit.js` allow direct local opening without fetch. JSON copies support editing and inspection. No external package, font, tracker or image request is required for core study. External source links need internet.

Automated checks passed. Actual browser layout and real-device touch/keyboard behavior remain unverified because preview infrastructure was unavailable. See `VALIDATION.md` for the limits of verification.
