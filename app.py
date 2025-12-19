from flask import Flask, render_template_string
import json
app=Flask(__name__)
points=[
    {"lat":52.229676,"lng":21.012229,"title":"Warszawa"},
    {"lat":50.06465,"lng":19.94498,"title":"Kraków"},
    {"lat":51.107883,"lng":17.038538,"title":"Wrocław"}
]
template='''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
  <title>Map</title>
  <style>html,body,#map{height:100%;margin:0;padding:0}</style>
</head>
<body>
  <div id="map"></div>
  <script>
    window.points={{ points|safe }};
    function initMap(){
      const pts=window.points;
      const center=pts.length?{lat:pts[0].lat,lng:pts[0].lng}:{lat:0,lng:0};
      const map=new google.maps.Map(document.getElementById('map'),{zoom:6,center});
      const bounds=new google.maps.LatLngBounds();
      pts.forEach(p=>{
        const marker=new google.maps.Marker({position:{lat:p.lat,lng:p.lng},map,title:p.title});
        bounds.extend(marker.getPosition());
      });
      if(pts.length>1) map.fitBounds(bounds);
    }
  </script>
  <script async defer src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap"></script>
</body>
</html>'''
@app.route('/')
def index():
    return render_template_string(template,points=json.dumps(points))
if __name__=='__main__':
    app.run(debug=True)