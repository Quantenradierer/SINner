# SINner backend

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

An simple abstraction layer for the database.

### services

Not every logic belongs into models. For example accessing GPT is a general functionality, which belongs into services.
Services should be standalone, and neither require other code or knowledge about other code in this project to work.

### tools

Some tools which may help at developing.