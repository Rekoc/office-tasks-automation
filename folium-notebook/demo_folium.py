import folium

m = folium.Map(location=[43.558214, 5.249263], zoom_start=15)

folium.Marker(
    [43.558678, 5.252096], popup="<i>Mt. Hood Meadows</i>",
    tooltip="Place du Grand Coudoux"
).add_to(m)
folium.Marker(
    [43.558010, 5.251256], popup="<b>Timberline Lodge</b>",
    tooltip="Salle des fêtes et Mairie"
).add_to(m)
folium.Marker(
    [43.558554, 5.254932], popup="<b>Timberline Lodge</b>",
    tooltip="Château de Coudoux"
).add_to(m)
folium.Marker(
    [43.556536, 5.244257], popup="<b>Timberline Lodge</b>",
    tooltip="Parc"
).add_to(m)
folium.Marker(
    [43.557309, 5.244753], popup="<b>Timberline Lodge</b>",
    tooltip="La Poste"
).add_to(m)
m