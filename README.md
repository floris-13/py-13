# Project py-13

```
                         .o    .oooo.   
                       o888  .dP""Y88b  
oo.ooooo.  oooo    ooo  888        ]8P' 
 888' `88b  `88.  .8'   888      <88b.  
 888   888   `88..8'    888       `88b. 
 888   888    `888'     888  o.   .88P  
 888bod8P'     .8'     o888o `8bd88P'   
 888       .o..P'                       
o888o      `Y8P'
```

Easy to use Templating Engine, that generates static websites from Markdown - written in Python.

## Why Floris, why? Kind of manifesto.

### The current web

**The current web ist technically bloated, mostly driven by commercial interests and very fast and clickbaity**. And this all plays together, of cause:

To make a high level and state of the art website these days, you have, let's say, a *Single Page Application*, a backend of *Microservices* and whatever *Services* connected to them, you have some kind of *Content Management System* and ways to feed it, you have *Identity and Access Management*, that users can login and -out, you have the whole tech stack of *Continuous-Integration* and -*Delivery* including tools to *build*, *linter*, *version* and what not, you have *Cloud Technologies* and *Containers* and I'm only scratching the surface here, not speaking yet of *UI/UX*, *Testing*, *Social Media Integration*, *Payment*, *Legal*, you name it.

This  can easily cost Euro-millions in the making and then every year again for maintaining and redesign. Technologies change every year. Obviously you cannot hope to make this as a single developer, but it sets the standard, it is the bar you are reaching out for.

**People expect the web to look like this now.**

To be fair, tools are getting better, but they also become more complicated. Often times you don't need and should not code anymore, but instead you configure your way through. It's not fun anymore, it's work. And people do it for money. To sell cars or ads or themselves as a brand in social media.

And even to use these websites is not fun, it's boring, it's work. They are made, so that you can do some paperwork for your insurance or buy a car, book a flight or look up what to do against your cat's fleas - you are there to do something, some commercial interaction, not to just be there.

And on Social Media the user is the product, squeezing out every possible minute of specific attention to sell to advertisers. Obviously as much fun as taking part in large-scale livestock farming. And when you are a content creator, your financial well being can end up with finger snapping of the platform you are on.

**It's not fun to make or use these websites or content, it's work.**

Sorry to be so negative .. but change is coming:

### The future web

Already are the dinosaurs eaten by new dinosaurs. For some years now people say, that *smartphone apps* are the new web and that's kind of true. Even more segmented then the current web already is.

And *AI*, of cause, the *Zero-Click-Web*, means: Users find what they are looking for already *inside the search engine*, no need to click any of the given links. No need even to show links any more. The answer given by the search engine may not be good - but good enough for most people. In the Zero-Click-Web the websites only feed AI language models and don't sell ads anymore, because no one clicks them. If someone makes a travel-blog that pays through ads or collections of recipes, small web tools, that pay through ads, those will fade.

Soon your *AI concierge* will do insurance paperwork for you, will provide commercial entertainment that you enjoy and choose from, then buy that chosen car or book that preferred flight and the flea medication will be in front of your door next day.

Oftentimes  people will choose to buy on the websites anyway. Less visitors, but higher conversion rate. People already know, why they are here. If you sell something, at least in the near future, not so much will change and your website will still make sense.

**Tl;dr: Sorry, but the future web will be even more commercial than the current web already is.**

But change ist coming (again):

### The Indie Web

The *Indie Web* is what people imagine that the web was in the 1990's. A little bit of romanticising and a whole lot of truth. And websites like http://neocities.org celebrate that.

But it's not the 1990's any more, so what can the Indie Web mean today?

- **You surf the web for fun**, start on one site, explore it, find interesting things and hidden secrets .. and find another website .. and another. They are all connected, it's like a real web!
- It's basically **non-commercial and ad-fee**. If your site does not comply with this rule, no one will link to you, it's as easy as that.
- **There is no controlling entity except the law.**
	- For the creator: No Facebook, YouTube, TikTok or X, **no one can control what you say or block you from your audience**. Your content is yours.
	- For the visitor: **You decide, where to go, which rabbit hole to follow.** No Facebook, YouTube, TikTok or X can feed and fatten you with ads and mindless stuff. 
- The websites are **technically simple**, means, they are static websites - you click and they load a new page - they contain a lot of HTML, low level CSS and just a little bit of JS, if at all. Sometimes as simple as Gopher Protocol was or Gemini Protocol is. Or very different from that:
- They are **individually designed**. Sometimes just text with links - often times very colourful and blinking and completely overloaded, 1990's style, visit Neocities, then you know, what I mean.
- **They are basically everything, the current web is not (any more).**

### Very interesting .. but why Project py-13 again?

This now is about me. **I own and care for some websites.** It was a lot of work to make them - and now it is a lot of work to maintain them. When I first heard of the Indie Web and this spark ignited, I thought:

- I want my private websites to be much more fun to make an visit.
- I want my commercial websites to be a lot easier to maintain.

For many years now **I already use Markdown**, especially Obsidian to textify my life, ideas and projects. So I imagined a button to click and **convert parts of my Markdown documents into simple websites**.

This idea evolved: First I thought, **a simple Python script** can do the job. It did the job, sort of. But I wanted more .. a lot more to implement - fun though, but aren't there already many frameworks and templating engines, that already exist?

I looked around and found 11ty, maybe that's something. Pro: I'm a fullstack developer for many years now. Con: I was quite tired already. Anyway, I looked into the documentation an did't understand anything. Too much, too complicated, too JavaScript. I'm sure 11ty is very useful for many people .. but me .. I  just don't like it.

I wanted something like 11ty, but easier to understand for the user (including me and future-me) and more focussed on the Indie Web. And I wanted it in Python, a language I am just starting to learn. This is, where the name **py-13** comes from: 11ty + Python + newer + different.

I decided to make it open source, for everyone to use, but it's still a hobby project, so please be kind don't expect too many commits per month. And as I said, please don't expect perfect Python code yet.

And this is also the reason why I write here so much: I don't have a tool yet to convert my Markdown into HTML to put in on a website - so i put it into this README-file. As a starting point, motivation an d manifesto. No line of code written yet, I will start from scratch.

## Some key features of py13

- All source files are of type `.md`

## Feature list of upcoming Version 1.0 (MVP)

- [ ] Specify (not generate yet) a **py-13** Project directory
- [ ] Convert Markdown files to HTML within this directory
- [ ] Generate Header & Footer, no templates yet
- [ ] Generate a very simple Menu system, no templates yet
- [ ] HTML is valid W3C Markup
- [ ] Generated files can be run in a browser without a server (if that is still possible)
- [ ] Write a simple documentation for Version 1.0
