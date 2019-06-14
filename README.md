# slashboard

Serverless Dashboarding, a simple prototype.

## Goal

Data is provided in a simple data base, e.g. SQLite. The data is comprised of

* several tables with data (let's call them *facts*)
* and one table resolving facts and users (*users* table).

So basically every fact has a key which can be used to join *facts* and *users*.

The goal is now to let the user

* formulate a (complex) calculation on the tables
* but transparently for him reduce the facts by the ones he does not have access to.

Therefore, a token, sent by the browser (here: simple header `X-Username`), has to be passed beyond the source for the (filtered) user data and the user already receives filtered input.
