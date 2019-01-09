How to contribute
=================

Welcome
-------

Thank you for your interest to contribute to this project!
We appretiate everyone who wants to help!

In this document we collected some information we think you will find useful to get started.

If you have any questions, please feel free to [ask your question](question)!


Be a nice person
----------------

We want everyone to feel welcome and be happy at our project. 
That's why we follow the **[Code of Conduct][code_of_conduct]**. 
Please follow it in all your interactions with the project, 
including comments, questions, issues, requests and so on.

How to contribute
-----------------

> No Programmer? No Problem! Find out how you can 
> [contribute without writing code][contribute-nocoder]!

To keep the code organized, we uses the **[Git Flow branching model][gitflow-model]**. 
If you never heard Git Flow before, please get familiar with the 
[concept of git flow][gitflow-model] and use the [Gitflow Cheatsheet][gitflow-cheatsheet].

Where it makes sense is done using [Behaviour-Driven Development][bdd] and Test-Driven Development[tdd].
We use python's unittest-module to write Unit tests and the behave-module to develop
behaviour tests.

Before you contribute, please contact us and tell us what you want to change!

How to do a pull request
------------------------

1. Open an issue and let us know what you want to change or improve.
   We are excited to discuss your idea with you!
2. [Fork the code][fork] and clone it, then checkout the development branch.
   
   ```
   git clone https://github.com/michagrandel/servertools.git
   git checkout develop
   ```
   
3. Make sure, any existings tests in the test directory are working!
4. Add a new feature branch

   ```
   git flow feature start MYFEATURE
   ```
   
   or 
   
   ```
   git checkout -b feature/MYFEATURE develop
   ```
  
5. Write a **.feature-file** for [behave](behave) to describe, what you want to change.\
   If you are new to the behave-module, you may find [this tutorial](behave-tutorial) helpful
6. Implement a Behaviour Tests using behave and Unit tests if needed
7. Develop your feature and implement everything you need
8. If you are finish, run your tests you wrote in the previous steps to 
   ensure everything runs as expected
9. Finally, make a pull request

I am no programmer. What can I do
---------------------------------

You don't *have* to be an programmer to contribute. There are many ways to help:

**Help us to optimize future development**

This is very simple! Just download our [tool to provide hardware- and software information][tool]
about your computer. Run the tool and you are done! This will help us focus on hard- and software
which is actual in use instead of get lost in improvments for platforms that do not
exist (any more).

**Help us write or improve documentation for users, so they can learn how to use the software**

Bad documentation frightens users! But it is hard to write good documentation.
We all make mistakes: Typos, explanations that are hard to understand, Formatting errors, 
missing documents or broken links...

You can help us improving our documentation or writing new documentation by joining our
[documentation wiki][documentation].

**Find and report bugs and test software**

If you find a bug, [please let us know][report-bug]!

If you didn't find a bug yet, download a [pre-release][pre-release] to test our new 
features and code. You probably will find something soon. 

**Help to improve the user interface**

Please provide screenshots of our software! This is very helpful for user interface enhancments!
If you are familiar with graphics software or UI Designers, you may want to suggest new
or enhanced user interface concepts!

**Translate the software in your mother tongue**

The more languages, the better! Please [contact us][translate] if you are interested!

Have a question?
----------------

Don't hesitate to [ask your questions][question] if you have something in mind!

<!-- project links -->
[question]: https://github.com/michagrandel/servertools/issues/new?labels=question&body=
[documentation]: https://github.com/michagrandel/servertools/wiki
[fork]: https://github.com/michagrandel/servertools/fork
[pre-release]: https://github.com/michagrandel/servertools/releases
[report-bug]: https://github.com/michagrandel/servertools/issues/new

<!-- File links -->
<!-- @todo: keep links up to date when changing a linked file! -->
[code_of_conduct]: https://github.com/michagrandel/servertools/blob/master/CODE_OF_CONDUCT.md

<!-- wiki links -->
<!-- @docs: The DOCUMENTATION TEAM will update these links if necessary -->
[contribute-nocoder]: I-am-no-programmer.-What-can-I-do
[maintainer]: https://github.com/michagrandel/servertools/wiki/Project-Maintainers
[tool]: https://github.com/michagrandel/servertools/wiki/Tools
[translate]: https://github.com/michagrandel/servertools/wiki/Internationalisation

<!-- external links -->
<!-- @release: check if these links work and update them if necessary -->
[gitflow-model]: http://nvie.com/posts/a-successful-git-branching-model/
[gitflow-cheatsheet]: elhttps://danielkummer.github.io/git-flow-cheatsheet/
[bdd]: https://dannorth.net/introducing-bdd/
[tdd]: https://en.wikipedia.org/wiki/Test-driven_development
[behave]: https://pypi.python.org/pypi/behave/1.2.5
[behave-tutorial]: https://pythonhosted.org/behave/tutorial.html 
