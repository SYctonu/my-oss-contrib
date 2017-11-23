## My OSS Contribution

- I found [TemPy](https://github.com/Hrabal/TemPy) via [Up for Grabs](http://up-for-grabs.net/#/), one of the sites suggested by [Katrina Owen](https://github.com/collections/choosing-projects).
- I chose this project for its familiar and relatively simple code and its openness to small, basic contributions.
- It is a very active project, the latest commit was less than a day from the time of my typing here.
- After running a sample code from the readme, I decided to contribute by editing that part of the readme such that the given code and expected output more correctly matched.

Before creating and cloning the [fork](https://github.com/SYctonu/TemPy):

![cloned fork](/images/clonedFork.PNG)

I copied the sample code for ["basic usage"](https://github.com/SYctonu/TemPy#basic-usage) to test on IDLE, a Python 3.6 editor:

![sample code test](/images/sampleCodeTest.PNG)

TemPy did not render the HTML as shown in the readme:

![actual render](/images/sampleRender.PNG)

So I modified my copy to better reflect the expected output:

![updated code](/images/modifiedCode.PNG)

The updated code successfully rendered all the correct HTML tags in the desired order...

![new render](/images/modRender.PNG)

but getting it to render them in the structured format remained a mystery.

Still, it was enough of an improvement for me to proceed.
I created and switched to a local branch,

![readme-edit branch](/images/branch.PNG)
![switch](/images/switchedBranch.PNG)

found the section,
![before](/images/beforeEdit.PNG)

applied my changes,
![after](/images/afterEdit.PNG)

committed, and pushed to my fork on GitHub:
![commit](/images/commit.PNG)

With a readme that now has what should be a more accurate usage example, I made a [pull request](https://github.com/Hrabal/TemPy/pull/32).