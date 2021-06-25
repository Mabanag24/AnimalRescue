from django.test import TestCase
# from petlist.models import Item, petcat
# # from django.http import HttpRequest
# # 09/19/2021
# # from django.http import HttpRequest
# # from django.template.loader import render_to_string
	
# class HomePageTest(TestCase):
# 	def test_mainpage_returns_correct_view(self):
# 		response = self.client.get('/')
# 		self.assertTemplateUsed(response,'mainpage.html')
		


# class ORMTest(TestCase):
# 	def test_saving_retrieving_list(self):
# 		Franky = petcat()
# 		Franky.save()
# 		txtItem1 = Item()
# 		txtItem1.text = 'Item one'
# 		txtItem1.pets = Franky
# 		txtItem1.save()
# 		txtItem2 = Item()
# 		txtItem2.pets = Franky
# 		txtItem2.text = 'Item two'
# 		txtItem2.save()
# 		savedItems = Item.objects.all()
# 		savedfranky = petcat.objects.first()
# 		self.assertEqual(savedItems.count(), 2)
# 		self.assertEqual(savedfranky,Franky)
# 		savedItem1 = savedItems[0]
# 		savedItem2 = savedItems[1]
# 		self.assertEqual(savedItem1.text, 'Item one')
# 		self.assertEqual(savedItem2.text, 'Item two')
# 		self.assertEqual(savedItem1.pets, Franky)
# 		self.assertEqual(savedItem2.pets, Franky)			



# class ViewTest(TestCase):
# 	def test_displays_each_saved(self):
# 		Franky = petcat.objects.create()
# 		Item.objects.create(pets=Franky, text='Pedro')
# 		Item.objects.create(pets=Franky, text='Sergio')
# 		response = self.client.get(f'/petlist/{Franky.id}/')
# 		self.assertContains(response, 'Pedro')
# 		self.assertContains(response, 'Sergio')
# 		self.assertNotContains(response, 'Lucifer')
# 		self.assertNotContains(response, 'Morningstar')
		
# 		Franky_2 = petcat.objects.create()
# 		Item.objects.create(pets=Franky_2, text='Lucifer')
# 		Item.objects.create(pets=Franky_2, text='Morningstar')
# 		response = self.client.get(f'/petlist/{Franky_2.id}/')
# 		self.assertContains(response, 'Lucifer')
# 		self.assertContains(response, 'Morningstar')

		
# 	def test_listview_uses_animal_page(self):
# 		Franky = petcat.objects.create()
# 		response = self.client.get(f'/petlist/{Franky.id}/')
# 		self.assertTemplateUsed(response, 'animalinfo.html')

# 	def test_pass_list_to_template(self):
# 		PL1 = petcat.objects.create()
# 		PL2 = petcat.objects.create()
# 		passList = petcat.objects.create()
# 		response = self.client.get(f'/petlist/{passList.id}/')
# 		self.assertEqual(response.context['pets'], passList)



# class CreateListTest(TestCase):
# 	def test_save_POST_request(self):
# 		response = self.client.post('/petlist/dobelist',data={'Superpet':'New entry'})	
# 		self.assertEqual(Item.objects.count(),1)
# 		newItem = Item.objects.first()
# 		self.assertEqual(newItem.text, 'New entry')

# 	def test_redirects_POST(self):
# 		response = self.client.post('/petlist/dobelist',data={'Superpet':'New entry'})
# 		newpetss = petcat.objects.first()
# 		self.assertRedirects(response, f'/petlist/{newpetss.id}/')

# class Add_Item_test(TestCase):
# 	def test_add_POST_request_to_existing_list(self):
# 		Pl1 = petcat.objects.create()
# 		PL2 = petcat.objects.create()
# 		userlist = petcat.objects.create()
# 		self.client.post(f'/petlist/{userlist.id}/petitem',data={'Superpet': 'New item for userlist'})
# 		self.assertEqual(Item.objects.count(),1)
# 		newItem = Item.objects.first()
# 		self.assertEqual(newItem.text, 'New item for userlist')
# 		self.assertEqual(newItem.pets, userlist)

# 	def test_redirects_to_list_view(self):
# 	 	PL1 = petcat.objects.create()
# 	 	PL2 = petcat.objects.create()
# 	 	userlist = petcat.objects.create()
# 	 	response = self.client.post(f'/petlist/{userlist.id}/petitem',data={'Superpet': 'New item for userlist'})
# 	 	self.assertRedirects(response, f'/petlist/{userlist.id}/')		