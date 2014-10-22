# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'RefBouteille', fields ['regionB']
        db.delete_unique('cave_refbouteille', ['regionB_id'])


        # Changing field 'RefBouteille.regionB'
        db.alter_column('cave_refbouteille', 'regionB_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, null=True, to=orm['cave.Region']))

    def backwards(self, orm):

        # Changing field 'RefBouteille.regionB'
        db.alter_column('cave_refbouteille', 'regionB_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, null=True, to=orm['cave.Region']))
        # Adding unique constraint on 'RefBouteille', fields ['regionB']
        db.create_unique('cave_refbouteille', ['regionB_id'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
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
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Group']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'cave.annee': {
            'Meta': {'object_name': 'Annee'},
            'annee': ('django.db.models.fields.DateField', [], {'default': "'01/01/2009'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '10', 'default': "'2009'", 'unique': 'True'})
        },
        'cave.bouteille': {
            'Meta': {'object_name': 'Bouteille'},
            'celluleB': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'blank': 'True', 'to': "orm['cave.Cellule']", 'null': 'True', 'related_name': "'maBouteille'"}),
            'gardeMaxB': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'blank': 'True', 'to': "orm['cave.Annee']", 'null': 'True', 'related_name': "'consoMax'"}),
            'gardeMinB': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'blank': 'True', 'to': "orm['cave.Annee']", 'null': 'True', 'related_name': "'consoMin'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observation': ('django.db.models.fields.TextField', [], {'max_length': '750', 'default': "'Mon observation'"}),
            'partage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prixB': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '8', 'default': "'20'"}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'refB': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'blank': 'True', 'to': "orm['cave.RefBouteille']", 'null': 'True', 'related_name': "'maReference'"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'monProprioBouteille'"})
        },
        'cave.cave': {
            'Meta': {'object_name': 'Cave'},
            'colonnes': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'dateCreation': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'dateModification': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lieu': ('django.db.models.fields.CharField', [], {'max_length': '500', 'default': "'Ma cave'"}),
            'lignes': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '500', 'default': "'Ma cave'"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'monProprio'"})
        },
        'cave.cellule': {
            'Meta': {'object_name': 'Cellule'},
            'cave': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['cave.Cave']", 'null': 'True', 'related_name': "'mesCellules'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'x': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'y': ('django.db.models.fields.IntegerField', [], {'default': '3'})
        },
        'cave.classification': {
            'Meta': {'object_name': 'Classification'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "'Grand cru'", 'unique': 'True'})
        },
        'cave.couleur': {
            'Meta': {'object_name': 'Couleur'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'Ma couleur'", 'unique': 'True'})
        },
        'cave.pays': {
            'Meta': {'object_name': 'Pays'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "'France'", 'unique': 'True'})
        },
        'cave.refbouteille': {
            'Meta': {'object_name': 'RefBouteille'},
            'anneeB': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'blank': 'True', 'to': "orm['cave.Annee']", 'null': 'True', 'related_name': "'creation'"}),
            'classificationB': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'blank': 'True', 'null': 'True', 'to': "orm['cave.Classification']"}),
            'couleurB': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'blank': 'True', 'null': 'True', 'to': "orm['cave.Couleur']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageB': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'default': "'void.jpeg'"}),
            'nomB': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'Ma teille'"}),
            'regionB': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'blank': 'True', 'null': 'True', 'to': "orm['cave.Region']"}),
            'typeB': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'blank': 'True', 'null': 'True', 'to': "orm['cave.TypeBouteille']"})
        },
        'cave.region': {
            'Meta': {'object_name': 'Region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "'Bordeaux'", 'unique': 'True'}),
            'paysR': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cave.Pays']"})
        },
        'cave.typebouteille': {
            'Meta': {'object_name': 'TypeBouteille'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ml': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '6'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'Magnum'", 'unique': 'True'}),
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