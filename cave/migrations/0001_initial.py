# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cave'
        db.create_table('cave_cave', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=500, default='Ma cave')),
            ('lieu', self.gf('django.db.models.fields.CharField')(max_length=500, default='Ma cave')),
            ('lignes', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('colonnes', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('dateCreation', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('dateModification', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
        ))
        db.send_create_signal('cave', ['Cave'])

        # Adding model 'Cellule'
        db.create_table('cave_cellule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cave', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='mesCellules', to=orm['cave.Cave'], blank=True)),
            ('x', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('y', self.gf('django.db.models.fields.IntegerField')(default=3)),
        ))
        db.send_create_signal('cave', ['Cellule'])

        # Adding model 'RefBouteille'
        db.create_table('cave_refbouteille', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nomB', self.gf('django.db.models.fields.CharField')(max_length=50, default='Ma teille')),
            ('typeB', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['cave.TypeBouteille'], blank=True, on_delete=models.SET_NULL)),
            ('couleurB', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['cave.Couleur'], blank=True, on_delete=models.SET_NULL)),
            ('classificationB', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['cave.Classification'], blank=True, on_delete=models.SET_NULL)),
            ('anneeB', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='creation', to=orm['cave.Annee'], blank=True, on_delete=models.SET_NULL)),
            ('regionB', self.gf('django.db.models.fields.related.OneToOneField')(null=True, unique=True, to=orm['cave.Region'], blank=True)),
            ('imageB', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('cave', ['RefBouteille'])

        # Adding model 'Bouteille'
        db.create_table('cave_bouteille', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('refB', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='maReference', to=orm['cave.RefBouteille'], blank=True, on_delete=models.SET_NULL)),
            ('gardeMinB', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='consoMin', to=orm['cave.Annee'], blank=True, on_delete=models.SET_NULL)),
            ('gardeMaxB', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='consoMax', to=orm['cave.Annee'], blank=True, on_delete=models.SET_NULL)),
            ('prixB', self.gf('django.db.models.fields.DecimalField')(default='20', max_digits=8, decimal_places=2)),
            ('celluleB', self.gf('django.db.models.fields.related.OneToOneField')(null=True, related_name='maBouteille', unique=True, to=orm['cave.Cellule'], blank=True)),
            ('rating', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('partage', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('observation', self.gf('django.db.models.fields.TextField')(max_length=750, default='Mon observation')),
        ))
        db.send_create_signal('cave', ['Bouteille'])

        # Adding model 'Annee'
        db.create_table('cave_annee', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=10, unique=True, default='2009')),
            ('annee', self.gf('django.db.models.fields.DateField')(default='01/01/2009')),
        ))
        db.send_create_signal('cave', ['Annee'])

        # Adding model 'Couleur'
        db.create_table('cave_couleur', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True, default='Ma couleur')),
        ))
        db.send_create_signal('cave', ['Couleur'])

        # Adding model 'TypeBouteille'
        db.create_table('cave_typebouteille', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True, default='Magnum')),
            ('volume', self.gf('django.db.models.fields.CharField')(max_length=10, default='75cl')),
            ('ml', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=6)),
        ))
        db.send_create_signal('cave', ['TypeBouteille'])

        # Adding model 'Classification'
        db.create_table('cave_classification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True, default='Grand cru')),
        ))
        db.send_create_signal('cave', ['Classification'])

        # Adding model 'Pays'
        db.create_table('cave_pays', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True, default='France')),
        ))
        db.send_create_signal('cave', ['Pays'])

        # Adding model 'Region'
        db.create_table('cave_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('paysR', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cave.Pays'])),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True, default='Bordeaux')),
        ))
        db.send_create_signal('cave', ['Region'])


    def backwards(self, orm):
        # Deleting model 'Cave'
        db.delete_table('cave_cave')

        # Deleting model 'Cellule'
        db.delete_table('cave_cellule')

        # Deleting model 'RefBouteille'
        db.delete_table('cave_refbouteille')

        # Deleting model 'Bouteille'
        db.delete_table('cave_bouteille')

        # Deleting model 'Annee'
        db.delete_table('cave_annee')

        # Deleting model 'Couleur'
        db.delete_table('cave_couleur')

        # Deleting model 'TypeBouteille'
        db.delete_table('cave_typebouteille')

        # Deleting model 'Classification'
        db.delete_table('cave_classification')

        # Deleting model 'Pays'
        db.delete_table('cave_pays')

        # Deleting model 'Region'
        db.delete_table('cave_region')


    models = {
        'cave.annee': {
            'Meta': {'object_name': 'Annee'},
            'annee': ('django.db.models.fields.DateField', [], {'default': "'01/01/2009'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '10', 'unique': 'True', 'default': "'2009'"})
        },
        'cave.bouteille': {
            'Meta': {'object_name': 'Bouteille'},
            'celluleB': ('django.db.models.fields.related.OneToOneField', [], {'null': 'True', 'related_name': "'maBouteille'", 'unique': 'True', 'to': "orm['cave.Cellule']", 'blank': 'True'}),
            'gardeMaxB': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'consoMax'", 'to': "orm['cave.Annee']", 'blank': 'True', 'on_delete': 'models.SET_NULL'}),
            'gardeMinB': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'consoMin'", 'to': "orm['cave.Annee']", 'blank': 'True', 'on_delete': 'models.SET_NULL'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observation': ('django.db.models.fields.TextField', [], {'max_length': '750', 'default': "'Mon observation'"}),
            'partage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prixB': ('django.db.models.fields.DecimalField', [], {'default': "'20'", 'max_digits': '8', 'decimal_places': '2'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'refB': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'maReference'", 'to': "orm['cave.RefBouteille']", 'blank': 'True', 'on_delete': 'models.SET_NULL'})
        },
        'cave.cave': {
            'Meta': {'object_name': 'Cave'},
            'colonnes': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'dateCreation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dateModification': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lieu': ('django.db.models.fields.CharField', [], {'max_length': '500', 'default': "'Ma cave'"}),
            'lignes': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '500', 'default': "'Ma cave'"})
        },
        'cave.cellule': {
            'Meta': {'object_name': 'Cellule'},
            'cave': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'mesCellules'", 'to': "orm['cave.Cave']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'x': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'y': ('django.db.models.fields.IntegerField', [], {'default': '3'})
        },
        'cave.classification': {
            'Meta': {'object_name': 'Classification'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'default': "'Grand cru'"})
        },
        'cave.couleur': {
            'Meta': {'object_name': 'Couleur'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True', 'default': "'Ma couleur'"})
        },
        'cave.pays': {
            'Meta': {'object_name': 'Pays'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'default': "'France'"})
        },
        'cave.refbouteille': {
            'Meta': {'object_name': 'RefBouteille'},
            'anneeB': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'creation'", 'to': "orm['cave.Annee']", 'blank': 'True', 'on_delete': 'models.SET_NULL'}),
            'classificationB': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['cave.Classification']", 'blank': 'True', 'on_delete': 'models.SET_NULL'}),
            'couleurB': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['cave.Couleur']", 'blank': 'True', 'on_delete': 'models.SET_NULL'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageB': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nomB': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'Ma teille'"}),
            'regionB': ('django.db.models.fields.related.OneToOneField', [], {'null': 'True', 'unique': 'True', 'to': "orm['cave.Region']", 'blank': 'True'}),
            'typeB': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['cave.TypeBouteille']", 'blank': 'True', 'on_delete': 'models.SET_NULL'})
        },
        'cave.region': {
            'Meta': {'object_name': 'Region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'default': "'Bordeaux'"}),
            'paysR': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cave.Pays']"})
        },
        'cave.typebouteille': {
            'Meta': {'object_name': 'TypeBouteille'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ml': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '6'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True', 'default': "'Magnum'"}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '10', 'default': "'75cl'"})
        }
    }

    complete_apps = ['cave']