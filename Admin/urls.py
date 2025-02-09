from django.urls import path
from Admin import views
app_name="webadmin"
urlpatterns = [

  path('Homepage/', views.Homepage,name="Homepage"),

  path('adminReg/', views.adminReg,name="Admin"),
  path('deleteAdmin/<int:id>',views.adminDelete,name="adminRegDelete"),

  
  path('District/', views.district,name="District"),
  path('deleteDistrict/<int:id>',views.districtDelete,name="districtDelete"),
  path('EditAdminReg/<int:id>',views.editadminReg,name="EditAdminReg"),
  path('EditDistrict/<int:id>',views.editDistrict,name="eidDistrict"),


  #path('place',views.place,name="place"),
  path('Place/', views.place,name="Place"),
  path('delPlace/<int:did>', views.delPlace,name="delPlace"),
  path('placeupdate/<int:eid>',views.placeupdate,name="placeupdate"),

  path('Type/', views.Type,name="type"),
  path('delType/<int:id>', views.DeleteType,name="delType"),
  path('typeupdate/<int:id>',views.EditType,name="typeupdate"),
  path('Watt/', views.Watt,name="watt"),
  path('DeleteWatt/<int:id>', views.DeleteWatt,name="DeleteWatt"),
  path('EditWatt/<int:id>', views.EditWatt,name="EditWatt"),

  path("ViewComplaint/",views. ViewComplaint,name="ViewComplaint"),
  path("Reply/<int:rid>",views. Reply,name="Reply"),
  path("ViewFeedback/",views. ViewFeedback,name="ViewFeedback"),

  path("logout/",views. logout,name="logout"),

]