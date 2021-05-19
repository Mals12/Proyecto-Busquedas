
var mymap = L.map('mapid').setView([19.046250, -96.259722], 7);

var apiKey = 'pk.eyJ1IjoibWlrZXNhbmRyaWEiLCJhIjoiY2tvb2xwb3hwMGFwejJ2cXI0aGk2OHd6OCJ9.ueHTwlCUkTTCVDZNizcrSg'

L.tileLayer(`https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=${apiKey}`, {
	maxZoom: 18,
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
		'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
		'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
	id: 'mapbox/streets-v11',
	tileSize: 512,
	zoomOffset: -1
}).addTo(mymap);

function creaIcono(ruta, width, height) {
	var icono = L.icon({
		iconUrl: ruta,
		iconSize: [width, height], 
	});
	return icono;
}

var locations = {
	'xalapa': {
		'titulo': 'Xalapa',
		'coordenadas': [19.54377, -96.91018],
		//'icon':creaIcono('images/xalapapng.png', 18, 31)
	},
	'zempoala': {
		'titulo': 'Zempoala',
		'coordenadas': [19.44688, -96.40507]
		//'icon':creaIcono('images/zempoalapng.png', 18, 31)
	},
	'vega': {
		'titulo': 'Vega de Alatorre',
		'coordenadas': [20.03034, -96.65044]
		//'icon':creaIcono('images/vegapng.png', 18, 31)
	},
	'papantla': {
		'titulo': 'Papantla',
		'coordenadas': [20.45667, -97.31561],
		//'icon':creaIcono('images/papantlapng.png', 18, 31)
	},
	'tecolutla': {
		'titulo': 'Tecolutla',
		'coordenadas': [20.47955, -97.01012],
		//'icon':creaIcono('images/tecolutlapng.png', 18, 31)
	},
	'teziutlan': {
		'titulo': 'Teziutlán',
		'coordenadas': [19.81601, -97.35705],
		//'icon':creaIcono('images/teziutlanpng.png', 18, 31)
	},
	'huatusco': {
		'titulo': 'Huatusco',
		'coordenadas': [19.14823, -96.96654],
		//'icon':creaIcono('images/huatuscopng.png', 18, 31)
	},
	'boca': {
		'titulo': 'Boca del Río',
		'coordenadas': [19.10627, -96.10632],
		//'icon':creaIcono('images/boca del riopng.png', 18, 31)
	},
	'fortin': {
		'titulo': 'Fortín de las Flores',
		'coordenadas': [18.9017, -96.99896],
		//'icon':creaIcono('images/fortinpng.png', 18, 31)
	},
	'yanga': {
		'titulo': 'Yanga',
		'coordenadas': [18.82928, -96.80027],
		//'icon':creaIcono('images/yangapng.png', 18, 31)
	},
	'alvarado': {
		'titulo': 'Alvarado',
		'coordenadas': [18.76961, -95.75894],
		//'icon':creaIcono('images/alvaradopng.png', 18, 31)
	},
	'joachin': {
		'titulo': 'Joachín',
		'coordenadas': [18.6407, -96.23095]
		//'icon':creaIcono('images/joachinpng.png', 18, 31)
	},
	'acayucan': {
		'titulo': 'Acayucan',
		'coordenadas': [17.94919, -94.91459]
		//'icon':creaIcono('images/acayucanpng.png', 18, 31)
	},
	'huautla': {
		'titulo': 'Huautla de Jiménez',
		'coordenadas': [18.13108, -96.84314],
		//'icon':creaIcono('images/huautla de jimenezpng.png', 18, 31)
	},
	'otatitlan': {
		'titulo': 'Otatitlán',
		'coordenadas': [18.18106, -96.03439],
		//'icon':creaIcono('images/otitlanpng.png', 18, 31)
	},
	'sanandres': {
		'titulo': 'San Andrés Tuxtla',
		'coordenadas': [18.44412, -95.21302],
		//'icon':creaIcono('images/San andrespng.png', 18, 31)
	},
	'mina': {
		'titulo': 'Minatitlán',
		'coordenadas': [17.99392, -94.5466],
		//'icon':creaIcono('images/minatitlanpng.png', 18, 31)
	},
	'nigromante': {
		'titulo': 'El Nigromante',
		'coordenadas': [17.76323, -95.75574],
		//'icon':creaIcono('images/nigromantepng.png', 18, 31)
	},
	'coatza': {
		'titulo': 'Coatzacoalcos',
		'coordenadas': [18.13447, -94.45898],
		//'icon':creaIcono('images/coatzacoalcospng.png', 18, 31)
	},
	'agua': {
		'titulo': 'Agua Dulce',
		'coordenadas': [18.14259, -94.1436],
		//'icon':creaIcono('images/agua dulcepng.png', 18, 31)
	},
};

Object.entries(locations).forEach(site => pintaMarker(site));

function pintaMarker(item) {
	//console.log(item);
	if (item[1].icon) {
		var marker = L.marker(item[1].coordenadas, {'title': item[1].titulo, icon: item[1].icon}).addTo(mymap);
	} else {
		var marker = L.marker(item[1].coordenadas, {'title': item[1].titulo}).addTo(mymap);
	}

}

// create a red polyline from an array of LatLng points
var ruta1 = [
	locations.xalapa.coordenadas,
	locations.zempoala.coordenadas,
	locations.vega.coordenadas,
	locations.tecolutla.coordenadas,
	locations.papantla.coordenadas,
	locations.teziutlan.coordenadas,
	locations.xalapa.coordenadas,
	locations.huatusco.coordenadas,
	locations.fortin.coordenadas,
	locations.huautla.coordenadas,
	locations.otatitlan.coordenadas,
	locations.nigromante.coordenadas,
	locations.acayucan.coordenadas,
	locations.mina.coordenadas,
	locations.coatza.coordenadas,
	locations.agua.coordenadas,
	locations.coatza.coordenadas,
	locations.sanandres.coordenadas,
	locations.alvarado.coordenadas,
	locations.otatitlan.coordenadas,
	locations.joachin.coordenadas,
	locations.yanga.coordenadas,
	locations.fortin.coordenadas,
	
];
var ruta2 = [
	locations.papantla.coordenadas,
	locations.vega.coordenadas,
	locations.xalapa.coordenadas,
	locations.boca.coordenadas,
	locations.joachin.coordenadas,
];
var ruta3 = [
	locations.zempoala.coordenadas,
	locations.boca.coordenadas,
	locations.alvarado.coordenadas,
	locations.sanandres.coordenadas,
	locations.acayucan.coordenadas,
];

var polyline = L.polyline(ruta1, {color: 'red'}).addTo(mymap);
var polyline = L.polyline(ruta2, {color: 'red'}).addTo(mymap);
var polyline = L.polyline(ruta3, {color: 'red'}).addTo(mymap);

//console.log(mymap.distance(locations.xalapa.coordenadas, locations.zempoala.coordenadas) + ' metros');
//console.log(mymap.distance(locations.xalapa.coordenadas, locations.zempoala.coordenadas) + ' metros');
for(var et in locations)
{
	for(var it in locations)
	{
		console.log(mymap.distance(locations[et].coordenadas, locations[it].coordenadas) + ' metros');
	}
}