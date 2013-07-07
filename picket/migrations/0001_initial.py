# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Organizer'
        db.create_table(u'picket_organizer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'picket', ['Organizer'])

        # Adding model 'Picket'
        db.create_table(u'picket_picket', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('begin_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('place_readable', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('place_latlong', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('organizer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picket.Organizer'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'picket', ['Picket'])


    def backwards(self, orm):
        # Deleting model 'Organizer'
        db.delete_table(u'picket_organizer')

        # Deleting model 'Picket'
        db.delete_table(u'picket_picket')


    models = {
        u'picket.organizer': {
            'Meta': {'object_name': 'Organizer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'picket.picket': {
            'Meta': {'object_name': 'Picket'},
            'begin_at': ('django.db.models.fields.DateTimeField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'end_at': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organizer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['picket.Organizer']"}),
            'place_latlong': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'place_readable': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['picket']