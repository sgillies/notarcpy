================================
(I Can't Believe It's) Not ArcPy
================================

Because of ArcPy, lots of people are writing and sharing Python code. And a lot
of this code needs help. I'd like to turn this into a teachable moment, but
I don't use or have ArcPy. I can't `import arcpy.` If I had a module that could
fake it, I could send new Python programmers tested pull requests. This is an
attempt at making such a fake module.

Example
=======

Say I want to group the names of a featureclass's fields by their types.
I write a function like:

.. sourcecode:: python

  def group_fields_by_type(fields):
      groups = {}
      for field in fields:
          if field.type not in groups:
              groups[field.type] = []
          groups[field.type].append(field.name)
      return groups

I need something to stand in for ArcPy's fields to test this. That thing is
`notarcpy.FakeField`. My test:

.. sourcecode:: python

  def test_field_grouping():
      fields = [
          FakeField(name='foo', type='String'), 
          FakeField(name='bar', type='Double')]
      groups = group_fields_by_type(fields)
      assert groups['String'] == ['foo']
      assert groups['Double'] == ['bar']

Fake cursors and fake rows (TODO) would make a lot of ArcPy scripts much more
testable.

