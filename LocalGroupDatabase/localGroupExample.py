# Example of extracting data from the Local Group galaxy data file. This example simply extracts the stellar masses of each galaxy
# and lists these values along with galaxy name.

import xml.etree.ElementTree as etree

tree = etree.parse('localGroupSatellites.xml')
root = tree.getroot()
galaxyDatabase = root.findall('galaxies')[0]
galaxies = galaxyDatabase.findall('galaxy')
for galaxy in galaxies:
    name = galaxy.findall('name')[0]
    mass = galaxy.findall('massStellar')
    dynamical = galaxy.findall('massDynamicalHalfLightRadius')
    if len(mass) > 0 and len(dynamical) > 0:
        massValue = mass[0].findall('value')[0]
        dynamicalValue = dynamical[0].findall('value')[0]
        print massValue.text,dynamicalValue.text,name.text
