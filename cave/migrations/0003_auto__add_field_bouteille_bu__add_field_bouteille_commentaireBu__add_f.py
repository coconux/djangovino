# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Bouteille.bu'
        db.add_column('cave_bouteille', 'bu',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Bouteille.commentaireBu'
        db.add_column('cave_bouteille', 'commentaireBu',
                      self.gf('django.db.models.fields.TextField')(blank=True, default='Commentaire bu', max_length=750),
                      keep_default=False)

        # Adding field 'Bouteille.partageCommentaireBu'
        db.add_column('cave_bouteille', 'partageCommentaireBu',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Bouteille.cadeau'
        db.add_column('cave_bouteille', 'cadeau',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Bouteille.commentaireCadeau'
        db.add_column('cave_bouteille', 'commentaireCadeau',
                      self.gf('django.db.models.fields.TextField')(blank=True, default='Commentaire cadeau', max_length=750),
                      keep_default=False)

        # Adding field 'Bouteille.offert'
        db.add_column('cave_bouteille', 'offert',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Bouteille.commentaireOffert'
        db.add_column('cave_bouteille', 'commentaireOffert',
                      self.gf('django.db.models.fields.TextField')(blank=True, default='Commentaire', max_length=750),
                      keep_default=False)


        # Changing field 'Bouteille.refB'
        db.alter_column('cave_bouteille', 'refB_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cave.RefBouteille'], default=''))

    def backwards(self, orm):
        # Deleting field 'Bouteille.bu'
        db.delete_column('cave_bouteille', 'bu')

        # Deleting field 'Bouteille.commentaireBu'
        db.delete_column('cave_bouteille', 'commentaireBu')

        # Deleting field 'Bouteille.partageCommentaireBu'
        db.delete_column('cave_bouteille', 'partageCommentaireBu')

        # Deleting field 'Bouteille.cadeau'
        db.delete_column('cave_bouteille', 'cadeau')

        # Deleting field 'Bouteille.commentaireCadeau'
        db.delete_column('cave_bouteille', 'commentaireCadeau')

        # Deleting field 'Bouteille.offert'
        db.delete_column('cave_bouteille', 'offert')

        # Deleting field 'Bouteille.commentaireOffert'
        db.delete_column('cave_bouteille', 'commentaireOffert')


        # Changing field 'Bouteille.refB'
        db.alter_column('cave_bouteille', 'refB_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, to=orm['cave.RefBouteille'], null=True))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'cave.annee': {
            'Meta': {'object_name': 'Annee'},
            'annee': ('django.db.models.fields.DateField', [], {'default': "'01/01/2009'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '10', 'unique': 'True', 'default': "'2009'"})
        },
        'cave.bouteille': {
            'Meta': {'object_name': 'Bouteille'},
            'bu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cadeau': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'celluleB': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'maBouteille'", 'blank': 'True', 'to': "orm['cave.Cellule']", 'unique': 'True', 'null': 'True'}),
            'commentaireBu': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "'Commentaire bu'", 'max_length': '750'}),
            'commentaireCadeau': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "'Commentaire cadeau'", 'max_length': '750'}),
            'commentaireOffert': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "'Commentaire'", 'max_length': '750'}),
            'gardeMaxB': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'consoMax'", 'blank': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['cave.Annee']", 'null': 'True'}),
            'gardeMinB': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'consoMin'", 'blank': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['cave.Annee']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observation': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "'Mon observation'", 'max_length': '750'}),
            'offert': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'partage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'partageCommentaireBu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prixB': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'default': "'20'"}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'refB': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'maReference'", 'to': "orm['cave.RefBouteille']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'monProprioBouteille'", 'to': "orm['auth.User']"})
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
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'monProprio'", 'to': "orm['auth.User']"})
        },
        'cave.cellule': {
            'Meta': {'object_name': 'Cellule'},
            'cave': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mesCellules'", 'blank': 'True', 'to': "orm['cave.Cave']", 'null': 'True'}),
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
            'anneeB': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'creation'", 'blank': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['cave.Annee']", 'null': 'True'}),
            'classificationB': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['cave.Classification']", 'null': 'True'}),
            'couleurB': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['cave.Couleur']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageB': ('django.db.models.fields.files.FileField', [], {'default': "'void.jpeg'", 'max_length': '100'}),
            'nomB': ('django.db.models.fields.CharField', [], {'default': "'Ma teille'", 'max_length': '50'}),
            'regionB': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['cave.Region']", 'null': 'True'}),
            'typeB': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['cave.TypeBouteille']", 'null': 'True'})
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
            'ml': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True', 'default': "'Magnum'"}),
            'volume': ('django.db.models.fields.CharField', [], {'default': "'75cl'", 'max_length': '10'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'db_table': "'django_content_type'", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cave']