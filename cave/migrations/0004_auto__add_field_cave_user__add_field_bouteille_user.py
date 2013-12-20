# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Cave.user'
        db.add_column('cave_cave', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Bouteille.user'
        db.add_column('cave_bouteille', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Cave.user'
        db.delete_column('cave_cave', 'user_id')

        # Deleting field 'Bouteille.user'
        db.delete_column('cave_bouteille', 'user_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cave.annee': {
            'Meta': {'object_name': 'Annee'},
            'annee': ('django.db.models.fields.DateField', [], {'default': "'01/01/2009'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'default': "'2009'", 'max_length': '10'})
        },
        'cave.bouteille': {
            'Meta': {'object_name': 'Bouteille'},
            'celluleB': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cave.Cellule']", 'null': 'True', 'related_name': "'maBouteille'", 'blank': 'True', 'unique': 'True'}),
            'gardeMaxB': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cave.Annee']", 'null': 'True', 'related_name': "'consoMax'", 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'gardeMinB': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cave.Annee']", 'null': 'True', 'related_name': "'consoMin'", 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observation': ('django.db.models.fields.TextField', [], {'max_length': '750', 'default': "'Mon observation'"}),
            'partage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prixB': ('django.db.models.fields.DecimalField', [], {'default': "'20'", 'decimal_places': '2', 'max_digits': '8'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'refB': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cave.RefBouteille']", 'null': 'True', 'related_name': "'maReference'", 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'cave.cave': {
            'Meta': {'object_name': 'Cave'},
            'colonnes': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'dateCreation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dateModification': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lieu': ('django.db.models.fields.CharField', [], {'max_length': '500', 'default': "'Ma cave'"}),
            'lignes': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '500', 'default': "'Ma cave'"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'cave.cellule': {
            'Meta': {'object_name': 'Cellule'},
            'cave': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cave.Cave']", 'null': 'True', 'related_name': "'mesCellules'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'x': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'y': ('django.db.models.fields.IntegerField', [], {'default': '3'})
        },
        'cave.classification': {
            'Meta': {'object_name': 'Classification'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'default': "'Grand cru'", 'max_length': '100'})
        },
        'cave.couleur': {
            'Meta': {'object_name': 'Couleur'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'default': "'Ma couleur'", 'max_length': '50'})
        },
        'cave.pays': {
            'Meta': {'object_name': 'Pays'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'default': "'France'", 'max_length': '100'})
        },
        'cave.refbouteille': {
            'Meta': {'object_name': 'RefBouteille'},
            'anneeB': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cave.Annee']", 'null': 'True', 'related_name': "'creation'", 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'classificationB': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['cave.Classification']", 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'couleurB': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['cave.Couleur']", 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageB': ('django.db.models.fields.files.FileField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'nomB': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'Ma teille'"}),
            'regionB': ('django.db.models.fields.related.OneToOneField', [], {'null': 'True', 'to': "orm['cave.Region']", 'blank': 'True', 'unique': 'True'}),
            'typeB': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['cave.TypeBouteille']", 'on_delete': 'models.SET_NULL', 'blank': 'True'})
        },
        'cave.region': {
            'Meta': {'object_name': 'Region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'default': "'Bordeaux'", 'max_length': '100'}),
            'paysR': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cave.Pays']"})
        },
        'cave.typebouteille': {
            'Meta': {'object_name': 'TypeBouteille'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ml': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '6'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'default': "'Magnum'", 'max_length': '50'}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '10', 'default': "'75cl'"})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cave']