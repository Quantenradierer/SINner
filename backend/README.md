# Schattenakte backend

## Architecture

The architecture is mostly based off domain-driven-design by Eric Evans.

### models

Models which contain data and business functionality.
Models should not actively use the repository or the database. The operation, not the model itself, decides when those
instances of models are being saved.
They may use and change other models, when they are the only one which manages it (see aggregates at domain driven
design).

### operations

Since most of the other patterns shall not interact with each other, operations tie everything together. They implement
the concrete business process.

### repositories

A simple abstraction layer for the database.
Yes, the model itself has all those wonderful methods to save, but this often leads to the model saving itself. 
But then, the model will be saved in every unittest, which then is no unittest and also results in higher test times. 

And even adding filters in the model mixes regular business objects with database access. 

It may even save the data when the business does not intend it. 

The access to databases should therefore mainly be used by the business process (operations). 
So that's what the repository is for: for the operations, to manage database access and transactions. 

### services

Not every logic belongs into models. For example accessing GPT is a general functionality, which belongs into services.
Services should be standalone, and neither require other code or knowledge about other code in this project to work.
