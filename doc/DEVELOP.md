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

**Prespec**: a shorthand name for a string that is an unparsed spec.
  A prespec might be ":number is integer" which can be turned into a
  spec, or instance of the Spec class.  The language of the prespec is
  likely to be ambiguous.

**Spec**: a specification for data item, of the class Spec.  This may
  be a terminal item, such as a label or entry item.  Alternately, it
  may be a collection.  It allowable for a collection Spec to have a
  value that is a prespec.  For example, a dictionary's spec might have
  values that will be parsed just before adding them to the gui.

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

Spec:  The compiled spec.
