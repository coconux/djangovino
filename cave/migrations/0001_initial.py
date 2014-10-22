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
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='monProprio')),
            ('nom', self.gf('django.db.models.fields.CharField')(default='Ma cave', max_length=500)),
            ('lieu', self.gf('django.db.models.fields.CharField')(default='Ma cave', max_length=500)),
            ('lignes', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('colonnes', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('dateCreation', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('dateModification', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
        ))
        db.send_create_signal('cave', ['Cave'])

        # Adding model 'Cellule'
        db.create_table('cave_cellule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cave', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['cave.Cave'], related_name='mesCellules')),
            ('x', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('y', self.gf('django.db.models.fields.IntegerField')(default=3)),
        ))
        db.send_create_signal('cave', ['Cellule'])

        # Adding model 'RefBouteille'
        db.create_table('cave_refbouteille', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nomB', self.gf('django.db.models.fields.CharField')(default='Ma teille', max_length=50)),
            ('typeB', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, blank=True, to=orm['cave.TypeBouteille'], null=True)),
            ('couleurB', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, blank=True, to=orm['cave.Couleur'], null=True)),
            ('classificationB', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, blank=True, to=orm['cave.Classification'], null=True)),
            ('anneeB', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, blank=True, to=orm['cave.Annee'], related_name='creation')),
            ('regionB', self.gf('django.db.models.fields.related.OneToOneField')(null=True, blank=True, to=orm['cave.Region'], unique=True)),
            ('imageB', self.gf('django.db.models.fields.files.FileField')(default='void.jpeg', max_length=100)),
        ))
        db.send_create_signal('cave', ['RefBouteille'])

        # Adding model 'Bouteille'
        db.create_table('cave_bouteille', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='monProprioBouteille')),
            ('refB', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, blank=True, to=orm['cave.RefBouteille'], related_name='maReference')),
            ('gardeMinB', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, blank=True, to=orm['cave.Annee'], related_name='consoMin')),
            ('gardeMaxB', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, blank=True, to=orm['cave.Annee'], related_name='consoMax')),
            ('prixB', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2, default='20')),
            ('celluleB', self.gf('django.db.models.fields.related.OneToOneField')(null=True, blank=True, to=orm['cave.Cellule'], related_name='maBouteille', unique=True)),
            ('rating', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('partage', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('observation', self.gf('django.db.models.fields.TextField')(default='Mon observation', max_length=750)),
        ))
        db.send_create_signal('cave', ['Bouteille'])

        # Adding model 'Annee'
        db.create_table('cave_annee', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(unique=True, default='2009', max_length=10)),
            ('annee', self.gf('django.db.models.fields.DateField')(default='01/01/2009')),
        ))
        db.send_create_signal('cave', ['Annee'])

        # Adding model 'Couleur'
        db.create_table('cave_couleur', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(unique=True, default='Ma couleur', max_length=50)),
        ))
        db.send_create_signal('cave', ['Couleur'])

        # Adding model 'TypeBouteille'
        db.create_table('cave_typebouteille', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(unique=True, default='Magnum', max_length=50)),
            ('volume', self.gf('django.db.models.fields.CharField')(default='75cl', max_length=10)),
            ('ml', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal('cave', ['TypeBouteille'])

        # Adding model 'Classification'
        db.create_table('cave_classification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(unique=True, default='Grand cru', max_length=100)),
        ))
        db.send_create_signal('cave', ['Classification'])

        # Adding model 'Pays'
        db.create_table('cave_pays', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(unique=True, default='France', max_length=100)),
        ))
        db.send_create_signal('cave', ['Pays'])

        # Adding model 'Region'
        db.create_table('cave_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('paysR', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cave.Pays'])),
            ('nom', self.gf('django.db.models.fields.CharField')(unique=True, default='Bordeaux', max_length=100)),
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
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"}),
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
            'celluleB': ('django.db.models.fields.related.OneToOneField', [], {'null': 'True', 'blank': 'True', 'to': "orm['cave.Cellule']", 'related_name': "'maBouteille'", 'unique': 'True'}),
            'gardeMaxB': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True', 'to': "orm['cave.Annee']", 'related_name': "'consoMax'"}),
            'gardeMinB': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True', 'to': "orm['cave.Annee']", 'related_name': "'consoMin'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observation': ('django.db.models.fields.TextField', [], {'default': "'Mon observation'", 'max_length': '750'}),
            'partage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prixB': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'default': "'20'"}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'refB': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True', 'to': "orm['cave.RefBouteille']", 'related_name': "'maReference'"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'monProprioBouteille'"})
        },
        'cave.cave': {
            'Meta': {'object_name': 'Cave'},
            'colonnes': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'dateCreation': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'dateModification': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lieu': ('django.db.models.fields.CharField', [], {'default': "'Ma cave'", 'max_length': '500'}),
            'lignes': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'nom': ('django.db.models.fields.CharField', [], {'default': "'Ma cave'", 'max_length': '500'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'monProprio'"})
        },
        'cave.cellule': {
            'Meta': {'object_name': 'Cellule'},
            'cave': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['cave.Cave']", 'related_name': "'mesCellules'"}),
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
            'anneeB': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True', 'to': "orm['cave.Annee']", 'related_name': "'creation'"}),
            'classificationB': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'blank': 'True', 'to': "orm['cave.Classification']", 'null': 'True'}),
            'couleurB': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'blank': 'True', 'to': "orm['cave.Couleur']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageB': ('django.db.models.fields.files.FileField', [], {'default': "'void.jpeg'", 'max_length': '100'}),
            'nomB': ('django.db.models.fields.CharField', [], {'default': "'Ma teille'", 'max_length': '50'}),
            'regionB': ('django.db.models.fields.related.OneToOneField', [], {'null': 'True', 'blank': 'True', 'to': "orm['cave.Region']", 'unique': 'True'}),
            'typeB': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'blank': 'True', 'to': "orm['cave.TypeBouteille']", 'null': 'True'})
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
            'ml': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'default': "'Magnum'", 'max_length': '50'}),
            'volume': ('django.db.models.fields.CharField', [], {'default': "'75cl'", 'max_length': '10'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cave']