Fetch
=====

What Problem Does Fetch Solve?
------------------------------

When an IPython notebook is shared between multiple users on multiple computers,
users must edit the notebook each time it is transferred to update the
file paths to any resources (movies, large analysis results, etc.). Usually,
their locations differ between individual computers. This is a drag.

Fetch directs the notebook to check a local stash, specified individually
on each computer by an environmental variable. For example, the stash might be
`/Users/dallan/Data` on my computer and `C:\Users\Someone\Experiments` on
yours. Fetch handles this implicitly.

If a stash is missing a given file, that file is automatically downloaded from
[Amazon S3](http://aws.amazon.com/s3/) and retained locally for future use. If the files are later deleted
to reclaim disk space, they are downloaded again as needed.

Installation & Setup
--------------------

Install fetch using pip:

    pip install http://github.com/danielballan/fetch/zipball/master

or, alternatively, using git:

    git clone http://github.com/danielballan/fetch
    cd fetch
    python setup.py install

If you have not already done so, you must set up Amazon AWS authentication
by defining environmental variables.

    export AWS_ACCESS_KEY_ID=...
    export AWS_SECRET_ACCESS_KEY=...

You can also specify the directory where fetch will stash local copy of the
files it downloads.

    export FETCH_STASH=/path/to/data-files

Otherwise, fetch will put the files in the current working directory.

Usage
-----

    >>> from fetch import fetch

    >>> fetch('my-bucket-name', 'my-file')
    Fetching data from S3...
    '/path/to/fetch-stash/my-file'

    >>> fetch('my-bucket-name', 'my-file')
    '/path/to/fetch-stash/my-file'

As illustrated above, the function `fetch` downloads the file if necessary
and returns the local filepath.
