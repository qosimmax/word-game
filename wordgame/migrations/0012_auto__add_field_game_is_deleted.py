# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Game.is_deleted'
        db.add_column('wordgame_game', 'is_deleted',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Game.is_deleted'
        db.delete_column('wordgame_game', 'is_deleted')


    models = {
        'wordgame.game': {
            'Meta': {'object_name': 'Game'},
            'board_status': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '100', 'null': 'True'}),
            'finished': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'letters': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'max_length': '32', 'unique': 'True', 'null': 'True'}),
            'opponent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'joined_games'", 'null': 'True', 'to': "orm['wordgame.Gamer']"}),
            'opponent_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ownered_games'", 'to': "orm['wordgame.Gamer']"}),
            'owner_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'started': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'vocabulary': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        'wordgame.gamer': {
            'Meta': {'object_name': 'Gamer'},
            'android_reg_id': ('django.db.models.fields.CharField', [], {'max_length': '4096', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'max_length': '32', 'unique': 'True', 'null': 'True'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'wordgame.pushnotification': {
            'Meta': {'object_name': 'PushNotification'},
            'gamers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['wordgame.Gamer']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'max_length': '32', 'unique': 'True', 'null': 'True'}),
            'reg_ids': ('django.db.models.fields.TextField', [], {}),
            'sent': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'wordgame.turn': {
            'Meta': {'object_name': 'Turn'},
            'board_status': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '100', 'null': 'True'}),
            'coords': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '100'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'turns'", 'to': "orm['wordgame.Game']"}),
            'gamer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wordgame.Gamer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'max_length': '32', 'unique': 'True', 'null': 'True'}),
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
            'object_id': ('django.db.models.fields.TextField', [], {'max_length': '32', 'unique': 'True', 'null': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['wordgame']