// Main Landing Page "/" with dual maps
'use client'
import { useEffect, useState } from "react";
import Map1 from "@/components/Map";
import 'ol-ext/dist/ol-ext.css';
import { Button } from "@/components/ui/button"

function DualMap() {
  const [map1Object, setMap1Object] = useState(null);
  return (
    <>
      <header className="flex h-16 w-full gap-4 items-center justify-center border-b">
        <Button onClick={() => console.log('clicked')}>Click me</Button>
      </header>
        <Map1 setMap1Object={setMap1Object} />
      {/* Uncomment the following line when Map1 is ready to be used */}
    </>
  );
}

export default DualMap;