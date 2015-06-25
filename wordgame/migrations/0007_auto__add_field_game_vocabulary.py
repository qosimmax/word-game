# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Game.vocabulary'
        db.add_column('wordgame_game', 'vocabulary',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Game.vocabulary'
        db.delete_column('wordgame_game', 'vocabulary')


    models = {
        'wordgame.game': {
            'Meta': {'object_name': 'Game'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'gamer1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ownered_games'", 'to': "orm['wordgame.Gamer']"}),
            'gamer1_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gamer2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'joined_games'", 'to': "orm['wordgame.Gamer']", 'null': 'True', 'blank': 'True'}),
            'gamer2_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'letters': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'max_length': '32', 'null': 'True', 'unique': 'True'}),
            'status': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '50', 'null': 'True'}),
            'vocabulary': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        'wordgame.gamer': {
            'Meta': {'object_name': 'Gamer'},
            'android_reg_id': ('django.db.models.fields.CharField', [], {'max_length': '4096', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'max_length': '32', 'null': 'True', 'unique': 'True'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'wordgame.pushnotification': {
            'Meta': {'object_name': 'PushNotification'},
            'gamers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['wordgame.Gamer']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'max_length': '32', 'null': 'True', 'unique': 'True'}),
            'reg_ids': ('django.db.models.fields.TextField', [], {}),
            'sent': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
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
            'object_id': ('django.db.models.fields.TextField', [], {'max_length': '32', 'null': 'True', 'unique': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'wordgame.word': {
            'Meta': {'object_name': 'Word'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'max_length': '32', 'null': 'True', 'unique': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'})
        }
    }

    complete_apps = ['wordgame']