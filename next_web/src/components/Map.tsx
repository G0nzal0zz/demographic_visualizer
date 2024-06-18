// components/Map1.js
'use client'
import { useEffect, useRef } from 'react';
import 'ol/ol.css';
import Map from 'ol/Map';
import View from 'ol/View';
import TileLayer from 'ol/layer/WebGLTile.js';
import OSM from 'ol/source/OSM';
import GeoTIFF from 'ol/source/GeoTIFF';
import XYZ from 'ol/source/XYZ';
import { transform } from 'ol/proj';

const key = '9rO47jAmcgTpD0Jgf3Wr';
const attributions =
  '<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> ' +
  '<a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>';

const Map1 = ({ setMap1Object } : any) => {
  const map1Container = useRef<HTMLDivElement>(null);
  // on component mount create the map and set the map references to the state
  useEffect(() => {
    const map1 = new Map({
      target: 'map',
      layers: [
        new TileLayer({
          source: new OSM(),
        }),
        new TileLayer({
          source: new XYZ({
            attributions: attributions,
            url:
              'https://api.maptiler.com/maps/outdoor-v2/256/{z}/{x}/{y}@2x.png?key=' +
              key,
            tilePixelRatio: 2, // THIS IS IMPORTANT
          }),
        }),
      ],
      view: new View({
        projection: 'EPSG:3857',
        center: transform([-112.18688965, 36.057944835], 'EPSG:4326', 'EPSG:3857'),
        zoom: 12,
      }),
    });

    if (map1Container.current) {
      map1.setTarget(map1Container.current);
      setMap1Object(map1);
    }

    // on component unmount remove the map references to avoid unexpected behaviour
    return () => {
      map1.setTarget(undefined);
      setMap1Object(null);
    };
  }, []);

  return (<><div ref={map1Container} className="w-full h-96"></div></>);
};

export default Map1;
