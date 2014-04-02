Development Doc
===

Glossary
---

**Entry Item**: a data item for an entry, such as a text box.  This
  will have additioanl information such as a default value, input
  type, and other guesses.

**Item**: a single data item for the display.  It might be an
  entry field, a text field, or it might be a collection of additional
  data items, i.e., a grid, an array, or a dictionary.

**Spec**:   a specification for data item.  If the data item is a collection,
then the spe will have an iterator for items in the spec.


Orientation
---

./cruft:  where I put old junk; the graveyard of code.

./doc:  documentation, both for users and developers

./lib:  libraries or blocks of code that are pulled from other sources

./src:  the main source code directory, holds the *makefile* and some
   random tests or experiments.

./src/pyui:  the actual pyui package.

Key Classes
---

Base:   PyUI abstract base class for UIs.  It has subclasses for each specific UI system, e.g., Echo, Tk, Text, etc.
