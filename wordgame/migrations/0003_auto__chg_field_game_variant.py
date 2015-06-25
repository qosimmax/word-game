# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Game.variant'
        db.alter_column('wordgame_game', 'variant', self.gf('django.db.models.fields.CharField')(max_length=80))

    def backwards(self, orm):

        # Changing field 'Game.variant'
        db.alter_column('wordgame_game', 'variant', self.gf('django.db.models.fields.CharField')(max_length=30))

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
            'status': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'default': "'0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'", 'max_length': '50'}),
            'variant': ('django.db.models.fields.CharField', [], {'max_length': '80'})
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
            'game': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'turns'", 'to': "orm['wordgame.Game']"}),
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