## What's this? 
- It is capable of efficiently extracting data from the Product Hunt website within daily, weekly, monthly and annual time periods.
- Including various metadata such as names, descriptions, categories, likes, multiple manufacturers, contact links, etc. 
- The running speed is extremely fast, requiring only a small amount of time and memory, and the operating cost is very economical.
- It is highly suitable for market research, competitive analysis and trend monitoring, and can provide reliable and structured data output, optimizing it for commercial intelligence applications.

## Your gains
- Efficient data extraction in multiple time dimensions: can efficiently extract data from the Product Hunt website within daily, weekly, monthly and annual time periods to meet the analysis needs of different time spans.
- Supports flexible control of data collection range and scale through parameters such as cycle, date, week, and limit to meet diverse needs.
- Comprehensive and rich metadata coverage: The extracted data includes complete metadata such as product name, description, category, number of likes, multiple manufacturer information and various contact links, providing a basis for in-depth analysis.
- Professional business intelligence application adaptation: highly suitable for market research, competitive analysis and trend monitoring scenarios, providing optimized and reliable structured data output.
- Comprehensive product performance indicators: the output includes latest_score, launch_day_score and other multi-dimensional scoring data to help analyze product popularity and growth trends.
- Complete social media footprint: Automatically extract links from multiple social media platforms such as Twitter, LinkedIn, and Facebook to facilitate social media influence analysis and competitive product social marketing strategy research.
- Detailed manufacturer network analysis: Contains detailed information (name, position, avatar, etc.) of all manufacturers for each product, which can be used to analyze entrepreneurial team composition and talent distribution trends.
- Technology stack analysis capability: Provides built_with field to clearly display the technical components used in the product and their evaluation, which is helpful for technology trend research and technology selection reference.
- Multimedia resource integration: including logo_url and media_list, providing product visual information to facilitate brand visual analysis and competitive product design research.

## Input & Output Struct
### 1、Input
- cycle: Data Cycle, For example: day, week, month, year
  - day: https://www.producthunt.com/leaderboard/daily/2025/11/12/all
  - week: https://www.producthunt.com/leaderboard/weekly/2025/46/all
  - month: https://www.producthunt.com/leaderboard/monthly/2025/11/all
  - year: https://www.producthunt.com/leaderboard/yearly/2025/all
- date: Date, For example: 2025-11-05
- week: Week of year, You need to enter date, and the year will be taken. range: 1-52, For example: 1
- limit: The maximum quantity obtained, the larger the quantity, the longer the time

Note: You can try it out for free and see what it outputs, Hope he can bring you value.

