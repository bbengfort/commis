# About Commis

I'm not sure why this doesn't exist yet, but I needed a library for creating command line utilities that wrapped the `argparse` library. Most of the ones I found used a decorator based syntax; but I really do like the Django management commands style of creating applications. Therefore, this library serves to give you the ability to do so!

## Contributing

Commis is open source, and I would be happy to have you contribute! You can contribute in the following ways:

1. Create a pull request in Github: [https://github.com/bbengfort/commis](https://github.com/bbengfort/commis)
2. Add issues or bugs on the bug tracker: [https://github.com/bbengfort/commis/issues](https://github.com/bbengfort/commis/issues)
3. Checkout the current dev board on waffle.io: [https://waffle.io/bbengfort/commis](https://waffle.io/bbengfort/commis)

Note that labels in the Github issues are defined in the blog post: [How we use labels on GitHub Issues at Mediocre Laboratories](https://mediocre.com/forum/topics/how-we-use-labels-on-github-issues-at-mediocre-laboratories).

If you've contributed a fair amount, I'll give you direct access to the repository, which is set up in a typical production/release/development cycle as described in _[A Successful Git Branching Model](http://nvie.com/posts/a-successful-git-branching-model/)_. A typical workflow is as follows:

1. Select a card from the [dev board](https://waffle.io/bbengfort/commis) - preferably one that is "ready" then move it to "in-progress".

2. Create a branch off of develop called "feature-[feature name]", work and commit into that branch.

        ~$ git checkout -b feature-myfeature develop

3. Once you are done working (and everything is tested) merge your feature into develop.

        ~$ git checkout develop
        ~$ git merge --no-ff feature-myfeature
        ~$ git branch -d feature-myfeature
        ~$ git push origin develop

4. Repeat. Releases will be routinely pushed into master via release branches, then deployed to the server.

Note that pull requests will be reviewed when the Travis-CI tests pass, so including tests with your pull request is ideal!

You can contact me on Twitter if needed: [@bbengfort](https://twitter.com/bbengfort)

## Name Origin
<big>com &middot; mis</big><br />
/ˈkämē,kô-/<br/>
*noun* a junior chef.

Origin<br />
[Latin] *committere*: 1930s: from French, 'deputy, clerk', past participle of commettre 'entrust', from Latin.<br \>

A commis is a basic chef in larger kitchens who works under a chef de partie to learn the station's or range's responsibilities and operation.[3] This may be a chef who has recently completed formal culinary training or is still undergoing training. &mdash; [Wikipedia](https://en.wikipedia.org/wiki/Chef#Commis_.28Chef.29_.2F_Range_chef)

This package is closely related to the [Confire](https://github.com/bbengfort/confire) configuration tool, hence the name in the same vein &mdash; French cooking words. In this case, a commis is someone to whom orders are given (commands) and seemed an appropriate term for a package whose function is accept and execute commands.

## Releases

The release versions that are sent to the Python package index are also tagged in Github. You can see the tags through the Github web application and download the tarball of the version you'd like. Additionally PyPI will host the various releases of Commis.

The versioning uses a three part version system, "a.b.c" - "a" represents a major release that may not be backwards compatible. "b" is incremented on minor releases that may contain extra features, but are backwards compatible. "c" releases are bug fixes or other micro changes that developers should feel free to immediately update to.

### Version 0.5

* **tag**: [v0.5](https://github.com/bbengfort/commis/releases/tag/v0.5)
* **deployment**: July 11, 2019

Updated the colorama requirements to `colorma>=0.3.6` in order to better support other console utilities that utilize newer version of colorama. Updates to documentation and examples.

### Version 0.4

* **tag**: [v0.4](https://github.com/bbengfort/commis/releases/tag/v0.4)
* **deployment**: October 11, 2017

Implemented some better handling for Python 3 argparse, continuing migration from Python 2.

### Version 0.3

* **tag**: [v0.3](https://github.com/bbengfort/commis/releases/tag/v0.3)
* **deployment**: June 2, 2016

Added Python 3.5 compatibility primarily by fixing the `--version` argument in  the `argparse` library (apparently a weirdly supported feature from old  versions of Python 2. Also updated tests with some capture for different import paths as well as adding six for testing 2to3 compatibility.

### Version 0.2

* **tag**: [v0.2](https://github.com/bbengfort/commis/releases/tag/v0.2)
* **deployment**: January 25, 2016

Solidified the Commis library by improving the test suite and the documentation. I've also included a couple of modules that were big helps in the past: a color library that wraps colorama, and a LabelCommand. This is really the official "first" version that I feel is production ready.

### Version 0.1

* **tag**: [v0.1](https://github.com/bbengfort/commis/releases/tag/v0.4)
* **deployment**: January 20, 2016

This is the initial release, which will simply bring over all the code and features that have previously been implemented in other locations. This release has also been published to PyPI and has some initial documentation.
