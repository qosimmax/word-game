# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Word'
        db.create_table('wordgame_word', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('wordgame', ['Word'])

        # Adding model 'Gamer'
        db.create_table('wordgame_gamer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('serial', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('token_id', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('wordgame', ['Gamer'])

        # Adding model 'Turn'
        db.create_table('wordgame_turn', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wordgame.Game'])),
            ('gamer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wordgame.Gamer'])),
            ('coords', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=50)),
            ('word', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gamer1_score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('gamer2_score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('played', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('wordgame', ['Turn'])

        # Adding model 'Game'
        db.create_table('wordgame_game', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gamer1', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wordgame.Gamer'])),
            ('gamer2', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='gamer2', null=True, to=orm['wordgame.Gamer'])),
            ('variant', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gamer1_score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('gamer2_score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('status', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=50)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('wordgame', ['Game'])


    def backwards(self, orm):
        # Deleting model 'Word'
        db.delete_table('wordgame_word')

        # Deleting model 'Gamer'
        db.delete_table('wordgame_gamer')

        # Deleting model 'Turn'
        db.delete_table('wordgame_turn')

        # Deleting model 'Game'
        db.delete_table('wordgame_game')


    models = {
        'wordgame.game': {
            'Meta': {'object_name': 'Game'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'gamer1': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wordgame.Gamer']"}),
            'gamer1_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gamer2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'gamer2'", 'null': 'True', 'to': "orm['wordgame.Gamer']"}),
            'gamer2_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '50'}),
            'variant': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'wordgame.gamer': {
            'Meta': {'object_name': 'Gamer'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'token_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'wordgame.turn': {
            'Meta': {'object_name': 'Turn'},
            'coords': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wordgame.Game']"}),
            'gamer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wordgame.Gamer']"}),
            'gamer1_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gamer2_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'played': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'wordgame.word': {
            'Meta': {'object_name': 'Word'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['wordgame']