# How to write robots.txt? Don’t just disallow a lot of them right from the start. It’s more effective to clarify these 5 rules first.

> Language: English | Region: Global | Keywords: how to write robots.txt, robots.txt settings, robots.txt rules, Disallow, Allow, crawl control, technical SEO, website crawl optimization

**Keywords**: How to write robots.txt, robots.txt settings, robots.txt rules, Disallow, Allow, crawl control, technical SEO, website crawl optimization, search engine crawling, page inclusion, crawl budget, noindex, Search Console, website index

---

## Why do many people change their robots.txt, and the first thing they block is their most important page?

Many people encounter robots.txt for the first time and have similar thoughts in their minds:

- Don’t want search engines to crawl
- I want to block “useless pages” first
- I feel that the stricter the rules are, the safer they will be
- As soon as there is a problem with the inclusion of the page, I want to change it in robots.txt.

Then the most common result is:

- The test directory is not blocked
- The official article directory was blocked instead
- CSS and JS resources are blocked together
- The sitemap was written, but it was stuck by robots rules again.

It seems that you are doing technical SEO, but in fact you are setting yourself up for trouble in many cases.

Because if robots.txt is written incorrectly, it will not affect a certain article, but may affect an entire batch of pages.

So now when I look at how to write robots.txt, I won’t first ask “what else can be blocked”, but first ask:

**Do I want to control crawling, or am I just anxious and want to change something first?**

These two starting points seem to be similar, but the final results are very different.

---

## What exactly does robots.txt do? Don’t misunderstand “no crawling” as “no inclusion”

This is the most confusing step.

Many people think that as long as `Disallow` is written in robots.txt, this page will definitely not appear in the search results.

That's not entirely true.

robots.txt mainly solves:

**Do you allow search engines to crawl this path.**

It is closer to "crawling rules" than "include switch".

You can first separate these concepts:

### 1. robots.txt
means:
**Don't catch this path yet, or catch it according to my rules.**

### 2. noindex
means:
**This page can be crawled, but I don't want it to be indexed.**

### 3. sitemap
means:
**These URLs are the official pages I want you to discover and understand first.**

### 4. canonical
means:
**The contents of these pages are very similar, please use one of them as the main version first.**

You will find that each of these tools has its own purpose.

So if you treat robots.txt as a "universal hidden button", it will be easy to make changes later and become more messy.

One situation in particular is particularly common:

**The page has been discovered by external links. Although you do not allow it to be crawled, it may still appear in the index as a URL.**

So don’t equate robots.txt with “absolutely not included”.

---

## How to write robots.txt? I would rather suggest clarifying these 5 rules first

### 1. Block the functional pages that are really unnecessary to capture first. Don’t block the content directory as soon as you start.

Robots.txt is best suited to handle, usually these paths:

- Backend directory
- Login page
- Shopping cart, checkout page
- Site search results page
- Obvious duplicate parameter pages
- Functional paths that you don’t want to be caught in the test environment

What these pages have in common is obvious:

**They usually don’t exist to get search traffic.**

So you can give priority to limiting the crawling of such pages.

But the most common mistake many people make is to block article directories, category directories, and product directories as soon as they start, thinking that they should "be conservative first."

This is very dangerous.

Because what search engines really need to capture are often these formal content pages.

If you block even the main content and talk about inclusion, ranking, and internal link delivery later, a lot of it will be in vain.

---

### 2. Don’t block CSS, JS, and image resources, otherwise the page may not even be able to render normally.

This trap is really not uncommon.

When someone sees these directories `/assets/`, `/static/`, `/wp-content/`, `/js/`, their first reaction is:

"These are not the main text, please stop them first."

But the problem is that when search engines now crawl pages, they not only look at the HTML text, but also look at whether the page can be rendered normally, whether the layout is complete, and whether the mobile experience is normal.

If you block key resources, this kind of problem is likely to occur later:

- The page can be crawled, but the rendering is incomplete.
- The style is confusing and the location of important content is distorted.
- Mobile experience evaluation affected
- You think there is a problem with the content page, but in fact it is because the resources are not released

So robots.txt is not "blocking the directory name if it doesn't look like the text."

A more stable approach is:

**First confirm whether the resources in this directory will affect the normal display of the page, and then decide whether to block them.**

Especially for websites that rely heavily on front-end, don't try to save trouble in this step.

---

### 3. If you want to prevent the page from being indexed, don’t just rely on robots.txt. You must distinguish between it and noindex.

Too many people use this confusingly.

For example, if you don’t want some pages to appear in the search results, the correct idea is usually not to check robots.txt first, but to look at:

- Should this page be crawled but not included?
- Should this page 301 directly to another page?
- Should this page be canonical to the official version?
- Should this page not exist publicly in the first place?

If you just want to prevent the page from being indexed, in many cases you should prioritize the following:

- `noindex`
- canonical
- Page status code
- Redirect

Rather than putting robots.txt on top of it.

Because once you completely disable crawling, search engines may not be able to get the noindex signal in your page.

This logic may seem confusing to many people when they first hear it, but it is particularly crucial.

**robots.txt solves the problem of "whether to arrest", not "how to collect it after arresting".**

