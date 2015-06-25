# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Turn.created'
        db.delete_column('wordgame_turn', 'created')

        # Deleting field 'Turn.gamer2_score'
        db.delete_column('wordgame_turn', 'gamer2_score')

        # Deleting field 'Turn.gamer1_score'
        db.delete_column('wordgame_turn', 'gamer1_score')

        # Adding field 'Turn.board_status'
        db.add_column('wordgame_turn', 'board_status',
                      self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Turn.owner_score'
        db.add_column('wordgame_turn', 'owner_score',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Turn.opponent_score'
        db.add_column('wordgame_turn', 'opponent_score',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Turn.played'
        db.add_column('wordgame_turn', 'played',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True, default=datetime.datetime(2014, 5, 22, 0, 0)),
                      keep_default=False)

        # Deleting field 'Game.gamer2'
        db.delete_column('wordgame_game', 'gamer2_id')

        # Deleting field 'Game.gamer1_score'
        db.delete_column('wordgame_game', 'gamer1_score')

        # Deleting field 'Game.gamer1'
        db.delete_column('wordgame_game', 'gamer1_id')

        # Deleting field 'Game.status'
        db.delete_column('wordgame_game', 'status')

        # Deleting field 'Game.gamer2_score'
        db.delete_column('wordgame_game', 'gamer2_score')

        # Adding field 'Game.owner'
        db.add_column('wordgame_game', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='ownered_games', to=orm['wordgame.Gamer']),
                      keep_default=False)

        # Adding field 'Game.opponent'
        db.add_column('wordgame_game', 'opponent',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, related_name='joined_games', to=orm['wordgame.Gamer']),
                      keep_default=False)

        # Adding field 'Game.owner_score'
        db.add_column('wordgame_game', 'owner_score',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Game.opponent_score'
        db.add_column('wordgame_game', 'opponent_score',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Game.board_status'
        db.add_column('wordgame_game', 'board_status',
                      self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=50, null=True),
                      keep_default=False)


        # Changing field 'Game.started'
        db.alter_column('wordgame_game', 'started', self.gf('django.db.models.fields.DateTimeField')(null=True, auto_now_add=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Turn.created'
        raise RuntimeError("Cannot reverse this migration. 'Turn.created' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Turn.created'
        db.add_column('wordgame_turn', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Turn.gamer2_score'
        db.add_column('wordgame_turn', 'gamer2_score',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Turn.gamer1_score'
        db.add_column('wordgame_turn', 'gamer1_score',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Turn.board_status'
        db.delete_column('wordgame_turn', 'board_status')

        # Deleting field 'Turn.owner_score'
        db.delete_column('wordgame_turn', 'owner_score')

        # Deleting field 'Turn.opponent_score'
        db.delete_column('wordgame_turn', 'opponent_score')

        # Deleting field 'Turn.played'
        db.delete_column('wordgame_turn', 'played')

        # Adding field 'Game.gamer2'
        db.add_column('wordgame_game', 'gamer2',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, related_name='joined_games', to=orm['wordgame.Gamer']),
                      keep_default=False)

        # Adding field 'Game.gamer1_score'
        db.add_column('wordgame_game', 'gamer1_score',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Game.gamer1'
        db.add_column('wordgame_game', 'gamer1',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='ownered_games', to=orm['wordgame.Gamer']),
                      keep_default=False)

        # Adding field 'Game.status'
        db.add_column('wordgame_game', 'status',
                      self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Game.gamer2_score'
        db.add_column('wordgame_game', 'gamer2_score',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Game.owner'
        db.delete_column('wordgame_game', 'owner_id')

        # Deleting field 'Game.opponent'
        db.delete_column('wordgame_game', 'opponent_id')

        # Deleting field 'Game.owner_score'
        db.delete_column('wordgame_game', 'owner_score')

        # Deleting field 'Game.opponent_score'
        db.delete_column('wordgame_game', 'opponent_score')

        # Deleting field 'Game.board_status'
        db.delete_column('wordgame_game', 'board_status')


        # Changing field 'Game.started'
        db.alter_column('wordgame_game', 'started', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 5, 22, 0, 0)))

    models = {
        'wordgame.game': {
            'Meta': {'object_name': 'Game'},
            'board_status': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '50', 'null': 'True'}),
            'finished': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'letters': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'max_length': '32', 'null': 'True', 'unique': 'True'}),
            'opponent': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'related_name': "'joined_games'", 'to': "orm['wordgame.Gamer']"}),
            'opponent_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ownered_games'", 'to': "orm['wordgame.Gamer']"}),
            'owner_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'started': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
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
            'gamers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['wordgame.Gamer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'max_length': '32', 'null': 'True', 'unique': 'True'}),
            'reg_ids': ('django.db.models.fields.TextField', [], {}),
            'sent': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'wordgame.turn': {
            'Meta': {'object_name': 'Turn'},
            'board_status': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '50', 'null': 'True'}),
            'coords': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '50'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'turns'", 'to': "orm['wordgame.Game']"}),
            'gamer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wordgame.Gamer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'max_length': '32', 'null': 'True', 'unique': 'True'}),
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
            'object_id': ('django.db.models.fields.TextField', [], {'max_length': '32', 'null': 'True', 'unique': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'})
        }
    }

    complete_apps = ['wordgame']