# daily-markdown-todoist-appender

As an avid user of both logseq and obsidian, I work with markdown files quite often. They have become my main tool for note-taking, scheduling, and keeping track of my life. One of the reasons I'm so obsessed with the format is because of how much control you have over it. I was introduced to outliners through workflowy. I loved workflowy so much for many years, but I became frustrated because of how limited it could be. 

One of the things I wished I could do with Workflowy was to automatically add my todoist tasks as bullets at the beginning of the day. This is possible in workflowy with a separate app named zapier, but would have required me to pay for it. I thought that was silly so I came up with a solution I liked better. I transferred my Workflowy notes to logseq, connected my logseq to an obsidian account I was already using, and made this script. That might seem like a lot of effort but the result for me has been a system that I have much more control over, which is important for me. 

# what this script does

I use this script to automatically add my todoist tasks to the beginning of my markdown files every day at 4:00 a.m. 

To get this script to work you'll need to - 
1. Update where it says **___PATH TO FILE___** to the path of the markdown file you'd like to add to. 
2. Update where it says **___API TOKEN___** to your todoist api token - https://todoist.com/help/articles/find-your-api-token-Jpzx9IIlB
3. Schedule the script to run at the times you want. This can be done using the windows task scheduler, apple automator, or with cron commands on linux.

Something else to note is that the default content I've added is in a bullet list format which is required for my chosen app logseq, but if you are working in other apps that don't require bullets for every line you can get rid of the "- " at the beginning of each item you're adding. 

<3 Terra