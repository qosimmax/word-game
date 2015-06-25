# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PushNotification'
        db.create_table('wordgame_pushnotification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_id', self.gf('django.db.models.fields.TextField')(max_length=32, unique=True, null=True)),
            ('reg_ids', self.gf('django.db.models.fields.TextField')()),
            ('sent', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('wordgame', ['PushNotification'])

        # Adding M2M table for field gamers on 'PushNotification'
        m2m_table_name = db.shorten_name('wordgame_pushnotification_gamers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pushnotification', models.ForeignKey(orm['wordgame.pushnotification'], null=False)),
            ('gamer', models.ForeignKey(orm['wordgame.gamer'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pushnotification_id', 'gamer_id'])

        # Deleting field 'Game.variant'
        db.delete_column('wordgame_game', 'variant')

        # Adding field 'Game.object_id'
        db.add_column('wordgame_game', 'object_id',
                      self.gf('django.db.models.fields.TextField')(max_length=32, unique=True, null=True),
                      keep_default=False)

        # Adding field 'Game.letters'
        db.add_column('wordgame_game', 'letters',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True),
                      keep_default=False)


        # Changing field 'Game.status'
        db.alter_column('wordgame_game', 'status', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))
        # Deleting field 'Gamer.token_id'
        db.delete_column('wordgame_gamer', 'token_id')

        # Adding field 'Gamer.object_id'
        db.add_column('wordgame_gamer', 'object_id',
                      self.gf('django.db.models.fields.TextField')(max_length=32, unique=True, null=True),
                      keep_default=False)

        # Adding field 'Gamer.android_reg_id'
        db.add_column('wordgame_gamer', 'android_reg_id',
                      self.gf('django.db.models.fields.CharField')(max_length=4096, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Gamer.name'
        db.alter_column('wordgame_gamer', 'name', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))
        # Deleting field 'Turn.played'
        db.delete_column('wordgame_turn', 'played')

        # Adding field 'Turn.object_id'
        db.add_column('wordgame_turn', 'object_id',
                      self.gf('django.db.models.fields.TextField')(max_length=32, unique=True, null=True),
                      keep_default=False)

        # Adding field 'Word.object_id'
        db.add_column('wordgame_word', 'object_id',
                      self.gf('django.db.models.fields.TextField')(max_length=32, unique=True, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'PushNotification'
        db.delete_table('wordgame_pushnotification')

        # Removing M2M table for field gamers on 'PushNotification'
        db.delete_table(db.shorten_name('wordgame_pushnotification_gamers'))

        # Adding field 'Game.variant'
        db.add_column('wordgame_game', 'variant',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=80),
                      keep_default=False)

        # Deleting field 'Game.object_id'
        db.delete_column('wordgame_game', 'object_id')

        # Deleting field 'Game.letters'
        db.delete_column('wordgame_game', 'letters')


        # Changing field 'Game.status'
        db.alter_column('wordgame_game', 'status', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=50))
        # Adding field 'Gamer.token_id'
        db.add_column('wordgame_gamer', 'token_id',
                      self.gf('django.db.models.fields.CharField')(null=True, max_length=100, blank=True),
                      keep_default=False)

        # Deleting field 'Gamer.object_id'
        db.delete_column('wordgame_gamer', 'object_id')

        # Deleting field 'Gamer.android_reg_id'
        db.delete_column('wordgame_gamer', 'android_reg_id')


        # Changing field 'Gamer.name'
        db.alter_column('wordgame_gamer', 'name', self.gf('django.db.models.fields.CharField')(null=True, max_length=200))
        # Adding field 'Turn.played'
        db.add_column('wordgame_turn', 'played',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=None, auto_now=True, blank=True),
                      keep_default=False)

        # Deleting field 'Turn.object_id'
        db.delete_column('wordgame_turn', 'object_id')

        # Deleting field 'Word.object_id'
        db.delete_column('wordgame_word', 'object_id')


    models = {
        'wordgame.game': {
            'Meta': {'object_name': 'Game'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'gamer1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ownered_games'", 'to': "orm['wordgame.Gamer']"}),
            'gamer1_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gamer2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'joined_games'", 'null': 'True', 'blank': 'True', 'to': "orm['wordgame.Gamer']"}),
            'gamer2_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'letters': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'max_length': '32', 'unique': 'True', 'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '25', 'default': "'0000000000000000000000000'", 'null': 'True'})
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
            'gamers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['wordgame.Gamer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'max_length': '32', 'unique': 'True', 'null': 'True'}),
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
            'object_id': ('django.db.models.fields.TextField', [], {'max_length': '32', 'unique': 'True', 'null': 'True'}),
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