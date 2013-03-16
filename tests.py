from notarcpy import FakeModule, FakeField

def test_fields():
    arcpy = FakeModule()
    arcpy.setField('test.shp', FakeField(name='foo', type='String'))
    arcpy.setField('test.shp', FakeField(name='bar', type='Double'))
    assert len(arcpy.ListFields('test.shp')) == 2
    f1, f2 = arcpy.ListFields('test.shp')
    assert f1.name, f1.type == ('bar', 'String')
    assert f2.name, f2.type == ('foo', 'Double')
    
