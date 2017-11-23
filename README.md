## My OSS Contribution

- I found [TemPy](https://github.com/Hrabal/TemPy) via [Up for Grabs], one of the sites suggested by [Katrina Owen].
- I chose this project for its familiar and relatively simple code and its openness to small, basic contributions.
- It is a very active project, the latest commit was less than a day from the time of my typing here.
- After running a sample code from the readme, I decided to contribute by editing that part of the readme such that the given code and expected output more correctly matched.

Documentation

After creating and cloning the [fork](https://github.com/SYctonu/TemPy):

![forked TemPy](/images/forkedTemPy.PNG)

![cloned fork](/images/clonedFork.PNG)

I copied the sample code for ["basic usage"](https://github.com/SYctonu/TemPy#basic-usage) to test on Python 3.6:

![sample code test](/images/sampleCodeTest.PNG)

TemPy did not render the HTML as shown in readme:

![actual render](/images/sampleRender.PNG)

So I modified my copy to better reflect the expected output:

![updated code](/images/modifiedCode.PNG)

The updated code successfully rendered the correct HTML tags...

![new render](/images/modRender.PNG)

but getting it to render them in the structured format remained a mystery.

Still, it was enough of an improvement for me to proceed.

I created and switched to a local branch,

![readme-edit branch](/images/branch.PNG)

found the section,
![before](/images/beforeEdit.PNG)

and applied my changes:
![after](/images/afterEdit.PNG)

![commit](/images/commit.PNG)
    
