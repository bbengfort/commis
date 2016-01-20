# Commis

**Create command line applications like Django management commands.**

[![Build Status](https://travis-ci.org/bbengfort/commis.svg?branch=master)](https://travis-ci.org/bbengfort/commis)
[![Coverage Status](https://coveralls.io/repos/github/bbengfort/commis/badge.svg?branch=master)](https://coveralls.io/github/bbengfort/commis?branch=master)

[![Pâte de fruit (gominolas) de laranxa sanguina][gominolas.jpg]][gominolas_flickr]

## About ##

I'm not sure why this doesn't exist yet, but I needed a library for creating command line utilities that wrapped the `argparse` library. Most of the ones I found used a decorator based syntax; but I really do like the Django management commands style of creating applications. Therefore, this library serves to give you the ability to do so!

### Contributing ###

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

### Name Origin ###
<big>com &middot; mis</big><br />
/ˈkämē,kô-/<br/>
*noun* a junior chef.

Origin<br />
[Latin] *committere*: 1930s: from French, 'deputy, clerk', past participle of commettre 'entrust', from Latin.<br \>

A commis is a basic chef in larger kitchens who works under a chef de partie to learn the station's or range's responsibilities and operation.[3] This may be a chef who has recently completed formal culinary training or is still undergoing training. &mdash; [Wikipedia](https://en.wikipedia.org/wiki/Chef#Commis_.28Chef.29_.2F_Range_chef)

This package is closely related to the [Confire](https://github.com/bbengfort/confire) configuration tool, hence the name in the same vein &mdash; French cooking words. In this case, a commis is someone to whom orders are given (commands) and seemed an appropriate term for a package whose function is accept and execute commands.

### Attribution

The photo used in this README, &ldquo;[Pâte de fruit (gominolas) de laranxa sanguina][gominolas_flickr]&rdquo; by [Receitasparatodososdias](https://www.flickr.com/photos/100127130@N05/) is used under a [CC BY-NC-ND 2.0](https://creativecommons.org/licenses/by-nc-nd/2.0/) creative commons license.

## Changelog ##

The release versions that are sent to the Python package index are also tagged in Github. You can see the tags through the Github web application and download the tarball of the version you'd like. Additionally PyPI will host the various releases of commis.

The versioning uses a three part version system, "a.b.c" - "a" represents a major release that may not be backwards compatible. "b" is incremented on minor releases that may contain extra features, but are backwards compatible. "c" releases are bug fixes or other micro changes that developers should feel free to immediately update to.

### v0.1.0 pending release ###

* **tag**: v0.1.0
* **deployment**: pending
* **commit**: (latest)

This is the initial release, which will simply bring over all the code and features that have previously been implemented in other locations.

<!-- References -->
[gominolas.jpg]: docs/img/gominolas.jpg
[gominolas_flickr]: https://flic.kr/p/mcSxAK