---

### 4. Don’t just use Disallow as a rule. Some directories need to be partially released.

Many people write robots.txt and know an action:

`Disallow`

In fact, what many sites really need is:

**The crawling of large directories is restricted, but individual paths must be released.**

`Allow` will be used at this time.

For example, there are mostly worthless parameter pages in a directory, but there are some static resources, core pages or necessary files that need to be captured. At this time, if only the entire section is blocked, it will be particularly easy to cause accidental damage.

My own habits are:

- Write the big rules you want to protect first
- Replenish the thin path that must be cleared
- Finally, take a few real URLs for testing

It’s not that fewer rules mean more advanced ones, but:

**Can your rules make it possible to "stop what should be stopped and let what should be let go".**

If you just try to save trouble, often the end result is not "cleaner", but "blurr".

---

### 5. Don’t rush to go online after making changes. Test first and then check Search Console and real crawl feedback.

This is a step that I particularly value now.

Many problems with robots.txt are not caused by the inability to write, but rather the lack of verification after writing.

I usually do at least these few things:

- Select a few article page URLs to see if they have been blocked by mistake.
- Select several category pages, parameter pages, and function pages to test separately
- Check whether the URL in the sitemap conflicts with robots
- Check if "Submitted but blocked by robots.txt" appears in Search Console
- If you can read the logs, you can see what the search engine spider has been crawling recently.

You will find that many rules are fine just by looking at the text, but the real URL is revealed.

So don’t think of robots.txt as a “finish it and upload it” file.

It's more like a little valve that needs to be checked all the time.

---

## I will basically avoid these robots.txt writing methods now.

- `Disallow: /` as soon as it comes up
- The official site still retains the interception rules from the test environment period
- Block all CSS, JS, and image directories
- Thinking that “no crawling” means “will never be included”
- The sitemap submitted A, but robots blocked the directory where A is located.
- Multiple environments share a copy of robots.txt, resulting in conflicts between online rules and test rules

The most troublesome part of these problems is:

**You may not necessarily go wrong immediately on the surface, but traffic, rendering, crawling and inclusion will slowly become weird together.**

And this kind of problem often does not drop an article, but a piece.

---

## If you want to check robots.txt now, you can follow these 5 steps directly

### Step 1: First list the types of pages you really want to be crawled
For example, article pages, product pages, category pages, and core topic pages.

### Step 2: List the paths you don’t want to waste your crawl budget
For example, backend, login, shopping cart, search results page, test directory, obvious duplicate parameter page.

### Step 3: Check whether the resource directory has been accidentally damaged
Focus on CSS, JS, images, and interface dependent resources.

### Step 4: Put robots, sitemap, canonical, and noindex together.
Don't let these signals fight with each other.

### Step 5: Test with a real URL before going online, and continue to read the feedback after making changes
Pay special attention to Search Console's blocking prompts and crawl exceptions.

This process is not complicated, but it can really help you avoid a lot of low-level pitfalls.

---

## My most common method now is to let AI do a rule check for me first, and then compare which one is most likely to damage the page accidentally.

The most troublesome thing about files like robots.txt is not that they are long, but that they are thin.

Sometimes a rule seems to be fine, but when it is put into the structure of the entire site, it starts to cause accidental damage.

So when I check now, I will first list this information to AI:

- Main directory structure of the website
- Which pages you want to crawl and which pages you don’t want to crawl?
- Current robots.txt rules
- Basic situation of sitemap, canonical and noindex

Then let me look at different models separately:

- Which rule is most likely to block official content by mistake?
- Which directories should not be blocked?
- Which places may seem trouble-free, but will create pitfalls for later inclusion?

If I want to quickly see the difference in judgment between different models, sometimes I will directly use **AI Comparison** and look at the suggestions given by Claude, GPT, and DeepSeek.

Instead of letting it make the decision for me, I can quickly find out those "accidental damage points that are easy to miss after looking at them for a long time".

In many cases, the difficulty with this kind of technical configuration is not that you don't know how to write, but that you think your writing is very stable, but in fact, if you miss one point, it will affect a large area. **

---

## Write at the end

How to write robots.txt? Now I feel more and more that it is not as simple as "stop a little first and then talk about it".

It's more like answering two questions:

1. **Which content is worthy of search engines’ attention?**
2. **Which paths should not continue to waste crawling resources?**

If you think about these two issues clearly, robots.txt will usually not be messy.

It’s not that the content of many sites is insufficient, or that the sitemap is not submitted, but that the crawling rules themselves block the road in the first place.

So if you are planning to change robots.txt recently, I highly recommend that you don’t rush to write a bunch of `Disallow`.

First, look at page types, resource directories, inclusion targets, and other technical signals together, and then decide which ones should be blocked and which ones should be included.

If robots.txt is written correctly, it will be easier for search engines to crawl the content you really want them to see;
If you write it wrong, the pages you most want to see may be blocked first.

---

**Related searches**: How to write robots.txt, robots.txt settings, robots.txt rules, Disallow, Allow, crawl control, technical SEO, website crawl optimization, search engine crawling, page inclusion, crawl budget, noindex, Search Console, website index
