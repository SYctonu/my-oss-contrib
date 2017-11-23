from tempy.tags import Html, Head, Body, Meta, Link, Div, P, A
my_text_list = ['This is foo', 'This is Bar', 'Have you met my friend Baz?']
another_list = ['Lorem ipsum ', 'dolor sit amet, ', 'consectetur adipiscing elit']

# make tags instantiating TemPy objects
page = Html()(  # add tags inside the one you created calling the parent
    Head()(  # add multiple tags in one call
        Meta(charset='utf-8'),  # add tag attributes using kwargs in tag initialization
        Link(href="my.css", typ="text/css", rel="stylesheet")
    ),
    body=Body()(  # give them a name so you can navigate the DOM with those names
        Div(klass='linkBox')(
            A(href='www.foo.com')
        ),
        (P()(text) for text in my_text_list),  # tag insertion accepts generators
        another_list  # add text from a list, str.join is used in rendering
    )
)

# add tags and content later
page[1][0](A(href='www.bar.com'))  # calling the tag
page[1][0].append(A(href='www.baz.com'))  # using the API
link = A().append_to(page.body[0]) # access the body as if it's a page attribute
page.body(testDiv=Div()) # WARNING! Correct ordering with named Tag insertion is ensured with Python >= 3.5 (because kwargs are ordered)
link.attr(href='www.python.org')('This is a link to Python.') # Add attributes and content to already placed tags

page.render() # does not return on Python shell

print(page.render())
testfile = open("tempyModTest.html", "w")
print(page.render(), file=testfile)
testfile.close()
