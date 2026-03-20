# How to set the Canonical tag? Stop having multiple pages pointing to the homepage, these 5 situations will be handled more effectively

> Language: Chinese | Region: China/Global | Keywords: How to set up canonical tags, canonical tags, how to use canonical, canonical tags, duplicate page SEO, page inclusion optimization, website index, technical SEO

**Keywords**: How to set up canonical tags, canonical tags, how to use canonical, canonical tags, duplicate page SEO, page inclusion optimization, website indexing, technical SEO, duplicate content processing, URL normalization, inclusion issues, Search Console

---

## Why do many websites point canonical to the homepage first when there is an inclusion problem?

I have seen this trap too many times.

The webmaster was a little anxious because the page was not included, so he opened the backend and made some changes, and finally it became:

- The article page points to the homepage
- Category page points to home page
- The parameter page points to the home page
- Even product pages point to the homepage

On the surface, it seems to be "unifying the weights."

But the actual effect is often: **Search engines will become increasingly confused about which page you want to be regarded as the main page. **

The tag canonical was originally used to tell search engines:

**"The contents of these pages are very similar, please treat this page as the official version first."**

It is not a universal repair button, nor is it a tool to blame the home page whenever there is a problem with the page.

So if you happen to be studying how to set up canonical tags recently, let me give you the conclusion first:

**canonical What I fear most is not not being able to write, but writing indiscriminately. **

---

## What exactly does canonical do? Don’t confuse it with 301 or noindex.

When many people come into contact with canonical for the first time, they are most likely to be confused with these two things:

- **301 Redirect**
- **noindex**

They are not the same thing.

### 1.canonical
means:
**This page is accessible, but I would rather you think of the other page as the master version. **

### 2. 301 Redirect
means:
**This page has moved, you can go directly to the new address. **

### 3. noindex
means:
**You can crawl this page, but do not put it in the index. **

So canonical is not "deleting the page", nor is it "forced to jump to the page".

It's more of an "archive note".

You are telling search engines:

> The content of these pages is almost the same. The main version that should be collected is this page.

If you don't even understand this premise, it will easily become more confusing later.

---

## How to set the canonical label? I recommend looking at these 5 common scenarios first

### 1. The same page only has different parameters. This is the most suitable to add canonical.

This is the most common and standard usage.

For example, on the same page, these addresses may appear due to statistical parameters, advertising parameters, and sharing parameters:

- `/seo-tools`
- `/seo-tools?utm_source=x`
- `/seo-tools?from=twitter`
- `/seo-tools?session=123`

The content users see is almost the same, just the URL is different.

The most stable approach at this time is usually:

**All parameter pages canonical return to the main URL. **

That is to say, unified pointing:

`/seo-tools`

In this case, it is easier for search engines to understand and least likely to cause trouble.

---

### 2. The sorting page, filtering page and original list page are highly repetitive. You can consider canonical returning to the main list page.

E-commerce sites, tool catalog sites, and content sites often have pages like this:

- Sort by price
- Sort by latest
- Filter by color
- Filter by region

The problem is:
Some filter pages actually bring no new search value, but just change the display order of the same content.

For example:

- `/plugins`
- `/plugins?sort=latest`
- `/plugins?sort=popular`

If the core content of the pages is similar and there is no obvious difference in search value, then you can consider canonicalizing the sorting page to the main list page.

But here’s something to note:

**Not all filter pages should be canonicalized back. **

If a filter page itself has clear search needs, such as "SEO plug-ins suitable for independent sites" or "free AI plug-ins", then it may be worth existing separately instead of being merged.

So don't do it mechanically. First check whether this page has independent value.

---

### 3. If there are multiple URLs for the same piece of content, only one main version must be explicitly retained.

This problem is particularly common in blogs, CMS, and revision sites.

For example, the same article may appear simultaneously in:

- new link
- old link
- Links with category paths
- Links without category path
- Two versions with and without slashes

The content is clearly one article, but there are several URLs.

If this is not done, the search engine will have to guess:
Which one is the official page?

The most important thing you should do is to first select a URL that you really want to keep for a long time, and then:

- Try your best to 301 if you can 301
- It cannot be jumped for the time being, at least canonical is unified to the main version.

Don’t use A today, B tomorrow, and C a few weeks later.

**Canonical This kind of thing is most afraid of your own instability. **

---

### 4. Similar product pages and similar landing pages should not be combined into one just because they are “similar”

There are many pitfalls.

For example, you have these pages:

- black running shoes
- white running shoes
- Women's running shoes
- Wide running shoes

They all looked very similar, so someone went directly to the "running shoe homepage" of Canonical.

The result is:
The page that could have separately covered the subdivided search terms was suppressed by you yourself.

My own judgment criteria are simple:

**If when users search this page, they expect to see different content, different information, and different purchasing decisions, don’t mix it up. **