### 2、Output Struct
```json
[
  {
    "id": "747127",
    "name": "GitLaw",
    "slug": "gitlaw",
    "tagline": "Agent + templates + workflow. Making legal documents free.",
    "latest_score": 179,
    "launch_day_score": 178,
    "created_at": "2025-11-05T00:01:00-08:00",
    "daily_rank": "5",
    "weekly_rank": "16",
    "monthly_rank": "569",
    "comments_count": 22,
    "product_url": "https://www.producthunt.com/products/gitlaw",
    "topics": [
      "Productivity",
      "Legal",
      "Operations"
    ],
    "website_url": "https://git.law",
    "ios_url": null,
    "android_url": null,
    "github_url": null,
    "twitter_url": "https://x.com/gitlawco",
    "facebook_url": null,
    "instagram_url": null,
    "linkedin_url": "https://www.linkedin.com/company/gitlawco/",
    "angellist_url": null,
    "threads_url": null,
    "medium_url": null,
    "followers_count": 432,
    "posts_count": 2,
    "discussion_url": "https://www.producthunt.com/p/gitlaw",
    "description": "Chat with GitLaw’s agent to draft or review legal documents in minutes. We're making legal documents free for millions of businesses.\n\nBuilt for Legal Work\nThinks like a lawyer, using structured reasoning for higher accuracy than generic AI tools.\n\nTrusted, open-sourcing templates \nWe've indexed thousands legal templates - combining accuracy, context, and speed. \n\nOne Seamless Workflow\nTracked changes and version control, smart reminders, all in one place.\n",
    "reviews_count": 0,
    "featured_shoutouts_to_count": null,
    "logo_url": "https://ph-files.imgix.net/5f04c042-55d3-45e4-af99-7a8754e9c03f.png",
    "launch_state": "featured",
    "website_domain": "git.law",
    "product_state": "default",
    "featured": true,
    "featured_at": "2025-11-05T00:01:00-08:00",
    "media_list": [
      {
        "id": "2526004",
        "url": "https://ph-files.imgix.net/6b091c27-e72e-4020-afb8-a1e75b47a966.png",
        "media_type": "image",
        "original_width": 1262,
        "original_height": 828
      },
      {
        "id": "2526003",
        "url": "https://ph-files.imgix.net/aaded0a5-a786-4c71-b8e9-cf5f5b145a4e.png",
        "media_type": "image",
        "original_width": 1262,
        "original_height": 828
      },
      {
        "id": "2526002",
        "url": "https://ph-files.imgix.net/f8111597-c2ed-4450-beba-678b4018727f.png",
        "media_type": "image",
        "original_width": 1262,
        "original_height": 828
      }
    ],
    "screenshots": [],
    "makers": [
      {
        "id": "992317",
        "name": "Rostyslav Khrinovskyi",
        "headline": "Backend Developer",
        "username": "rossof_rostislav",
        "avatarUrl": "https://ph-avatars.imgix.net/992317/original.jpeg",
        "homepage": "https://www.producthunt.com/@rossof_rostislav"
      },
      {
        "id": "9108033",
        "name": "Enoch Kambale",
        "headline": "building what's next",
        "username": "enkambale",
        "avatarUrl": "https://ph-avatars.imgix.net/9108033/original.jpeg",
        "homepage": "https://www.producthunt.com/@enkambale"
      },
      {
        "id": "2615189",
        "name": "Max Kostuchenko",
        "headline": "Tech problem generator",
        "username": "kstmaks",
        "avatarUrl": "https://ph-avatars.imgix.net/2615189/07d6a995-c317-48e6-a01d-819cafff7ebc.jpeg",
        "homepage": "https://www.producthunt.com/@kstmaks"
      },
      {
        "id": "149492",
        "name": "Viktor Taranenko",
        "headline": null,
        "username": "viktortnk",
        "avatarUrl": "https://ph-avatars.imgix.net/149492/original.jpeg",
        "homepage": "https://www.producthunt.com/@viktortnk"
      },
      {
        "id": "5557619",
        "name": "Nick Holzherr",
        "headline": "Investor & CEO",
        "username": "nickholzherr",
        "avatarUrl": "https://ph-avatars.imgix.net/5557619/original.jpeg",
        "homepage": "https://www.producthunt.com/@nickholzherr"
      },
      {
        "id": "7845133",
        "name": "Siân Allmark",
        "headline": "Growth Marketing Strategy & Activation",
        "username": "sian_allmark",
        "avatarUrl": "https://ph-avatars.imgix.net/7845133/433334bf-34bb-4c19-80b2-171f835bcb91.png",
        "homepage": "https://www.producthunt.com/@sian_allmark"
      },
      {
        "id": "9098143",
        "name": "Ankit Sinha",
        "headline": "Solving Access to Justice, ex-lawyer",
        "username": "sinhaankit",
        "avatarUrl": "https://ph-avatars.imgix.net/9098143/56909347-49a5-411f-be92-d43b9736061c.png",
        "homepage": "https://www.producthunt.com/@sinhaankit"
      },
      {
        "id": "9098129",
        "name": "Lottie Hutchins",
        "headline": "PR Director & Consultant",
        "username": "lottiehutchins",
        "avatarUrl": "https://ph-avatars.imgix.net/9098129/original.jpeg",
        "homepage": "https://www.producthunt.com/@lottiehutchins"
      },
      {
        "id": "2271318",
        "name": "Igor Korshunov",
        "headline": "Tech problems solver",
        "username": "igor_korshunov",
        "avatarUrl": "https://ph-avatars.imgix.net/2271318/0ebc464e-3d91-4771-80e6-7d40978ff2b7.jpeg",
        "homepage": "https://www.producthunt.com/@igor_korshunov"
      }
    ],
    "built_with": [
      {
        "id": "364261",
        "slug": "langsmith",
        "name": "LangSmith",
        "tagline": "Build and deploy LLM applications with confidence",
        "product_url": "https://www.producthunt.com/products/langsmith",
        "logo_url": "https://ph-files.imgix.net/7c436514-299e-40cf-87a4-543b7f3dfd30.png",
        "overall_experience": "Evals / tracing / monitoring is awesome and out of the box"
      },
      {
        "id": "390400",
        "slug": "gemini-6",
        "name": "Gemini",
        "tagline": "Google's answer to GPT-4",
        "product_url": "https://www.producthunt.com/products/gemini-6",
        "logo_url": "https://ph-files.imgix.net/99b3e788-14c7-4bbb-97ea-d87c23c9318f.png",
        "overall_experience": "Incredible frontier model"
      },
      {
        "id": "364262",
        "slug": "langchain",
        "name": "Langchain",
        "tagline": "LangChain’s suite of products supports AI development",
        "product_url": "https://www.producthunt.com/products/langchain",
        "logo_url": "https://ph-files.imgix.net/35b92c0d-5cc6-499a-b2cf-9d25d3e9538b.png",
        "overall_experience": "Awesome tooling to build agents"
      },
      {
        "id": "288205",
        "slug": "openai",
        "name": "OpenAI",
        "tagline": "APIs and tools for building AI products",
        "product_url": "https://www.producthunt.com/products/openai",
        "logo_url": "https://ph-files.imgix.net/f904aec8-e324-4aed-ae3b-ff68795ce44f.png",
        "overall_experience": "Incredible frontier model"
      },
      {
        "id": "364260",
        "slug": "claude",
        "name": "Claude by Anthropic",
        "tagline": "A family of foundational AI models",
        "product_url": "https://www.producthunt.com/products/claude",
        "logo_url": "https://ph-files.imgix.net/ae49ce7d-30a4-457b-823a-2e1ee8d44dbb.png",
        "overall_experience": "Incredible frontier model"
      }
    ],
    "introduction": "Hey ProductHunt community,\n\nI'd love to hear what you think about GitLaw. \n\nGitLaw offers free, open-source legal templates with Git-powered collaboration and version control.\n\nWe have over 300 documents today and hope to receive many more. Employment contracts, NDAs, SaaS agreements, Privacy Policies etc - all free. \n\nDocs exist - why GitLaw?\n- Existing templates are often low quality and cost money. \n- Using Git, we’re enabling the community to build \"open standards\" together. \n- Smart input fields that automatically fill in the contract fields and simple on/off or variant selection for clauses makes it simple to customize and use templates on GitLaw \n- A private workspace for your documents (we’ve got a lot more stuff to build here)\n\nIsn’t AI coming to eat legal?\n- Well, yes. People already use tools like ChatGPT to generate docs. But the general consensus is that while LLMs are amazing - trusted templates are a much more reliable base. \n- AI presents a significant opportunity to help people *use* legal templates - but a template repository is a helpful foundation. We believe the time is right for GitLaw to exist.\n- Our plan is to add a Co-Pilot in the future - an AI chatbot to act as a quasi paralegal to help summarize or adapt documents. We also think AI agents can help make legal documents much faster/easier to create / review / sign.\n\nHow is GitLaw going to make money? \n- Everything we have will remain free. \n- Once server costs start to add up we might add a paid option for additional features - for example - the latest LLM models for a small monthly fee and referring lawyers through a marketplace when a human is needed. \n\nWe’ve built this as a fun side project with no funding."
  }
]
```

## Feedback
We will always iterate its functions, including launching new features and fixing known bugs. If you encounter any problems during use, please create an issue in the Issues section in a timely manner, and we will follow up and solve it promptly.
