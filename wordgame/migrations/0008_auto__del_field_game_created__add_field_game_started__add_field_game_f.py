# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Game.created'
        db.delete_column('wordgame_game', 'created')

        # Adding field 'Game.started'
        db.add_column('wordgame_game', 'started',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=None, blank=True),
                      keep_default=False)

        # Adding field 'Game.finished'
        db.add_column('wordgame_game', 'finished',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Game.created'
        db.add_column('wordgame_game', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=None, blank=True),
                      keep_default=False)

        # Deleting field 'Game.started'
        db.delete_column('wordgame_game', 'started')

        # Deleting field 'Game.finished'
        db.delete_column('wordgame_game', 'finished')


    models = {
        'wordgame.game': {
            'Meta': {'object_name': 'Game'},
            'finished': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'gamer1': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wordgame.Gamer']", 'related_name': "'ownered_games'"}),
            'gamer1_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gamer2': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wordgame.Gamer']", 'related_name': "'joined_games'", 'null': 'True', 'blank': 'True'}),
            'gamer2_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'letters': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100'}),
            'object_id': ('django.db.models.fields.TextField', [], {'unique': 'True', 'null': 'True', 'max_length': '32'}),
            'started': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'null': 'True', 'max_length': '50'}),
            'vocabulary': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        'wordgame.gamer': {
            'Meta': {'object_name': 'Gamer'},
            'android_reg_id': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '4096', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '40'}),
            'object_id': ('django.db.models.fields.TextField', [], {'unique': 'True', 'null': 'True', 'max_length': '32'}),
            'serial': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'})
        },
        'wordgame.pushnotification': {
            'Meta': {'object_name': 'PushNotification'},
            'gamers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['wordgame.Gamer']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'unique': 'True', 'null': 'True', 'max_length': '32'}),
            'reg_ids': ('django.db.models.fields.TextField', [], {}),
            'sent': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'wordgame.turn': {
            'Meta': {'object_name': 'Turn'},
            'coords': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wordgame.Game']", 'related_name': "'turns'"}),
            'gamer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wordgame.Gamer']"}),
            'gamer1_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gamer2_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'unique': 'True', 'null': 'True', 'max_length': '32'}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'wordgame.word': {
            'Meta': {'object_name': 'Word'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'unique': 'True', 'null': 'True', 'max_length': '32'}),
            'word': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['wordgame']