Canonical is more appropriate only when these pages are really only slightly repetitive, the main content is almost the same, and the independent value is weak.

Otherwise, you are not standardizing, but actively cutting off long-tail traffic entrances.

---

### 5. The page has been updated and the old page is no longer going to be retained. Use 301; do not use canonical hard top.

There is one situation where it is most likely to be used incorrectly:

The old page is obsolete and the new page has completely replaced it.

At this time, many people are too lazy to make a jump, so they add a canonical to the old page to point to the new page, thinking it is "almost".

Not exactly the same.

If there is no need to keep the old page and you want users to go directly to the new page when they visit the old page, it is usually more appropriate:

**301 redirect instead of just writing canonical. **

Because the premise of canonical is that the old page still exists, it just tells the search engine "please focus on that page".

And 301 is clearly expressing:

**This page has officially been moved. **

Many people don't pay attention to this difference at ordinary times, but they will be very embarrassed when checking the index and weight later.

---

## I think these four canonical mistakes are more harmful than not writing.

### Mistake 1: All pages point to the homepage

This is the most common form of rough handling.

The problem is that the homepage, article pages, product pages, and category pages are not originally search intent.

When you point a bunch of pages back to the homepage, you are telling the search engines:

"None of these pages are important, it's the homepage that's important."

Don’t be too surprised if many long-tail words cannot be used.

---

### Mistake 2: The content of the page is much different, but the same canonical is still written

canonical is not meant to merge "completely different topics".

If the topics, user intentions, and keyword directions of the two pages are all different, but they are just slightly related, then you shouldn’t point them randomly.

The search engine does not just see that you have written canonical and just follow it, it will also judge the similarity of the content by itself.

If you write randomly, many times it won't do what you mean.

---

### Mistake 3: canonical points to 404, jump pages, or even noindexed pages

This is a low-level pitfall that is most easily overlooked in technology.

The target page pointed to by canonical should preferably meet these conditions:

- Can be opened normally
- Status code is normal
- Not 404
- Not the address after multi-level jumps
- not noindexed

Otherwise, you are giving the search engine a very vague or even wrong instruction.

---

### Mistake 4: Canonical on one side and give opposite signals on the other.

For example:

- The page writes its own self-reference canonical
- Another URL was submitted in the sitemap
- Most internal links point to the third URL
- hreflang, redirect, canonical fight each other

This situation is the most troublesome.

Because what the search engine finally receives is not a clear conclusion, but a bunch of conflicting tips.

**Really effective canonical is not to write a single point correctly, but to not undermine each other in the entire set of URL signals. **

---

## If you want to check canonical now, this list is enough

When I do my own troubleshooting, I usually look in this order:

### Step one: Does this page have independent search value?
If so, don’t canonical it to another page easily.

### Step 2: Is this page highly similar to the target page?
If they are somewhat similar but actually solve different problems, don’t merge them.

### Step 3: Is the target page stable, accessible, and capable of inclusion?
Don’t point to 404s, redirect links, or noindex pages.

### Step 4: Are other signals in the site consistent?
Check the sitemap, internal links, navigation, and redirects to see if there are any conflicts.

### Step 5: Canonical scenarios, don’t just write canonical
The old page has been retired, so don’t leave it half-dead.

Looking at these 5 steps, most canonical problems can actually be pinpointed.

---

## My more common approach now: straighten out the URL relationship first, and then talk about canonical

To be honest, many websites have canonical problems, not because the tags themselves are difficult, but because the URL structure was not thought out clearly from the beginning.

For example:

- The same content can generate three or four types of links
- Category paths change frequently
- Coexistence of old and new URLs
- Parameter rules are confusing
- Templates and plug-ins automatically generate a bunch of duplicate pages

Even if you patch canonical on every page of this kind of site, you will just keep patching it later.

So now I prefer to do this first:

**First think clearly about "which pages should exist, which pages should not exist, and which pages should be merged." **

After thinking about it clearly, canonical will become a very convenient organizing tool.

Otherwise it can easily be used as a fire extinguishing tool.

---

## Write at the end

How to set the canonical label is actually not as mysterious as imagined.

The difficulty is not how to write the code, but whether you can judge clearly first:

- Which pages are really duplicates
- Which pages are just similar but should be kept
- Which pages should be canonical
- Which pages should actually be 301

I feel more and more now that the core value of canonical is not "transfer weight", but:

**Let search engines know more clearly which page of your website is the official version. **

As long as this idea is clear, many problems such as slow collection, duplicate pages, and chaotic indexing will be much easier to deal with than before.

If you happen to be checking for inclusion recently, don’t just check whether canonical has written it.

What's more:

**Is it written to the right page? **

---

**Related searches**: How to set up canonical tags, canonical tags, how to use canonical, canonical tags, duplicate page SEO, page inclusion optimization, website indexing, technical SEO, duplicate content processing, URL normalization, inclusion issues, Search Console
