# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Cave.iiModification'
        db.add_column('cave_cave', 'iiModification',
                      self.gf('django.db.models.fields.DateTimeField')(blank=True, default=datetime.datetime(2013, 11, 28, 0, 0), auto_now=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Cave.iiModification'
        db.delete_column('cave_cave', 'iiModification')


    models = {
        'cave.annee': {
            'Meta': {'object_name': 'Annee'},
            'annee': ('django.db.models.fields.DateField', [], {'default': "'01/01/2009'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'default': "'2009'", 'max_length': '10', 'unique': 'True'})
        },
        'cave.bouteille': {
            'Meta': {'object_name': 'Bouteille'},
            'celluleB': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cave.Cellule']", 'blank': 'True', 'unique': 'True', 'related_name': "'maBouteille'", 'null': 'True'}),
            'gardeMaxB': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'to': "orm['cave.Annee']", 'blank': 'True', 'related_name': "'consoMax'", 'null': 'True'}),
            'gardeMinB': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'to': "orm['cave.Annee']", 'blank': 'True', 'related_name': "'consoMin'", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observation': ('django.db.models.fields.TextField', [], {'default': "'Mon observation'", 'max_length': '750'}),
            'partage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prixB': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'default': "'20'"}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'refB': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'to': "orm['cave.RefBouteille']", 'blank': 'True', 'related_name': "'maReference'", 'null': 'True'})
        },
        'cave.cave': {
            'Meta': {'object_name': 'Cave'},
            'colonnes': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'dateCreation': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'dateModification': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iiModification': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'lieu': ('django.db.models.fields.CharField', [], {'default': "'Ma cave'", 'max_length': '500'}),
            'lignes': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'nom': ('django.db.models.fields.CharField', [], {'default': "'Ma cave'", 'max_length': '500'})
        },
        'cave.cellule': {
            'Meta': {'object_name': 'Cellule'},
            'cave': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cave.Cave']", 'blank': 'True', 'related_name': "'mesCellules'", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'x': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'y': ('django.db.models.fields.IntegerField', [], {'default': '3'})
        },
        'cave.classification': {
            'Meta': {'object_name': 'Classification'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'default': "'Grand cru'", 'max_length': '100', 'unique': 'True'})
        },
        'cave.couleur': {
            'Meta': {'object_name': 'Couleur'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'default': "'Ma couleur'", 'max_length': '50', 'unique': 'True'})
        },
        'cave.pays': {
            'Meta': {'object_name': 'Pays'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'default': "'France'", 'max_length': '100', 'unique': 'True'})
        },
        'cave.refbouteille': {
            'Meta': {'object_name': 'RefBouteille'},
            'anneeB': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'to': "orm['cave.Annee']", 'blank': 'True', 'related_name': "'creation'", 'null': 'True'}),
            'classificationB': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'to': "orm['cave.Classification']", 'blank': 'True', 'null': 'True'}),
            'couleurB': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'to': "orm['cave.Couleur']", 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageB': ('django.db.models.fields.files.FileField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'nomB': ('django.db.models.fields.CharField', [], {'default': "'Ma teille'", 'max_length': '50'}),
            'regionB': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cave.Region']", 'blank': 'True', 'unique': 'True', 'null': 'True'}),
            'typeB': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'to': "orm['cave.TypeBouteille']", 'blank': 'True', 'null': 'True'})
        },
        'cave.region': {
            'Meta': {'object_name': 'Region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'default': "'Bordeaux'", 'max_length': '100', 'unique': 'True'}),
            'paysR': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cave.Pays']"})
        },
        'cave.typebouteille': {
            'Meta': {'object_name': 'TypeBouteille'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ml': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'nom': ('django.db.models.fields.CharField', [], {'default': "'Magnum'", 'max_length': '50', 'unique': 'True'}),
            'volume': ('django.db.models.fields.CharField', [], {'default': "'75cl'", 'max_length': '10'})
        }
    }

    complete_apps = ['cave']