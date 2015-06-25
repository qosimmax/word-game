# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Turn.coords'
        db.alter_column('wordgame_turn', 'coords', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'Turn.coords'
        db.alter_column('wordgame_turn', 'coords', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=50))

    models = {
        'wordgame.game': {
            'Meta': {'object_name': 'Game'},
            'board_status': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'null': 'True', 'max_length': '50'}),
            'finished': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'letters': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100'}),
            'object_id': ('django.db.models.fields.TextField', [], {'null': 'True', 'unique': 'True', 'max_length': '32'}),
            'opponent': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['wordgame.Gamer']", 'blank': 'True', 'related_name': "'joined_games'"}),
            'opponent_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wordgame.Gamer']", 'related_name': "'ownered_games'"}),
            'owner_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'started': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'vocabulary': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        'wordgame.gamer': {
            'Meta': {'object_name': 'Gamer'},
            'android_reg_id': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '4096', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '40'}),
            'object_id': ('django.db.models.fields.TextField', [], {'null': 'True', 'unique': 'True', 'max_length': '32'}),
            'serial': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'})
        },
        'wordgame.pushnotification': {
            'Meta': {'object_name': 'PushNotification'},
            'gamers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['wordgame.Gamer']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'null': 'True', 'unique': 'True', 'max_length': '32'}),
            'reg_ids': ('django.db.models.fields.TextField', [], {}),
            'sent': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'wordgame.turn': {
            'Meta': {'object_name': 'Turn'},
            'board_status': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'null': 'True', 'max_length': '50'}),
            'coords': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '100'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wordgame.Game']", 'related_name': "'turns'"}),
            'gamer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wordgame.Gamer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'null': 'True', 'unique': 'True', 'max_length': '32'}),
            'opponent_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'owner_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'played': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'wordgame.word': {
            'Meta': {'object_name': 'Word'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'null': 'True', 'unique': 'True', 'max_length': '32'}),
            'word': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['wordgame']